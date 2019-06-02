
#include "list.h"
#include "memorypool.h"

#ifndef NULL
#define NULL (void*)0
#endif

struct list {
	int value;
	struct list * next;
};

struct list * list_alloc() {
	struct list * re = ALLOC_GET(sizeof(struct list));
	re->next = NULL;
	return re;
}

void list_add(struct list * l, int value) {
	struct list * new = ALLOC_GET(sizeof(struct list));

	new->value = l->value;
	new->next = l->next;
	l->value = value;
	l->next = new;
}

int list_compare_two(void * opaque_a, void * opaque_b) {
	struct list * a = opaque_a;
	struct list * b = opaque_b;

	while (a) {
		if (b == NULL) {
			return 0;
		}
		if (a->value != b->value) {
			return 0;
		}
		a = a->next;
		b = b->next;
	}
	if (b != NULL) {
		return 0;
	} else {
		return 1;
	}
}

long unsigned int list_to_int(void * opaque) {
	struct list * l = opaque;

	if (l->next == l) {
		return 0;
	}

	long unsigned int re = 0;
	while (l) {
		re = l->value + (re << 6) + (re << 16) - re;
		l = l->next;
	}

	return re;
}