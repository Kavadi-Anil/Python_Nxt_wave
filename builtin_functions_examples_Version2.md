# Python Built-in Functions Examples

## Basic Built-in Function Usage

```python
print(min(1, 3, 4, 4))             # 1
print(min("python", "java"))       # java (alphabetically first)
print(max(1, 3, 4, 4))             # 4
print(max("python", "java"))       # python (alphabetically last)
print(sum([1, 3, 4, -4]))          # 4

x = [1, 3, 4, -4]
print(sorted(x))                   # [-4, 1, 3, 4]
print(sorted(x, reverse=False))    # [-4, 1, 3, 4]
print(sorted(x, reverse=True))     # [4, 3, 1, -4]
```

---

## Coding Problem: Get Numbers from a String

### Without a Function

```python
string = input()   # Example input: 8233434
list = []
for i in string:
    if i.isdigit():
        list = list + [int(i)]
    else:
        pass

print(list)
print(min(list))
print(max(list))
print(sum(list))
```

---

### Using a Function

```python
def fucntion(string):
    list = []
    for i in string:
        if i.isdigit():
            list = list + [int(i)]
        else:
            pass
    return list

string = input()         # Example input: 8233434
output = fucntion(string)
print(output)
print(min(output))
print(max(output))
print(sum(output))
```

---

## Output Example

Given input:  
```
8233434
```
The output will be:
```
[8, 2, 3, 3, 4, 3, 4]
2
8
27
```

---

## Notes

- `min()` and `max()` can be used with numbers or strings (lexicographical order for strings).
- `sum()` adds up all numbers in an iterable (like a list).
- `sorted()` returns a new sorted list, can be reversed.
- To extract numbers from a string, `str.isdigit()` is helpful.
- When using built-in functions on lists produced from string digit extraction, you can quickly find the smallest, largest, and the sum.