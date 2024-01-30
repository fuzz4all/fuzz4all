# SMT Solver

## Setup

### Z3

clone the most recent version of Z3

```shell
cd z3
python scripts/mk_make.py --debug  # compile with debug flag
cd build/
make
sudo make install # install to path
```

### CVC5

clone the most recent version of cvc5

```shell
cd cvc5
./configure.sh production --assertions --auto-download # use --assertion to enable debug assertions
cd build/
make
sudo make install # install to path
```