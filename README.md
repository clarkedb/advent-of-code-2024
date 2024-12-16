# advent of code 2024

Advent of Code 2024 solutions in Python

## usage

### running solver

The main command takes three arguments:

- `--day`: day (1-25) to solve
- `--part`: part (1,2) to solve
- `--input`: puzzle input file path

```sh
python run src/app.py --day [1 to 25]--part [1 or 2] --input [path]
```

### set up new day

The init command takes one argument:

- `day`: the number of the day to initialize

```sh
make init_day day=<day>
```

## dependencies

This project uses `uv` to manage dependencies. Install `uv` if needed.

Day initializer requires `make`.
