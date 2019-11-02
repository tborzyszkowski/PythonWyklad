
LAMBDA_SYMBOL = '->'
LAMBDA_DECL   = '\\'

def find_first_char(s: str, stops: list):
	for i in range(len(s)):
		sub = s[i:]
		for k in stops:
			if sub.startswith(k):
				return i
	return -1
def find_first_sub(s: str, subs: list, start: int = 0):
	for i in range(len(s)):
		if i < start: continue
		for k in subs:
			if s.startswith(k, i):
				return i
	return -1
def find_next_bracket(s: str):
	count = 0
	for i, c in enumerate(s):
		if c == '(': count += 1
		elif c == ')':
			count -= 1
			if count == 0:
				return i
	return -count

class Branch:
	def __init__(self, text: str, branches: list, is_lambda: bool, is_token: bool, is_arg: bool):
		self.text = text
		self.branches = branches
		self.is_lambda = is_lambda
		self.is_token = is_token
		self.is_arg = is_arg

	@staticmethod
	def from_text(original: str):
		expr = original.strip()
		# print('branch="{}"'.format(expr))

		is_lambda = expr.startswith(LAMBDA_DECL)

		re = Branch(None, [], is_lambda=is_lambda, is_token=False, is_arg=False)

		if is_lambda:
			stop = find_first_sub(expr, [' ', LAMBDA_SYMBOL], start=1)
			if stop < 0:
				raise RuntimeError('Lambda expression "{}" has no body!'.format(expr))
			argname = expr[1:stop]
			re.branches.append( Branch(argname, [], is_lambda=False, is_token=True, is_arg=True) )
			expr = expr[stop:]

		while len(expr) > 0:
			if expr[0].isspace():   # skip
				expr = expr[1:]
				continue
			elif expr.startswith(LAMBDA_SYMBOL):     # skip
				expr = expr[len(LAMBDA_SYMBOL):]
				continue
			elif expr.startswith(LAMBDA_DECL):       # lambda
				sub = Branch.from_text(expr)
				size = len(sub.branches)
				if size == 0:
					raise RuntimeError('Sub-expression "{}" of expression "{}" cannot be empty!'.format(body, expr))
				elif size == 1:
					re.branches.append(sub.branches[0])
				else:
					re.branches.append(sub)

				expr = ''
			elif expr[0] == '(':    # another branch
				stop = find_next_bracket(expr)
				if stop < 0:
					raise RuntimeError('Wrong number of brackets: need {} more ")"!'.format(stop))
				body = expr[1:stop]
				sub = Branch.from_text(body)
				size = len(sub.branches)
				if size == 0:
					raise RuntimeError('Sub-expression "{}" of expression "{}" cannot be empty!'.format(body, expr))
				elif size == 1:
					re.branches.append(sub.branches[0])
				else:
					re.branches.append(sub)

				expr = expr[stop + 1:]
			else: # simple token
				stop = find_first_char(expr, [' ', '(', LAMBDA_DECL])
				if stop < 0:
					stop = len(expr)
				tok = expr[0:stop]
				re.branches.append(Branch(tok, [], is_lambda=False, is_token=True, is_arg=False))
				expr = expr[stop:]
		return re

class Leaf:
	counter = 0

	def __init__(self, leafs: list, parent):
		self.leafs = leafs
		self.parent = parent

		self.unique_id = Leaf.counter
		Leaf.counter += 1

	def print(self, indent: int):
		i_str = '\t' * indent
		l_str = '\n'.join(map ( lambda l: l.print(indent + 1), self.leafs))
		return l_str
	def __eq__(self, other) -> bool:
		return self.unique_id == other.unique_id
	def __ne__(self, other) -> bool:
		return not self == other

	# TODO: should I increment index on every parent, or only when the parent is Lambda?
	def get_argument_index(self, arg) -> int:
		''' How far up argument is declared '''
		re = 0
		le = self
		while not le is None:
			if type(le) is Lambda:
				if le.arg.name == arg.name:
					return re
			le = le.parent
			re += 1

		raise RuntimeError('Argument {} not found when traversing parents of: \n{}\n'.format(arg.name, le.print(0)))

	def encode_as_vector(self) -> list:
		''' Returns structural representation of this Leaf tree as vector of integers '''
		buf = []
		for leaf in self.leafs:
			t = type(leaf)
			if t is Argument:
				buf.append(self.get_argument_index(arg=leaf))
			elif t is Lambda:
				buf.append(-4)
				buf += leaf.encode_as_vector()
				buf.append(-5)
			elif t is Leaf:
				buf.append(-6)
				buf += leaf.encode_as_vector()
				buf.append(-7)
			elif t is Bind:
				buf.append(-8)
				buf.append(leaf.unique_id)
			else:
				raise RuntimeError('Unexpected type "{}"'.format(t))
		return buf

	def to_text(self) -> str:
		t = type(self)
		if t is Lambda:
			ret = LAMBDA_DECL + self.arg.name + ' ' + LAMBDA_SYMBOL + ' '
			leafs = list(map(lambda x: x.to_text(), self.leafs))
			ret += ' '.join(leafs)
			return '(' + ret + ')'
		if t is Argument:
			return self.name
		if t is Bind:
			return self.name
		if t is Leaf:
			leafs = list(map(lambda x: x.to_text(), self.leafs))
			ret = ' '.join(leafs)
			return '(' + ret + ')'
		else:
			raise RuntimeError("Unexpected leaf type: {}".format(t))

class Argument(Leaf):
	def __init__(self, name: str, parent: Leaf):
		super(Argument, self).__init__(leafs=[], parent=parent)
		self.name = name
	def __repr__(self):
		return self.print(0)
	def print(self, indent):
		return ('\t' * indent) + '[' + self.name + ']'

	def count_usages(self, target: Leaf) -> int:
		if type(target) is Argument:
			if target.name == self.name:
				return 1
			else:
				return 0
		elif type(target) is Lambda and target.arg.name == self.name:
			return 0
		else:
			ret = 0
			for leaf in target.leafs:
				ret += self.count_usages(leaf)
			return ret

class Lambda(Leaf):
	def __init__(self, scope: list, arg: Argument, leafs: list, parent: Leaf):
		super(Lambda, self).__init__(leafs=leafs, parent=parent)
		self.scope = scope
		self.arg = arg
	def print(self, indent: int):
		i_str = '\t' * indent
		l_str = ''
		for l in self.leafs:
			l_str += '\n' + l.print(indent + 1)
		return '{}(lambda {} of {}): {}'.format(i_str, self.scope, self.arg.name, l_str)

class Bind(Leaf):
	def __init__(self, name: str, target: Leaf):
		super(Bind, self).__init__([], parent=None)
		self.name = name
		self.target = target
		self.predefined = False
	def __repr__(self):
		return self.print(0)
	def print(self, indent):
		name = self.name if not self.name is None else 'expr' + str(self.unique_id)
		return ('\t' * indent) + '{' + name + '}'

def trimSpaces(s: str) -> str:
	re = ''
	last = ''
	for c in s:
		if c.isspace():
			if last == c:
				continue
			elif last == LAMBDA_DECL:
				last = c
				continue
			else:
				re += ' '
		else:
			re += c
		last = c
	return re
def transformMultipleLambdas(s: str) -> str:
	re = ''
	last_lambda = False
	buff = ''
	for i, c in enumerate(s):
		if last_lambda:
			buff += c
			if s.endswith(LAMBDA_SYMBOL, 0, i + 1):
				buff = buff[:-(len(LAMBDA_SYMBOL))].strip()
				buff = buff.replace(' ', ' {} {}'.format(LAMBDA_SYMBOL, LAMBDA_DECL)) + ' '
				re += buff + LAMBDA_SYMBOL

				buff = ''
				last_lambda = False
		else:
			if c == LAMBDA_DECL:
				last_lambda = True
			re += c
	return re

def parse_tokens(expr: str) -> Branch:
	expr = trimSpaces(expr)
	expr = transformMultipleLambdas(expr)
	return Branch.from_text(expr)
def parse_token(token: Branch, scope: list, binds: list) -> Leaf:
	if token.text.startswith('$'):
		name = token.text[1:]
		re = Bind(name, None)
		re.predefined = True
		return re
	for arg in reversed(scope):
		if arg.name == token.text:
			return arg
	for b in binds:
		if b.name == token.text:
			return b
	raise RuntimeError('not defined binding "{}" in scope = {} and bindings = {}'.format(token.text, scope, list(map(lambda b: b.name, binds))))

def add_scope_argument(current_scope: list, new_arg: Branch, parent: Leaf) -> list:
	return current_scope + [Argument(new_arg.text, parent=parent)]

def parse_leafs(b: Branch, scope: list, binds: list, parent: Leaf) -> list:
	lfs = []
	for t in b.branches:
		if t.is_token:
			if t.is_arg: continue
			lfs.append(parse_token(token=t, scope=scope, binds=binds))
		else:
			lfs.append(parse_structure(t, scope, binds, parent=parent))
	return lfs
def parse_structure(b: Branch, scope: list, binds: list, parent: Leaf) -> Leaf:
	if b.is_lambda:
		arg = b.branches[0]
		sc = add_scope_argument(scope, arg, parent=parent)
		arg = sc[-1]
		re = Lambda(arg=arg, scope=sc, leafs=None, parent=parent)
		lfs = parse_leafs(b=b, scope=sc, binds=binds, parent=re)
		re.leafs = lfs
		return re
	else: # is brackets
		re = Leaf(leafs=None, parent=parent)
		lfs = parse_leafs(b=b, scope=scope, binds=binds, parent=re)
		if len(lfs) == 1:
			return lfs[0]
		re.leafs = lfs
		return re
