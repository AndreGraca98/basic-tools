# Basic Tools

![badge](https://img.shields.io/github/package-json/v/AndreGraca98/basic-tools?filename=basic_tools%2Fversion.json&label=basic-tools&logo=python&logoColor=yellow)

basic-tools is a library that contains a cluster of different useful tools

- [Basic Tools](#basic-tools)
  - [Package contents](#package-contents)
  - [Environment](#environment)
  - [Example](#example)
  - [TODO](#todo)

## Package contents

- assertions
- common
- decorators
- enums
- exceptions
- strings

## Environment

```bash
# Create env
env_name=basic-tools
conda create -n $env_name python=3.7 -y
conda activate $env_name

# Install package
pip install git+https://github.com/AndreGraca98/basic-tools.git

source ~/.profile
```

## Example

```python
from basic_tools.common import isfloat

print(isfloat("2.3")) # True
print(isfloat(2)) # True
print(isfloat(2.3)) # True
print(isfloat("2e3")) # True
print(isfloat("234")) # True
print(isfloat("2.3.4")) # False
print(isfloat("2.asd")) # False
print(isfloat([1, 2, 3])) # False
```

## TODO

1. [ ] finish test cases
1. [ ] finish function docs
