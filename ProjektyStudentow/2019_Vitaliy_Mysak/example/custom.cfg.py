
class print_true:
	def exec(x):
		'''
		puts("true");
		return lambda_error("Evaluated print_true");
		'''

class print_false:
	def exec(x):
		'''
		puts("false");
		return lambda_error("Evaluated print_false");
		'''

class ec:

	counter = ('int', '0')

	def exec(arg):
		'''
		if (arg == fin) {
			printf("Counter(%d)\\n", custom->counter);
		}
		custom->counter++;
		return me_abs;
		'''

	def cache():
		return ['me->counter']

class booly:

	value = ('bool', 'false')

	def exec(x):
		'''
		return me_abs;
		'''

	def cache():
		return ['me->value']

class bnot:

	def exec(x: booly) -> booly:
		'''
		rc->value = ! x->value;
		return ret;
		'''
	def cache():
		return []

class pbooly:
	def exec(x: booly):
		'''
		if (x->value) {
			puts("true");
		} else {
			puts("false");
		}
		return x_base;
		'''

class mif:
	def exec(x: booly, a, b):
		'''
		if (x->value) {
			return a;
		} else {
			return b;
		}
		'''
	def cache():
		return []

class mint:
	''' Machine integer '''

	value = ('int', '0')

	def exec(x):
		'''
		return me_abs;
		'''

	def cache():
		return ['me->value']

class pmint:
	''' Print machine integer '''
	def exec(x: mint):
		'''
		printf("%d\\n", x->value);
		return x_base;
		'''

class msuc:
	''' Increment machine integer '''
	def exec(x: mint) -> mint:
		'''
		rc->value = x->value + 1;
		return ret;
		'''
	def cache():
		return []

class mdec:
	''' Decrement machine integer '''
	def exec(x: mint) -> mint:
		'''
		rc->value = x->value - 1;
		return ret;
		'''
	def cache():
		return []

class mis0:
	''' Tells if machine integer is 0 '''
	def exec(x: mint) -> booly:
		'''
		if (x->value == 0) {
			rc->value = true;
		} else {
			rc->value = false;
		}
		return ret;
		'''
	def cache():
		return []

class meq:
	''' Tells if two machine integers are equal '''
	def exec(a: mint, b: mint) -> booly:
		'''
		if (a->value == b->value) {
			rc->value = true;
		} else {
			rc->value = false;
		}
		return ret;
		'''
	def cache():
		return []

class facc:
	'''
	fast factorial
	'''

	def exec(arg: mint) -> mint:
		'''
		rc->value = 1;
		for (int i = 2; i <= arg->value; i++) {
			rc->value *= i;
		}
		return ret;
		'''

	def cache():
		return []


class add:
	def exec(a: mint, b: mint) -> mint:
		'''
		rc->value = a->value + b->value;
		return ret;
		'''

	def cache() -> list:
		return []

class mult:
	def exec(a: mint, b: mint) -> mint:
		'''
		rc->value = a->value * b->value;
		return ret;
		'''

	def cache() -> list:
		return []

class pow:
	''' Positive power '''
	def exec(a: mint, b: mint) -> mint:
		'''
		rc->value = 1;
		for (int i = 0; i < b->value; i++) {
			rc->value *= a->value;
		}
		return ret;
		'''

	def cache() -> list:
		return []

class mlist:
	''' Empty list '''

	# listt = ('list *', 'new list')
	value = ('ff', 'NULL')
	next  = ('ff', 'NULL')

	def exec(x):
		'''
		return me_abs;
		'''

	def cache():
		'''
		list_add(ret, -12);
		if (me->value != NULL) {
			if (me->value->cache(me->value, ret, set)) {
					return true;
			}
		}
		if (me->next != NULL) {
			if (me->next->cache(me->next, ret, set)) {
					return true;
			}
		}
		list_add(ret, -13);
		'''
		return []

class cons:
	''' Append to head of the list '''

	def exec(val, l) -> mlist:
		'''
		rc->value = val;
		rc->next = l;
		return ret;
		'''

	def cache():
		return []

class head:
	''' Get head of the list '''

	def exec(l: mlist):
		'''
		if (l->value == NULL) {
			return lambda_error("Head got empty list");
		} else {
			return l->value;
		}
		'''

	def cache():
		return []

class tail:
	''' Get the rest of the list '''

	def exec(l: mlist) -> mlist:
		'''
		if (l->next == NULL) {
			return lambda_error("Tail got empty list");
		} else {
			return l->next;
		}
		'''

	def cache():
		return []

class mnil:
	''' Checks if list is nil '''

	def exec(l: mlist) -> booly:
		'''
		rc->value = l->value == NULL;
		return ret;
		'''

class dolist:
	''' Evaluates given expression for every element of list
	    Returns last evaluated element '''

	def exec(f, l: mlist):
		'''
		ff evaled = NULL;

		do {
			if (l->value == NULL) {
				if (evaled) {
					return evaled;
				} else {
					return lambda_error("dolist got []");
				}
			}
			eval(f, l->value);

			ff next = l->next;
			if (next == NULL) {
				break;
			}

			evaled = eval(next, fin);
			if (evaled == NULL) {
				return lambda_error("NULL during dolist");
			}

			l = evaled->custom;
			if (l == NULL) {
				return lambda_error("dolist got NULL for next list");
			}
		} while (1);

		return evaled;
		'''
