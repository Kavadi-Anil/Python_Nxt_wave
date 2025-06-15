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








 # Assignment vs In-place Modification with Lists in Python

## Example Code

```python
def add_list(number):
    number = number + [13, 9]

list = [5, 8]
add_list(list)
print(list)      # Output: [5, 8]
```

---

## Explanation

- In this code, inside the function, `number = number + [13, 9]` **creates a new list** and assigns it to the local variable `number`.
- The original list (`list`) **outside the function is not changed**.
- The function does **not** return anything or modify the original list in place.

### Key Point

- **Assignment like `number = number + [13, 9]` makes a new object**.
- The variable `number` inside the function now points to the new list, but this does **not affect** the `list` variable outside the function.

---

## Visual Illustration

| Step            | `number` (inside function) | `list` (outside function) | Same Object?   |
|-----------------|---------------------------|---------------------------|---------------|
| Before function | [5, 8]                    | [5, 8]                    | Yes           |
| After `number = number + [13, 9]` | [5, 8, 13, 9]           | [5, 8]                    | No            |

---

## Summary

- If you want to modify the original list, use an in-place method (like `number += [13, 9]` or `number.extend([13, 9])`).
- If you use assignment (`number = ...`), it only changes the local reference, **not the original variable**.

```python
def add_list(number):
    number += [13, 9]   # or number.extend([13, 9])
```
This version **will** modify the original list.

# List Mutation vs Assignment in Python Function Arguments

## Example 1: In-place Modification (`+=`)

```python
def add_lists(numbers):
    numbers += [13, 9]

list_1 = [5, 8]
add_lists(list_1)
print(list_1)  # Output: [5, 8, 13, 9]
```

**Explanation:**  
- `numbers += [13, 9]` modifies the list **in place**.
- `numbers` is a reference to `list_1`, so the original list is changed.

---

## Example 2: Assignment (`=`)

```python
def add_lists(numbers):
    numbers = numbers + [13, 9]

list_1 = [5, 8]
add_lists(list_1)
print(list_1)  # Output: [5, 8]
```

**Explanation:**  
- `numbers = numbers + [13, 9]` creates a **new list** and assigns it to the local variable `numbers`.
- This does **not modify** `list_1` outside the function.

---

## Key Difference

| Operation             | Modifies Original List? | Notes                                                       |
|-----------------------|:----------------------:|-------------------------------------------------------------|
| `numbers += [13, 9]`  | Yes                   | In-place change; both names (`numbers` and `list_1`) see it |
| `numbers = numbers + [13, 9]` | No            | Creates new list for `numbers`; `list_1` is unchanged      |

---

## Visual Illustration

- **In-Place (`+=`)**:  
  Both `numbers` (inside) and `list_1` (outside) point to the same object, so the change is visible everywhere.
- **Assignment (`=`)**:  
  `numbers` points to a new list inside the function, so `list_1` is unaffected.

---
