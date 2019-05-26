
#include <stdio.h>
#include <assert.h>

#include "list.c"
#include "map.c"
#include "memorypool.c"

void printlist(struct list * l) {
	printf("[ ");
	while (l) {
		printf("%d ", l->value);
		l = l->next;
	}
	printf("]\n");
}

int cmp(struct list * a, struct list * b, const char * mess) {
	int eq = list_compare_two(a, b);
	printf("%s equal %d \n", mess, eq);
	return eq;
}

void test_list() {
	{
		struct list * al = list_alloc();
		list_add(al, 5);

		struct list * bl = list_alloc();
		list_add(bl, 5);

		assert(cmp(al, bl, "1") == 1);
	}
	{
		struct list * al = list_alloc();
		list_add(al, 3);
		list_add(al, 5);

		struct list * bl = list_alloc();
		list_add(bl, 3);
		list_add(bl, 5);

		assert(cmp(al, bl, "1") == 1);
	}
	{
		struct list * al = list_alloc();
		list_add(al, 5);

		struct list * bl = list_alloc();
		list_add(bl, 5);
		list_add(bl, 5);

		assert(cmp(al, bl, "0") == 0);
	}
	{
		struct list * al = list_alloc();
		list_add(al, 5);
		list_add(al, 5);

		struct list * bl = list_alloc();
		list_add(bl, 5);

		assert(cmp(al, bl, "0") == 0);
	}
	{
		struct list * al = list_alloc();
		list_add(al, 2);

		struct list * bl = list_alloc();
		list_add(bl, 5);

		assert(cmp(al, bl, "0") == 0);
	}
	{
		struct list * al = list_alloc();
		list_add(al, 5);
		list_add(al, 2);

		struct list * bl = list_alloc();
		list_add(bl, 5);

		assert(cmp(al, bl, "0") == 0);
	}
}

int node_get_length(struct node * n) {
	if (n->key == NULL) {
		return 0;
	}

	int re = 0;

	do {
		n = n->next;
		re++;
	} while (n);

	return re;
}

double get_avg_map_nodes_size(struct map * m) {
	double re = 0;
	int count = 0;

	for (int i = 0; i < m->size; i++) {
		struct node * n = m->nodes + i;
		if (n->key) {
			int len = node_get_length(n);
			re = (re * count + len) / ((double)(count + 1));
			count++;
		}
	}

	return re;
}
double get_fill_ratio(struct map * m) {
	int count = 0;

	for (int i = 0; i < m->size; i++) {
		struct node * n = m->nodes + i;
		if (n->key) {
			count++;
		}
	}

	return count / ((double) m->size);
}
int get_max_map_nodes_size(struct map * m) {
	int re = 0;

	for (int i = 0; i < m->size; i++) {
		struct node * n = m->nodes + i;
		int len = node_get_length(n);
		if (len > re) { re = len; }
	}

	return re;
}
void ass_map(struct map * m, double ex_avg, double ex_fill)
{
	double avg  = get_avg_map_nodes_size(m);
	double fill = get_fill_ratio(m);
	int max = get_max_map_nodes_size(m);

	puts("");
	printf("avg  = %lf; ", avg);
	if (ex_avg >= 0) {
		printf("expected = %lf; ", ex_avg);
		assert(avg == ex_avg);
	}

	puts("");
	printf("fill = %lf; ", fill);
	if (ex_fill >= 0) {
		printf("expected = %lf; ", ex_fill);
		assert(fill == ex_fill);
	}

	puts("");
	printf("max = %d; ", max);

	puts("");
}

int map_add_list(struct map * m, struct list * key, void * value) {
	return map_add(m, key, value, list_to_int, list_compare_two);
}
void * map_get_list(struct map * m, struct list * key) {
	return map_get(m, key, list_to_int, list_compare_two);
}

void test_map() {
	{
		struct map * m = map_alloc(9);

		struct fun * val = (void*)5;
		
		struct list * al = list_alloc();
		list_add(al, 3);
		list_add(al, 5);

		map_add_list(m, al, val);

		ass_map(m, -1, -1);

		map_add_list(m, al, val);
		map_add_list(m, al, val);
		map_add_list(m, al, val);

		ass_map(m, -1, -1);

		struct list * bl = list_alloc();
		list_add(bl, 3);
		list_add(bl, 5);

		map_add_list(m, bl, val);
		map_add_list(m, bl, val);
		map_add_list(m, bl, val);

		ass_map(m, -1, -1);

		printf("get bl = %p \n", map_get_list(m, bl));

		struct fun * val2 = (void*)7;

		struct list * cl = list_alloc();
		list_add(cl, 3);
		list_add(cl, 5);
		list_add(cl, 2);

		map_add_list(m, cl, val2);
		map_add_list(m, cl, val2);
		map_add_list(m, cl, val2);

		ass_map(m, -1, -1);

		printf("get cl = %p \n", map_get_list(m, cl));

		for (int i = 0; i < 9999; i++) {
			struct list * tmp = list_alloc();
			list_add(tmp, 5);
			list_add(tmp, -i);
			list_add(tmp, 7);
			list_add(tmp, i);

			struct fun * val = (void*)(long int)i;
			map_add_list(m, tmp, val);
		}

		printf("get cl = %p \n", map_get_list(m, cl));
		ass_map(m, -1, -1);
	}
}

int main() {
	ALLOC_INIT();

	test_list();
	test_map();

	puts("OK");
	return 0;
}
