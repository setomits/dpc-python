# What is this

This is a Python library to parse DPC files.

# How to use

```
from dpc import EFFile

eff = EFFile('/path/to/EFn_987654321_2311.txt')
print(eff.file_name)
if eff.has_header:
    print('has header line')
print(f'There are {len(eff.lines)} lines.')
```

# For Developer

## Testing

```
$  python -m unittest discover -s tests
```
