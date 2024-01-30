# C Compiler

## Setup

### GCC

clone the most recent version of gcc

```shell
mkdir gcc-build
cd gcc-build
./../gcc-source/configure --prefix=$HOME/GCC-Temp --enable-languages=c,c++
make
make install
```

you may want to build with coverage option (`--enable-coverage`)

### Clang

clone the most recent version of LLVM

build with debug option (note you might have to download a newer cmake binary)

```shell
cd llvm-project
mkdir build
cd build
cmake -DLLVM_ENABLE_PROJECTS=clang -DCMAKE_BUILD_TYPE=Debug -G "Unix Makefiles" ../llvm
make
```
