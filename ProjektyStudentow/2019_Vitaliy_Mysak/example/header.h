#pragma once

#include "flags.h"

#include <assert.h>
#include <stdio.h>

typedef char bool;
#define true  1
#define false 0

#ifndef NULL
#define NULL ((void*)0)
#endif

struct fun;
typedef struct fun * ff;

#ifdef DO_CACHING

#include "map.h"
#include "list.h"

typedef struct list mapkey_t;
typedef struct map recursion_set;

void recset_add(recursion_set * set, ff me);
int  recset_check(recursion_set * set, ff me);

struct map * g_caching_map;

#endif

#ifdef COUNT_TOTAL_EXEC
extern int total_eval_count;
#ifdef DO_CACHING
extern int g_cache_hits_count;
#endif
#endif

struct fun {
	ff parent;
	ff x;

	ff (*eval_now)(ff, ff);

	void * custom; /* For custom expressions */
	int customsize; /* For copying */

#ifdef USE_TYPEID
	int typeuuid;
#endif
#ifdef DO_CACHING
	int (*cache)(ff me, mapkey_t * ret, recursion_set * set);
#endif
};

ff eval(ff me, ff x);

#include "fin.h"
#include "error.h"

#include "memorypool.h"
