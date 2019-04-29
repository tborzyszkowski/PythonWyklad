
#if TRACK_ALLOCS
void * ALLOC_GET(int size, const char * name);
#else
void * ALLOC_GET(int size);
#endif

#define QUOTE(x) #x

#if TRACK_ALLOCS
#define ALLOC(x) ((x*)ALLOC_GET(sizeof(x), QUOTE(x)))
#else
#define ALLOC(x) ((x*)ALLOC_GET(sizeof(x)))
#endif

void ALLOC_INIT(void);

