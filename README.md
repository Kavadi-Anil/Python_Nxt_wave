# Key Concepts

## Mutable Objects
- Lists in Python are mutable, meaning they can be changed in place.

## Assignment vs. In-place Modification
- `a = a + 1` (or `list_z = list_z + [1]`) creates a new object and assigns it to the variable.
- `a += 1` (or `list_z += [1]`) modifies the existing object in place if possible (for mutable types like lists).

---

## Example 1: `list_z = list_z + [1]`

```python
def increment(list_z):
    list_z = list_z + [1] 
    print(list_z)          # prints [1, 2, 1]

list_z = [1, 2]
increment(list_z)
print(list_z)              # prints [1, 2]
```

**What happens here?**
- Inside the function: `list_z + [1]` creates a new list `[1, 2, 1]`, and assigns it to the local variable `list_z`.
- This does **not change** the original list outside the function.
- So, inside the function: `[1, 2, 1]` is printed.
- Outside, `list_z` is still `[1, 2]`.

---

## Example 2: `list_z += [1]`

```python
def increment(list_z):
    list_z += [1] 
    print(list_z)          # prints [1, 2, 1]

list_z = [1, 2]
increment(list_z)
print(list_z)              # prints [1, 2, 1]
```

**What happens here?**
- Inside the function: `list_z += [1]` modifies the original `list_z` list **in place** (because lists are mutable).
- So, both inside and outside the function, `list_z` becomes `[1, 2, 1]`.

---

## Summary Table

| Operation                | Changes original list? | Output inside function | Output outside function |
|--------------------------|:---------------------:|:----------------------:|:-----------------------:|
| list_z = list_z + [1]    |         No            |     [1, 2, 1]          |        [1, 2]           |
| list_z += [1]            |        Yes            |     [1, 2, 1]          |      [1, 2, 1]          |

---

## Why is this important?
- `+=` (for lists) modifies the list you pass in (mutates it).
- `=` creates a new object and binds the variable to it (does not mutate the original).

> If you want the function to change the original list, use `+=`.  
> If you want the original list to stay unchanged, use `=` with `+`.
