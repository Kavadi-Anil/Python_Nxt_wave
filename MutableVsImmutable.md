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




# Understanding Mutable Default Arguments in Python

## Code Example

```python
def add_item(list_x=[]):
    list_x += [3]  
    print(list_x)

add_item()           # 1
add_item([2,5])      # 2
add_item([2,5])      # 3
add_item()           # 4
add_item()           # 5
add_item()           # 6
add_item([4,5])      # 7
add_item()           # 8
add_item([2,5])      # 9
add_item([2,5])      # 10
```

### Output

```
[3]
[2, 5, 3]
[2, 5, 3]
[3, 3]
[3, 3, 3]
[3, 3, 3, 3]
[4, 5, 3]
[3, 3, 3, 3, 3]
[2, 5, 3]
[2, 5, 3]
```

---

## What is Happening?

### The Key Point

- The function `add_item` uses a **mutable default argument** (`list_x=[]`).
- In Python, default argument values are evaluated **only once**, at function definition time.
- This means if you use the function without passing a new list, it keeps using (and modifying) the **same list** every time.

### Step-by-Step Explanation

1. **First call:** `add_item()`
   - Uses the default list (`[]`)
   - Adds `3` → `[3]`
2. **Second call:** `add_item([2,5])`
   - Uses a **new list** `[2,5]`
   - Adds `3` → `[2, 5, 3]`
3. **Third call:** `add_item([2,5])`
   - Uses a **new list** `[2,5]`
   - Adds `3` → `[2, 5, 3]`
4. **Fourth call:** `add_item()`
   - Uses the **same default list** from step 1, now `[3]`
   - Adds `3` → `[3, 3]`
5. **Fifth call:** `add_item()`
   - Default list is `[3, 3]`
   - Adds `3` → `[3, 3, 3]`
6. **Sixth call:** `add_item()`
   - Default list is `[3, 3, 3]`
   - Adds `3` → `[3, 3, 3, 3]`
7. **Seventh call:** `add_item([4,5])`
   - Uses a **new list** `[4,5]`
   - Adds `3` → `[4, 5, 3]`
8. **Eighth call:** `add_item()`
   - Default list is `[3, 3, 3, 3]`
   - Adds `3` → `[3, 3, 3, 3, 3]`
9. **Ninth & Tenth calls:** `add_item([2,5])`
   - Each uses a **new list** `[2,5]`
   - Adds `3` → `[2, 5, 3]` (each time)

--- 




# Understanding Mutable Default Arguments and Object IDs in Python

## Code Example with Object IDs

```python
def add_item(list_x=[]):
    list_x += [3]
    print(list_x, id(list_x))

add_item()           # 1
add_item([2,5])      # 2
add_item([2,5])      # 3
add_item()           # 4
add_item()           # 5
add_item()           # 6
add_item([4,5])      # 7
add_item()           # 8
add_item([2,5])      # 9
add_item([2,5])      # 10
```

### Output

```
[3] 140715559318528
[2, 5, 3] 140715557520576
[2, 5, 3] 140715557520576
[3, 3] 140715559318528
[3, 3, 3] 140715559318528
[3, 3, 3, 3] 140715559318528
[4, 5, 3] 140715557520576
[3, 3, 3, 3, 3] 140715559318528
[2, 5, 3] 140715557520576
[2, 5, 3] 140715557520576
```

## Why Does This Matter?

- **Mutable default arguments** can lead to unexpected behavior, as the same object is shared across function calls.
- To avoid this, use `None` as a default and create a new list inside the function:

```python
def add_item(list_x=None):
    if list_x is None:
        list_x = []
    list_x += [3]
    print(list_x)
```

- Now, every call with no argument gets a fresh list!

--- 




# Understanding Mutable Arguments and References in Python

## Example Code

```python
def add_list(number):
    number += [13, 9]

list = [5, 8]
add_list(list)
print(list)      # Output: [5, 8, 13, 9]
```

---

## Explanation

- When you call `add_list(list)`, the parameter `number` inside the function refers to the **same list object** as `list` outside the function.
- The operation `number += [13, 9]` modifies the original list **in place** (it is equivalent to `number.extend([13, 9])`).
- Therefore, after the function call, `list` is updated to `[5, 8, 13, 9]`.

---

## Key Point

> Both `number` (inside the function) and `list` (outside) **point to the same memory address**. Any in-place modification to `number` also affects `list`.

---

## Visual Illustration

| Step            | `number` (inside function) | `list` (outside function) | Memory Address (id)   |
|-----------------|---------------------------|---------------------------|-----------------------|
| Before function | [5, 8]                    | [5, 8]                    | Same                  |
| After `+= [13,9]` | [5, 8, 13, 9]           | [5, 8, 13, 9]             | Same                  |

---

## General Rule

- **Mutable objects** (like lists, dicts, etc.) passed to functions can be changed inside the function, and these changes will be visible outside the function.
- **Immutable objects** (like integers, strings, tuples) do not exhibit this behavior.

---

## If you want to avoid modifying the original list

You can pass a copy instead:

```python
def add_list(number):
    number += [13, 9]

list = [5, 8]
add_list(list[:])   # Passes a copy
print(list)         # Output: [5, 8]
```
