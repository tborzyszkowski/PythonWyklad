
#pragma once

struct list;

/* Alloc empty list */
struct list * list_alloc(void);

void list_add(struct list * l, int value);

/* a == b -> return 1 */
int list_compare_two(void * list_a, void * list_b);

long unsigned int list_to_int(void * list);
