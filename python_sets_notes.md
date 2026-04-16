# Python Notes — Sets

---

## 1. Recap: Data Structures

Data Structures allow us to **store and organize** data efficiently.

Python has 4 main data structures — List, Tuple, **Set**, Dictionary.

Today's focus → **Set**

---

## 2. What is a Set?

A Set is an **unordered collection of items** where:
- Every element is **unique** (no duplicates allowed)
- Every element must be **immutable** (e.g. int, float, string, tuple — but NOT list)

> 💡 Think of it like a mathematical set — a bag where each item appears only once and the order doesn't matter.

```
Set visual:  { 5,  "Six",  2,  8.2 }   ← no index, no order
```

---

## 3. Creating a Set

- Use **{ } curly brackets**
- Separate each item with a **comma**

```python
a = 2
set_a = {5, "Six", a, 8.2}
print(type(set_a))   # <class 'set'>
print(set_a)         # {8.2, 2, 'Six', 5}  ← order may differ!
```

> ⚠️ Output order need not match the order you defined — sets are **unordered**.

---

## 4. No Duplicate Items

If you add duplicate values, the set automatically removes them:

```python
set_a = {"a", "b", "c", "a"}
print(set_a)   # {'b', 'a', 'c'}  ← only one 'a'
```

---

## 5. Immutable Items Only

Set elements **must be immutable**. Since a list is mutable, it **cannot** be a set element:

```python
set_a = {"a", ["c", "a"]}   # ❌ list inside set!
print(set_a)
```

**Output:**
```
TypeError: unhashable type: 'list'
```

✅ Valid set elements: `int`, `float`, `str`, `tuple`
❌ Invalid set elements: `list`, `dict`, `set`

---

## 6. Creating an Empty Set

> ⚠️ You **cannot** use `{}` for an empty set — that creates an empty **dictionary**!

Always use `set()` to create an empty set:

```python
set_a = set()
print(type(set_a))   # <class 'set'>
print(set_a)         # set()
```

---

## 7. Converting to Set — `set(sequence)`

`set(sequence)` takes any sequence and converts it into a set, automatically removing duplicates.

### From a List:
```python
set_a = set([1, 2, 1])
print(set_a)   # {1, 2}  ← duplicate 1 removed
```

### From a Tuple:
```python
set_a = set((1, 2, 1))
print(set_a)   # {1, 2}
```

### From a String:
```python
set_a = set("apple")
print(set_a)   # {'l', 'p', 'e', 'a'}  ← duplicate 'p' removed, unordered
```

---

## 8. Accessing Items — ❌ Not Possible with Index/Slice

Since sets are **unordered**, there is no concept of position/index. So you **cannot** use indexing or slicing:

```python
set_a = {1, 2, 3}
print(set_a[1])     # ❌ Error!
print(set_a[1:3])   # ❌ Error!
```

**Output:**
```
TypeError: 'set' object is not subscriptable
```

> ✅ However, sets **are mutable** — you can add and remove items (just not access by index).

---

## 9. Mutability of Sets — Adding Items

### `set.add(value)` — Add a Single Item

Adds the item **only if it is not already present**:

```python
set_a = {1, 3, 6, 2, 9}
set_a.add(7)         # 7 not present → added
print(set_a)         # {1, 2, 3, 6, 7, 9}

set_a.add(2)         # 2 already present → ignored
print(set_a)         # {1, 2, 3, 6, 9}  ← no change
```

---

### `set.update(sequence)` — Add Multiple Items

Adds all items from a sequence, ignoring duplicates:

```python
set_a = {1, 3, 9}
set_a.update([2, 3])   # 2 added, 3 already exists → ignored
print(set_a)           # {2, 1, 3, 9}
```

---

## 10. Mutability of Sets — Removing Items

### `set.discard(value)` — Safe Remove

Removes the item **if present**. If item is **not found**, it does **nothing** (no error):

```python
set_a = {1, 3, 9}
set_a.discard(3)    # 3 found → removed
print(set_a)        # {1, 9}

set_a.discard(5)    # 5 not found → no error, no change
print(set_a)        # {1, 9}
```

---

### `set.remove(value)` — Strict Remove

Removes the item if present. If item is **not found**, raises a **KeyError**:

```python
set_a = {1, 3, 9}
set_a.remove(5)   # ❌ 5 not in set → KeyError!
```

**Output:**
```
KeyError: 5
```

### 🔑 discard vs remove

| Method | Item Found | Item NOT Found |
|--------|-----------|----------------|
| `discard(value)` | Removes it ✅ | Does nothing ✅ |
| `remove(value)` | Removes it ✅ | Raises KeyError ❌ |

> 💡 Use `discard()` when you're not sure if the item exists. Use `remove()` when you want strict checking.

---

## 11. Operations on Sets

Given:
```python
a = 2
set_a = {5, "Six", a, 8.2}
```

Supported operations:

| Operation | Method/Syntax | Description |
|-----------|--------------|-------------|
| Clear | `set_a.clear()` | Removes all items from the set |
| Length | `len(set_a)` | Returns number of items |
| Iterating | `for item in set_a` | Loop through all items |
| Membership | `x in set_a` / `x not in set_a` | Check if item exists |

---

### Iterating Over a Set:

```python
set_a = {1, 3, 2, 6, 9, 10}
for item in set_a:
    print(item)
# Output: 1 2 3 6 9 10  (order may vary)
```

---

### Membership Check (`in` / `not in`):

```python
set_a = {1, 2, 6, 9, 10, 3}

is_part = 10 in set_a
print(is_part)          # True

is_part = 11 not in set_a
print(is_part)          # True  (11 is indeed NOT in set)
```

---

## 12. Sets vs Lists vs Tuples — Quick Comparison

| Feature | List | Tuple | Set |
|---------|------|-------|-----|
| Brackets | `[ ]` | `( )` | `{ }` |
| Ordered | ✅ Yes | ✅ Yes | ❌ No |
| Duplicates | ✅ Allowed | ✅ Allowed | ❌ Not allowed |
| Mutable | ✅ Yes | ❌ No | ✅ Yes (add/remove) |
| Indexing | ✅ Yes | ✅ Yes | ❌ No |
| Element type | Any | Immutable only (for hashing) | Immutable only |

---

## 🔑 Key Takeaways

| Topic | What to Remember |
|-------|-----------------|
| **Set** | Unordered, unique elements, mutable |
| **Creating** | Use `{ }` for non-empty, `set()` for empty |
| **Converting** | `set(sequence)` removes duplicates automatically |
| **No indexing** | Can't access items by position or slice |
| **add()** | Adds one item, ignores if already present |
| **update()** | Adds multiple items from a sequence |
| **discard()** | Removes safely — no error if item missing |
| **remove()** | Removes strictly — KeyError if item missing |
| **in / not in** | Membership check works on sets |
| **Iterating** | Use `for` loop to go through set items |
