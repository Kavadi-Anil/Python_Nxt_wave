# Python Notes — Set Operations

---

## 0. Daily Challenge — Identify The Mistake

```python
# Code 1 - Using a set inside update()
set_a = {"pencil"}
set_a.update({"pen"})   # ✅ Works — {"pen"} is a set (iterable)
print(set_a)            # {'pen', 'pencil'}

# Code 2 - Using a list inside update()
set_a = {"pencil"}
set_a.update(["pen"])   # ✅ Also works — ["pen"] is a list (iterable)
print(set_a)            # {'pen', 'pencil'}
```

> 💡 Both work! `update()` accepts any iterable — set, list, tuple, or string.
> ⚠️ Output order can be in **any order** since sets are unordered.

---

## 1. Agenda — Set Operations

Two main topics today:

**Part 1 — Set Operations:**
- Union
- Intersection
- Difference
- Symmetric Difference

**Part 2 — Set Comparisons:**
- Subset
- Superset
- Isdisjoint

---

## 2. Overview of Set Operations

| Operation | Symbol | Method |
|-----------|--------|--------|
| Union | `\|` | `.union()` |
| Intersection | `&` | `.intersection()` |
| Difference | `-` | `.difference()` |
| Symmetric Difference | `^` | `.symmetric_difference()` |

---

## 3. Union

> Returns a set containing **all elements** from both sets (no duplicates)

```
  set_a          set_b
(  4, 8  ( 2 )   1  )
 \________↑__________/
  ALL elements selected
  {4, 8, 2, 1}
```

| set_a | set_b | Union Result |
|-------|-------|-------------|
| {4, 2, 8} | {1, 2} | {1, 2, 4, 8} |

**Syntax:**
```python
set_a | set_b
# or
set_a.union(sequence)   # union() can take any sequence (list, tuple etc.)
```

**Code Example — using `|` operator:**
```python
set_a = {4, 2, 8}
set_b = {1, 2}
union = set_a | set_b
print(union)   # {1, 2, 4, 8}
```

**Code Example — using `.union()` with a list:**
```python
set_a = {4, 2, 8}
list_a = [1, 2]
union = set_a.union(list_a)
print(union)   # {1, 2, 4, 8}
```

> 💡 `.union()` automatically converts the sequence to a set and performs the union.

---

## 4. Intersection

> Returns a set containing only the **common elements** of both sets

```
  set_a          set_b
(  4, 8  ( 2 )   1  )
          ↑
    only common part selected
    {2}
```

| set_a | set_b | Intersection Result |
|-------|-------|-------------------|
| {4, 2, 8} | {1, 2} | {2} |

**Syntax:**
```python
set_a & set_b
# or
set_a.intersection(sequence)
```

**Code Example — using `&` operator:**
```python
set_a = {4, 2, 8}
set_b = {1, 2}
intersection = set_a & set_b
print(intersection)   # {2}
```

**Code Example — using `.intersection()` with a list:**
```python
set_a = {4, 2, 8}
list_a = [1, 2]
intersection = set_a.intersection(list_a)
print(intersection)   # {2}
```

> 💡 `.intersection()` also converts sequence to a set automatically.

---

## 5. Difference

> Returns a set containing elements that are in the **first set but NOT in the second**

```
  set_a          set_b
(  4, 8  ( 2 )   1  )
  ↑↑↑
  only left side selected (excluding common)
  {4, 8}
```

| set_a | set_b | Difference (set_a - set_b) |
|-------|-------|--------------------------|
| {4, 2, 8} | {1, 2} | {4, 8} |

> ⚠️ Order matters! `set_a - set_b` ≠ `set_b - set_a`

**Syntax:**
```python
set_a - set_b
# or
set_a.difference(sequence)
```

**Code Example — using `-` operator:**
```python
set_a = {4, 2, 8}
set_b = {1, 2}
diff = set_a - set_b
print(diff)   # {8, 4}
```

**Code Example — using `.difference()` with a tuple:**
```python
set_a = {4, 2, 8}
tuple_a = (1, 2)
diff = set_a.difference(tuple_a)
print(diff)   # {8, 4}
```

---

## 6. Symmetric Difference

> Returns a set containing elements that are **NOT common** to both sets (opposite of intersection)

```
  set_a          set_b
(  4, 8  ( 2 )   1  )
  ↑↑↑             ↑
  both outer sides selected (excluding common)
  {4, 8, 1}
```

| set_a | set_b | Symmetric Difference |
|-------|-------|---------------------|
| {4, 2, 8} | {1, 2} | {8, 1, 4} |

> 💡 Think of it as: **Union MINUS Intersection** = everything except the common part

**Syntax:**
```python
set_a ^ set_b
# or
set_a.symmetric_difference(sequence)
```

**Code Example:**
```python
set_a = {4, 2, 8}
set_b = {1, 2}
symmetric_diff = set_a ^ set_b
print(symmetric_diff)   # {8, 1, 4}
```

---

## 7. All 4 Operations — Side by Side Summary

Using `set_a = {4, 2, 8}` and `set_b = {1, 2}`:

```
  set_a          set_b
( 4, 8   ( 2 )   1  )

Union     |  → ( 4, 8  [2]  1 )  = {1, 2, 4, 8}   ALL
Intersect &  → (     [2]    )    = {2}              COMMON ONLY
Diff      -  → ( 4, 8       )    = {4, 8}           set_a ONLY
Sym Diff  ^  → ( 4, 8       1 )  = {8, 1, 4}        NON-COMMON ONLY
```

| Operation | Operator | Result |
|-----------|----------|--------|
| Union | `\|` | `{1, 2, 4, 8}` |
| Intersection | `&` | `{2}` |
| Difference | `-` | `{4, 8}` |
| Symmetric Difference | `^` | `{8, 1, 4}` |

---

## 8. Set Comparisons

Set comparisons are used to **validate whether one set fully exists within another**.

Three methods:
- `issubset()`
- `issuperset()`
- `isdisjoint()`

---

### `issubset()` — Is one set inside another?

```
  set_1 = {1, 2, 4}
  ┌─────────────────┐
  │   4             │
  │  ┌──────────┐   │
  │  │  2   1   │   │  ← set_2 = {1, 2} is fully inside set_1
  │  └──────────┘   │
  └─────────────────┘
```

`set_2.issubset(set_1)` → Returns **True** if ALL elements of `set_2` are present in `set_1`

| set_1 | set_2 | set_2.issubset(set_1) |
|-------|-------|----------------------|
| {1, 2, 4} | {1, 2} | True ✅ |
| {1, 2, 4} | {1, 5} | False ❌ |

---

## 🔑 Key Takeaways

| Topic | Summary |
|-------|---------|
| **Union** `\|` | All elements from both sets |
| **Intersection** `&` | Only common elements |
| **Difference** `-` | Elements in first set, not in second |
| **Symmetric Difference** `^` | All non-common elements (opposite of intersection) |
| **issubset()** | Checks if one set is fully inside another |
| **issuperset()** | Checks if one set fully contains another |
| **isdisjoint()** | Checks if two sets have NO common elements |
| **Method versions** | All operators have a method version that accepts any sequence |
