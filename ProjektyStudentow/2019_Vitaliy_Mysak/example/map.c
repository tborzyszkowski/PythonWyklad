
#include "map.h"
#include "memorypool.h"

#ifndef NULL
#define NULL (void*)0
#endif

struct node {
	void * key;
	void * value;
	struct node * next;
};

static void node_add(struct node * last, void * key, void * value)
{
	last->next = ALLOC_GET(sizeof(struct node));
	last->next->key = key;
	last->next->value = value;
}

static void init_node(struct node * o) {
	o->next = NULL;
	o->key = NULL;
	o->value = NULL;
}

struct map {
	struct node * nodes;
	int size;
};

static int simple_hash(int n, long unsigned int k) {
	long int pos = 0, ret = -1;

	while (pos < n)
	{
		ret = pos;
		k = 1 + k * 2862933555777941757ULL;
		pos = ((double)(1LL << 31) / (double)((k >> 33) + 1)) * (ret + 1);
	}

	return ret % n;
}

struct map * map_alloc(const int size) {
	struct map * m = ALLOC_GET(sizeof(struct map));
	m->size = size;

	m->nodes = ALLOC_GET(sizeof(struct node) * m->size);
	for (int i = 0; i < m->size; i++) {
		init_node(m->nodes + i);
	}

	return m;
}

int map_add(struct map * m, void * key, void * value, map_hash_void_f_t h, map_cmp_f_t cmp) {
	long int hash = simple_hash(m->size, h(key));

	struct node * place = m->nodes + hash;

	if (place->key == NULL) {
		/* If this is the first key at index 'hash' */
		place->key = key;
		place->value = value;
		return 0;
	}

	while (place->next) {
		if (cmp(place->key, key)) {
			/* Same key already added */
			return 1;
		}
		place = place->next;
	}

	/* If not found, append to tail */
	node_add(place, key, value);

	return 0;
}

void * map_get(struct map * m, void * key, map_hash_void_f_t h, map_cmp_f_t cmp) {
	long int hash = simple_hash(m->size, h(key));

	struct node * place = m->nodes + hash;

	if (place->key == NULL) {
		return 0;
	}

	do {
		if (cmp(place->key, key)) {
			return place->value;
		}
		place = place->next;
	} while (place);

	return 0;
}
