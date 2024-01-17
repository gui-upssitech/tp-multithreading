# TP Multithreading

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/pre-commit/pre-commit/main.svg)](https://results.pre-commit.ci/latest/github/pre-commit/pre-commit/main)

Project about parrallelisation and coding practices such as :
- versionning
- packaging
- testing
- communication between multiple coding languages (`Python` and `C++` here)

## Usage

> **Tip** : Always stay inside the base directory

Run the base python example
```bash
bash tmux-boss-minion.sh
```

Run the extended example (with c++ minion)
```bash
cmake -B build -S .
cmake --build build
bash tmux-boss-minion-proxy.sh
```

Run tests for the task class
```bash
python3 -m tp_multithreading.tests.test_task
```

## C++ CMake commands
```bash
# configure
cmake -B build -S .
# compile
cmake --build build
# run
./build/low_level
```
