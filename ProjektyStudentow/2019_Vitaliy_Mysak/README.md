This is a lambda-calculus to C compiler  

# Usage

1) Write lambda expressions to example/script.ini
2) `$ make`

or just  
1) `$ ./repl.py`

# Features

- Based on true lazy untyped lambda-calculus
- Easily extensible
- Allows to define expression bindings
- Optional caching (memoization) of evaluations (most of the time allow for exponential speed up)
- Easy to hack into generated translation as it preserves the names and has simple structure
- Easy to define efectful bindings by using special syntax (example at example/custom.cfg.py)
- No predefined symbols
- Optional expanding of bindigs a.k.a inlining (use `--make-inline`)
- Call stack trace is available at will

# TODO
This project is under active development

- [x] lazy evaluation
- [x] fix unique lambda members (each member should have its own argument x)
- [x] fix Y combinator case
- [x] inline bindings: do not introduce overhead from bindings
- [x] allow order-independent bindings
	- [x] fix infinite recursion for inliner
- [ ] cache evalutations [hard]
	- [x] use simple hash map and store whole environment as cache key
	- [x] determine which lambda abstractions are actually used in evaluation (will get more cache hits)
	- [x] fix (or find reason for) cache drop when using inlining - expected to have more hits than without inlining
	- [x] make base class (fun) more consistant
	- [x] add command line argument for caching
	- [x] use more efficient map than `std::map` and better keys than `std::vector<int>`
	- [x] use definitional irrelevance for smarter equality [hard]
	- [ ] never duplicate work (using Levy's definition) [hard]
	- [ ] compress Leaf.encode_as_vector to just one integer using hashmap of previus Leaf vectors
- [ ] efectful expression
	- [x] create translator that is going to use configs as definitions for efectful expressions (customwriter)
	- [x] make possible to create custom expressions with more than 1 argument (ex. add, multiply)
	- [x] create list
	- [ ] create hashmap (will work only if cache enabled?)
	- [ ] create some advanced IO (maybe sound or windowing)
- [ ] pass 'parent' as argument to exec
	- [ ] do ALLOC("X") and Init_Bind_"X" in its parent Init instead of its parent Exec
- [ ] representation: find a good way to print numbers, strings
- [x] make more names legal
- [ ] stackoverflow: use queue instead
- [ ] add garbage collector [hard]
- [ ] use multithreading [hard]
- [x] maybe use C instead of C++ (faster compile-time, maybe better optimisations)
- [ ] maybe use llvm instead (faster compile-time) [hard]
- [ ] improve code quality (*.py -> *.hs)
- [ ] incremental compilation
- [x] repl
	- [ ] use incremental compilation
	- [ ] allow to use arrow keys
- [ ] improve dynamic typing
- [ ] introduce static typing [hard]
- [x] fix bindings case:
	- reproduces with `--no-do-caching` only
	- doesnt work: `sum = \l -> fold + l 0`
	- does   work: `sum = \l -> fold (\acc cur -> + acc cur) l 0`
	- also  works: `sum = \l -> fold $add l $mint`
- [ ] add string literals
	- [ ] add parser for machine integers like `parsemint "3"` -> `$msuc ($msuc ($msuc $mint))`
- [ ] get better types info than just index
	- [ ] by default print lambdas as tree using type names
