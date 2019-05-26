
#include "header.h"

#include "fin.h"

#include <stdio.h>

ff fin_eval_now(ff me, ff x) {
	// Init leafs
	fprintf(stderr, "%s", "fin should not be evaluated!\n");
	return me;
}

#ifdef DO_CACHING
int Cache_fin(ff me_abs, mapkey_t * ret, recursion_set * set) {
	return true;
}
#endif

struct fun Instance_fin = {
	.parent = 0,
	.x = 0,
	.eval_now = fin_eval_now,
	.customsize = 0,

#ifdef DO_CACHING
	.cache = Cache_fin,
#endif
};

ff fin = &Instance_fin;
