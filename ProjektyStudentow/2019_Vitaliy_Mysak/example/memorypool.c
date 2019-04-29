
/* *** MEMORY POOL *** */

#include <stdlib.h>
#include <stdint.h>
#include <stdio.h>

#include "memorypool.h"

struct ALLOCPOOL {
	uint8_t *buf;
	int index;
	int size;
	struct ALLOCPOOL *next;
};

struct ALLOCPOOL * pool_cur = NULL;

/* FREEING THE POOL ALSO FREES THE BUFFER */
struct ALLOCPOOL * ALLOC_NEW_POOL(int size)
{
	uint8_t *mem = (uint8_t*)malloc(sizeof(struct ALLOCPOOL) + size);

#if TRACK_POOL_ALLOCS
	fprintf (stderr, "ALLOCATED NEW MEM: [%p] of size %d\n", mem, size);
#endif
	
	struct ALLOCPOOL * ret = (struct ALLOCPOOL*)mem;
	ret->buf = mem + sizeof(struct ALLOCPOOL);
	ret->index = 0;
	ret->size = size;
	ret->next = NULL;

	return ret;
}

#if TRACK_ALLOCS
void * ALLOC_GET(int size, const char * name)
{
	fprintf (stderr, "ALLOCATING [%s]\n", name);
#else
void * ALLOC_GET(int size)
{
#endif
	if (pool_cur->size > pool_cur->index + size) {
		uint8_t *ret = pool_cur->buf + pool_cur->index;
		pool_cur->index += size;
		return ret;
	} else {
		struct ALLOCPOOL * np = ALLOC_NEW_POOL(pool_cur->size);
		pool_cur->next = np;
		pool_cur = np;
#if TRACK_ALLOCS
		return ALLOC_GET(size, name);
#else
		return ALLOC_GET(size);
#endif
	}
}

/* SIZE HAS TO BE SMALLER THAN THE ALLOCPOOL->SIZE */

void ALLOC_INIT(void)
{
	pool_cur = ALLOC_NEW_POOL(20111000);
}
