# Python Notes — Tuples & Sequences

---

## 1. Recap: Data Structures

Data Structures allow us to **store and organize** data efficiently.

Python has 4 main data structures:
- **List**
- **Tuple**
- **Set**
- **Dictionary**

---

## 2. What is a Tuple?

- Holds an **ordered sequence of items**
- Items are indexed starting from **0**
- **Tuple is immutable** → once created, it cannot be modified
- Whereas a **List is mutable** → it can be modified

**Example:**

| Index | 0 | 1     | 2 | 3   |
|-------|---|-------|---|-----|
| Value | 5 | "Six" | 2 | 8.2 |

---

## 3. Creating a Tuple

- Elements are enclosed within **( ) round brackets**
- Each item is separated by a **comma**

```python
a = 2
tuple_a = (5, "Six", a, 8.2)
print(type(tuple_a))   # <class 'tuple'>
print(tuple_a)         # (5, 'Six', 2, 8.2)
```

### ⚠️ Special Cases

```python
a = ()      # empty tuple      → <class 'tuple'>
b = (5)     # NOT a tuple!     → <class 'int'>
c = (1, 2)  # tuple            → <class 'tuple'>
```

> **Note:** `(5)` is just an integer. To make a single-element tuple, add a **trailing comma**.

---

## 4. Tuple with a Single Item

To create a tuple with only one element, you must add a **trailing comma**:

```python
a = (1,)
print(type(a))   # <class 'tuple'>
print(a)         # (1,)
```

---

## 5. Accessing Tuple Elements

Use **index** (inside square brackets) to access elements:

```python
a = 2
tuple_a = (5, "Six", a, 8.2)
print(tuple_a[1])   # Six
```

- Indexing starts at **0**
- `tuple_a[0]` → `5`
- `tuple_a[1]` → `'Six'`
- `tuple_a[2]` → `2`
- `tuple_a[3]` → `8.2`

---

## 6. Tuples are Immutable

You **cannot modify** a tuple after creation. Trying to do so raises a `TypeError`:

```python
tuple_a = (1, 2, 3, 5)
tuple_a[3] = 4        # ❌ This will cause an error!
print(tuple_a)
```

**Output:**
```
TypeError: 'tuple' object does not support item assignment
```

---

## 7. Operations on Tuples

Given:
```python
a = 2
tuple_a = (5, "Six", a, 8.2)
```

Supported operations:
- `len()` — get number of elements
- **Iterating** — loop through elements
- **Slicing** — get a portion of the tuple
- **Extended Slicing** — slicing with step

---

## 8. Converting to Tuple — `tuple(sequence)`

`tuple(sequence)` takes any sequence and converts it into a tuple.

### From a String:
```python
color = "Red"
tuple_a = tuple(color)
print(tuple_a)   # ('R', 'e', 'd')
```

### From a Range:
```python
tuple_a = tuple(range(4))
print(tuple_a)   # (0, 1, 2, 3)
```

### From a List:
```python
list_a = [1, 2, 3]
tuple_a = tuple(list_a)
print(tuple_a)   # (1, 2, 3)
```

---

## 9. Membership Check (`in` / `not in`)

Used to check if a given element is part of a sequence or not.

**Operators:** `in`, `not in`

### With Tuple:
```python
tuple_a = (1, 2, 3, 4)

is_part = 5 in tuple_a
print(is_part)          # False

is_part = 1 not in tuple_a
print(is_part)          # False
```

### With List:
```python
list_a = [1, 2, 3, 4]
is_part = 1 in list_a
print(is_part)          # True
```

### With String:
```python
word = 'Python'
is_part = 'th' in word
print(is_part)          # True
```

> **Note:** `in` and `not in` work on **any sequence** — tuples, lists, and strings.

---

## 10. Unpacking

Values of any sequence can be **directly assigned to variables**.

> ⚠️ Number of variables on the left **must match** the length of the sequence.

### Tuple Unpacking:
```python
tuple_a = ('R', 'e', 'd')
(s_1, s_2, s_3) = tuple_a
print(s_1)   # R
print(s_2)   # e
print(s_3)   # d
```

### List Unpacking:
```python
list_a = ['R', 'e', 'd']
s_1, s_2, s_3 = list_a
print(s_1)   # R
```

### String Unpacking:
```python
str_1 = 'Red'
s_1, s_2, s_3 = str_1
print(s_2)   # e
```

### ❌ Mismatch Error:
```python
tuple_a = ('R', 'e', 'd')
s_1, s_2 = tuple_a        # ❌ Too many values!
```
**Output:**
```
ValueError: too many values to unpack (expected 2)
```

---

## 11. Tuple Packing

- `( )` brackets are **optional** while creating tuples
- Values separated by commas are **automatically packed** into a tuple

```python
a = 1, 2, 3
print(type(a))   # <class 'tuple'>
print(a)         # (1, 2, 3)
```

### ⚠️ Packing vs Unpacking (Single Value):

```python
a = 1,           # Packing  → tuple (1,)
print(type(a))   # <class 'tuple'>

a, = 1,          # Unpacking → int 1
print(type(a))   # <class 'int'>
```

### Combined Packing & Unpacking:
```python
a, b, c = 1, 2, "Hi"
print(a)   # 1
print(b)   # 2
print(c)   # Hi
```

---

## 12. Returning Multiple Values from a Function

Tuples are commonly used to **return multiple values** from a function:

```python
def get_sum_and_product(a, b):
    num_sum = a + b
    num_product = a * b
    return num_sum, num_product

x, y = get_sum_and_product(2, 3)
print(x)   # 5
print(y)   # 6
```

> Internally, `return num_sum, num_product` packs the values into a tuple, and `x, y = ...` unpacks them.

---

## 🔑 Key Takeaways

| Topic | Summary |
|---|---|
| **Tuple** | Ordered, immutable sequence of items |
| **Immutability** | Tuple elements cannot be changed after creation |
| **Membership Check** | Use `in` and `not in` to check element presence |
| **Packing** | Comma-separated values are packed into a tuple |
| **Unpacking** | Tuple values assigned directly to variables |
| **Multiple Return** | Functions can return multiple values using tuples |
