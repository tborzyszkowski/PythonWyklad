#!/usr/bin/env python3

import inspect
import importlib.util
import os, sys
from collections import OrderedDict

import writer
from writer import line, lfold, tufold, block_norm, block_to_text

def instance(x):
	''' Flag for classes that want to have their instance predefined '''
	x._instance = True
	return x

def get_arguments():
	import argparse
	parser = argparse.ArgumentParser()

	parser.add_argument('src', help='Source file of lambdas definitions')
	parser.add_argument('declarations', help='Destination file for generated declarations')
	parser.add_argument('definitions', help='Destination file for generated definitions')

	return parser.parse_args()

def get_module_name(path: str):
	bname = os.path.basename(path)
	split = os.path.splitext(bname)
	return split[0]

def load_dynamic(path: str):
	module_name = get_module_name(path)
	spec = importlib.util.spec_from_file_location(module_name, path)

	re = importlib.util.module_from_spec(spec)
	spec.loader.exec_module(re)

	return re

def get_classes(mod) -> list:
	ret = []
	mems = inspect.getmembers(mod)
	for name, obj in mems:
		if (inspect.isclass(obj)):
			ret.append(obj)
	return ret

class lambda_obj:
	def __init__(self, target_class):
		self.target_class = target_class
		self.name = target_class.__name__

		v    = dict ( vars (target_class) )
		filt = filter( lambda k: type( v[k] ) is tuple and not k.startswith('_'), v)
		di   = dict ( map( lambda k: (k, v[k]), filt) )
		self.mems = di

		self.exec_func = lambda_obj.func(target_class.exec)
		self.cache_func = lambda_obj.func(target_class.cache) if 'cache' in vars(target_class) else None

		self.pure = not self.cache_func is None
		self.insance = '_instance' in vars(target_class)

	def custom_name(self) -> str:
		return 'Custom_' + self.name
	def bind_name(self) -> str:
		return 'Bind_' + self.name
	def carry_custom_name(self, argument_index: int) -> str:
		return 'CustomPriv_{}_{}'.format(self.name, argument_index)
	def carry_bind_name(self, argument_index: int) -> str:
		return 'BindPriv_{}_{}'.format(self.name, argument_index)

	class func:
		def __init__(self, f):
			self.f = f
			self.sign = inspect.signature(f)
			self.name = f.__name__
			self.args = OrderedDict(self.sign.parameters)
			self.args_pre = list(self.args)[:-1]

			self.code = f.__doc__
			if not self.code:
				return

			codepre = ''
			for arg in self.args:
				if self.args[arg].annotation is inspect._empty:
					codepre += '	ff {name} = ${name};\n'.format(name = arg)
				else:
					arg_t = self.args[arg].annotation.__name__
					codepre += tufold(block_norm('''
						ff {name}_base = (eval(${name}, fin));
						struct Custom_{t} * {name} = {name}_base->custom;
					#ifdef USE_TYPEID
						if ({name}_base->typeuuid != Typeid_Bind_{t}) {{
							return lambda_error("Type: expected type %d ({t}) / got type %d", Typeid_Bind_{t}, {name}_base->typeuuid);
						}}
					#endif
					''', 0)).format(t = arg_t, name = arg)

			if not self.sign.return_annotation is inspect._empty:
				arg_t = self.sign.return_annotation.__name__
				codepre += tufold(block_norm('''
				ff ret = Init_Bind_{t}(NULL);
				if (ret == NULL) {{
					return lambda_error("Initialization: failed of type {t} during exec of type {name}");
				}}
				struct Custom_{t} * rc = ret->custom;
				''', 1)).format(t = arg_t, name=arg)

			self.code = tufold(block_norm(self.code, 1))
			self.code = codepre + self.code

			curr_str = 'me_abs'
			for a in reversed(self.args):
				self.code = self.code.replace('$' + a, curr_str + '->x')
				curr_str += '->parent'

def loadcfg(path: str) -> list:
	mod = load_dynamic(path)
	cl = get_classes(mod)
	objs = list(map(lambda_obj, cl))

	return objs

def get_struct_decl(o: lambda_obj) -> str:
	return 'struct ' + o.custom_name()
def get_carry_struct_decl(o: lambda_obj, argument_index: int) -> str:
	return 'struct ' + o.carry_custom_name(argument_index)

def get_carry_definition(o: lambda_obj, argument_index: int) -> str:
	return 'struct {} {{ }};'.format(o.carry_custom_name(argument_index))

def get_definition(o: lambda_obj) -> str:
	re = ''
	if len(o.exec_func.args) > 1:
		for i, a in enumerate(o.exec_func.args_pre):
			re += get_carry_definition(o, i) + '\n'

	re += 'struct Custom_{} {{\n'.format(o.name)
	for m in o.mems:
		re += '	{} {};\n'.format(o.mems[m][0], m)

	if o.insance:
		re += '	Bind_{name}() {{ Init_Bind_{name}(this); }} \n'.format(name=o.name)
		re += '}} Instance_Bind_{};'.format(o.name)
	else:
		re += '};'

	return re

def get_typeid_str(o: lambda_obj) -> str:
	return 'const int Typeid_{} = __COUNTER__ ;'.format(o.bind_name())
def get_carry_typeid_str(o: lambda_obj, argument_index: int):
	return 'const int Typeid_{} = __COUNTER__;'.format(o.carry_bind_name(argument_index))

def get_init_decl(o: lambda_obj) -> str:
	return 'ff Init_{name} (ff parent)'.format(name=o.bind_name())
def get_carry_init_decl(o: lambda_obj, argument_index: int) -> str:
	return 'ff Init_{name} (ff parent)'.format(name=o.carry_bind_name(argument_index))

def get_init_func(o: lambda_obj) -> str:
	def get_common_init(bindname: str, customname: str, mems: dict, decl: str) -> str:
		members = tufold([(1, 'custom->{} = {};'.format(m, mems[m][1])) for m in mems])

		return block_to_text(0,
			'''
			{decl} {{
				ff me = ALLOC_GET(sizeof(struct fun));
				me->x = NULL;
				me->parent = parent;
				me->eval_now = Exec_{bindname};

				me->custom = ALLOC_GET(sizeof(struct {customname}));
				struct {customname} * custom = me->custom;
				me->customsize = sizeof(struct {customname});

			{members}

			#ifdef USE_TYPEID
				me->typeuuid = Typeid_{bindname};
			#endif
			#ifdef DO_CACHING
				me->cache = Cache_{bindname};
			#endif

				return me;
			}}
			'''
		).format(
			decl=decl,
			members=members,
			bindname=bindname,
			customname=customname)

	re = get_common_init(o.bind_name(), o.custom_name(), o.mems, get_init_decl(o))

	if len(o.exec_func.args) > 1:
		for (i, arg) in enumerate(o.exec_func.args_pre):
			re += get_common_init(o.carry_bind_name(i), o.carry_custom_name(i), {}, get_carry_init_decl(o, i))

	return re

def get_cache_decl(o: lambda_obj) -> str:
	return 'int Cache_{} (ff me_abs, mapkey_t * ret, recursion_set * set)'.format(o.bind_name())
def get_carry_cache_decl(o: lambda_obj, argument_index: int) -> str:
	return 'int Cache_{} (ff me_abs, mapkey_t * ret, recursion_set * set)'.format(o.carry_bind_name(argument_index))
def get_cache_func(o: lambda_obj) -> str:
	if o.pure:
		def common(bindname: str, customname: str, decl: str, rest: list, custom_code: str, carry_index: int) -> list:
			# use custom code from cache function doc

			# call cache function to get the rest
			custom_mems = []
			for r in rest:
				custom_mems.append('list_add(ret, {});'.format(r))
			custom_mems = lfold(custom_mems)
			custom_mems = tufold(block_norm(custom_mems, 1))

			custom_block = ''
			if custom_code:
				custom_block = tufold(block_norm(custom_code, 1))

			previus_xs = ''
			current_parent = 'me_abs->parent'
			for i in range(carry_index):
				previus_xs += line('list_add(ret, {p}->x->cache({p}->x, ret, set));'.format(p=current_parent), 1)
				current_parent += '->parent'

			return tufold(block_norm('''
				{declaration} {{
					struct {customname} * me = me_abs->custom;

					if (recset_check(set, me_abs)) {{
						list_add(ret, -2);
						return false;
					}} else {{
						recset_add(set, me_abs);
					}}

					list_add(ret, -9);
					list_add(ret, Typeid_{bindname});

					if (me_abs->x) {{
						list_add(ret, me_abs->x->cache(me_abs->x, ret, set));
					}} else {{
						list_add(ret, -1);
					}}

				{previus_xs}

				{custom_block}
				{custom_mems}

					return false;
				}}
				''', 0)).format(
						declaration=decl,
						custom_block=custom_block,
						custom_mems=custom_mems,
						previus_xs=previus_xs,
						bindname=bindname,
						customname=customname)

		re = ''
		re += common(o.bind_name(), o.custom_name(), get_cache_decl(o), rest=o.cache_func.f(), custom_code=o.cache_func.code, carry_index=0)
		if len(o.exec_func.args) > 1:
			for (i, arg) in enumerate(o.exec_func.args_pre):
				re += common(o.carry_bind_name(i), o.carry_custom_name(i), get_carry_cache_decl(o, i), rest=[], custom_code=[], carry_index=(i + 1))
		return re
	else:
		def common(decl: str) -> str:
			return tufold(block_norm('''
				{declaration} {{
					return true;
				}}
				'''.format(declaration=decl), 0))

		re = ''
		if len(o.exec_func.args) > 1:
			for (i, arg) in enumerate(o.exec_func.args_pre):
				re += common(get_carry_cache_decl(o, i))
		re += common(get_cache_decl(o))
		return re

def get_exec_decl(o: lambda_obj) -> str:
	return 'ff Exec_{} (ff me_abs, ff __x)'.format(o.bind_name())
def get_carry_exec_decl(o: lambda_obj, argument_index: int) -> str:
	return 'ff Exec_{} (ff me_abs, ff __x)'.format(o.carry_bind_name(argument_index))
def get_exec_func(o: lambda_obj) -> str:
	def last_arg(fullname: str, decl: str, code: str) -> str:
		return tufold(block_norm('''
			{declaration} {{
				struct {name} * custom = me_abs->custom;
			{code}
			}}
			''', 0)).format(
						declaration = decl,
						code        = code,
						name        = fullname)

	if len(o.exec_func.args) > 1:
		def carry_common(decl, fullname, ret_t: str) -> str:
			return tufold(block_norm('''
				{declaration} {{
					struct {name} * custom = me_abs->custom;

					ff ret = Init_{ret_t}(NULL);
					if (ret == NULL) {{
						fprintf(stderr, "%s", "Could not initialize type {ret_t} \\n");
					}}
					ret->parent = me_abs;

					return ret;
				}}
				''', 0)).format(
							declaration = decl,
							name = fullname,
							ret_t = ret_t)

		re = ''

		re += carry_common(
			decl     = get_exec_decl(o),
			fullname = o.custom_name(),
			ret_t    = o.carry_bind_name(0)) + '\n'

		for (i, arg) in enumerate(o.exec_func.args_pre[:-1]):
			# ret_t = o.exec_func.args_pre[i + 1]
			ret_t = o.carry_bind_name(i + 1)
			re += carry_common(
				decl     = get_carry_exec_decl(o, i),
				fullname = o.carry_custom_name(i),
				ret_t    = ret_t )

		re += last_arg(
			decl     = get_carry_exec_decl(o, len(o.exec_func.args_pre) - 1),
			fullname = o.carry_custom_name(len(o.exec_func.args_pre) - 1),
			code     = o.exec_func.code)

		return re
	else:
		return last_arg(
			fullname = o.custom_name(),
			decl     = get_exec_decl(o),
			code     = o.exec_func.code)

def write(objs, args):

	with open(args.declarations, 'w') as declarations_f:
		fs = [(get_struct_decl, get_carry_struct_decl),
		      (get_init_decl, get_carry_init_decl),
		      (get_exec_decl, get_carry_exec_decl)
			  ]

		for o in objs:
			if len(o.exec_func.args) > 1:
				for (i, arg) in enumerate(o.exec_func.args_pre):
					declarations_f.write(get_carry_typeid_str(o, i))
					declarations_f.write('\n')
			declarations_f.write(get_typeid_str(o))
			declarations_f.write('\n')
		declarations_f.write('\n')

		for f in fs:
			(main, pre) = f
			for o in objs:
				if len(o.exec_func.args) > 1:
					for (i, arg) in enumerate(o.exec_func.args_pre):
						declarations_f.write(pre(o, i))
						declarations_f.write(';\n')
				declarations_f.write(main(o))
				declarations_f.write(';\n')
			declarations_f.write('\n')

		declarations_f.write('#ifdef DO_CACHING\n')
		for o in objs:
			if len(o.exec_func.args) > 1:
				for (i, arg) in enumerate(o.exec_func.args_pre):
					declarations_f.write(get_carry_cache_decl(o, i))
					declarations_f.write(';\n')
			declarations_f.write(get_cache_decl(o))
			declarations_f.write(';\n')
		declarations_f.write('#endif\n')

	with open(args.definitions, 'w') as definitions_f:
		fs = [get_definition,
		      get_init_func,
		      get_exec_func]

		for f in fs:
			for o in objs:
				definitions_f.write(f(o))
				definitions_f.write('\n\n')

		definitions_f.write('#ifdef DO_CACHING\n')
		for o in objs:
			definitions_f.write(get_cache_func(o))
			definitions_f.write('\n\n')
		definitions_f.write('#endif\n')

def main():
	args = get_arguments()
	objs = loadcfg(args.src)
	write(objs, args)
	print('done')

if __name__ == '__main__':
	main()

