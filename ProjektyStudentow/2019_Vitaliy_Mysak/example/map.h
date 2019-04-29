
#pragma once

struct map;

struct map * map_alloc(const int size);

typedef int (*map_cmp_f_t)(void*, void*);
typedef long unsigned int (*map_hash_void_f_t)(void*);

int map_add(struct map * m, void * key, void * value, map_hash_void_f_t h, map_cmp_f_t cmp);
void * map_get(struct map * m, void * key, map_hash_void_f_t h, map_cmp_f_t cmp);
