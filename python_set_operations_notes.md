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

## 9. issubset()
 
> Checks if one set is **completely inside** another set
 
```
  Nested circles — set_2 fully inside set_1:
 
  ┌─────────────────┐
  │   set_1         │
  │  3    5         │
  │    ┌───────┐    │
  │    │ set_2 │    │
  │    │ 'a' 1 │    │
  │    └───────┘    │
  └─────────────────┘
  set_2 is SUBSET of set_1 → True ✅
 
  Circles overlapping but NOT fully inside:
  set_1 = {4, 6}   set_2 = {2, 6}
  set_2 has element 2 which is NOT in set_1 → False ❌
```
 
**Syntax:** `set_2.issubset(set_1)`
 
**Example — True case:**
```python
set_1 = {'a', 1, 3, 5}
set_2 = {'a', 1}
is_subset = set_2.issubset(set_1)
print(is_subset)    # True  ✅ (all of set_2 is inside set_1)
```
 
**Example — False case:**
```python
set_1 = {4, 6}
set_2 = {2, 6}
is_subset = set_2.issubset(set_1)
print(is_subset)    # False ❌ (2 is in set_2 but NOT in set_1)
```
 
---
 
## 10. issuperset()
 
> Checks if one set **fully contains** another set — the opposite of issubset
 
```
  set_1 is the BIG circle, set_2 is the SMALL circle inside:
 
  ┌─────────────────┐
  │   set_1         │
  │  3    5         │
  │    ┌───────┐    │
  │    │ set_2 │    │
  │    │ 'a' 1 │    │
  │    └───────┘    │
  └─────────────────┘
  set_1 is SUPERSET of set_2 → True ✅
```
 
> 💡 **Subset vs Superset — same relationship, different perspective:**
> - `set_2.issubset(set_1)` → asking from set_2's view: "Am I inside set_1?"
> - `set_1.issuperset(set_2)` → asking from set_1's view: "Do I contain set_2?"
> Both give the same answer!
 
**Syntax:** `set_1.issuperset(set_2)`
 
**Example — True case:**
```python
set_1 = {'a', 1, 3, 5}
set_2 = {'a', 1}
is_superset = set_1.issuperset(set_2)
print(is_superset)   # True  ✅ (set_1 fully contains set_2)
```
 
**Example — False case:**
```python
set_1 = {4, 6}
set_2 = {2, 6}
is_superset = set_1.issuperset(set_2)
print(is_superset)   # False ❌ (set_1 doesn't contain 2)
```
 
---
 
## 11. isdisjoint()
 
> Checks if two sets have **absolutely no common elements**
 
```
  True case — circles completely SEPARATE (no overlap):
 
  ( set_1 )    ( set_2 )
  {  3, 5 }    { 'a', 1 }
  no shared elements → True ✅
 
  False case — circles OVERLAPPING:
 
  ( set_1  ( 6 )  set_2 )
  {4,  6 }  ↑  { 2, 6 }
             6 is common → False ❌
```
 
**Syntax:** `set_1.isdisjoint(set_2)`
 
**Example — True case:**
```python
set_a = {1, 2}
set_b = {3, 4}
is_disjoint = set_a.isdisjoint(set_b)
print(is_disjoint)   # True  ✅ (no common elements)
```
 
**Example — False case:**
```python
set_1 = {4, 6}
set_2 = {2, 6}
is_disjoint = set_1.isdisjoint(set_2)
print(is_disjoint)   # False ❌ (6 is common to both)
```
 
---
 
## 12. Subset vs Superset vs Disjoint — Side by Side
 
```
  SUBSET:          SUPERSET:        DISJOINT:
  ┌──────────┐     ┌──────────┐     ( A )   ( B )
  │  set_1   │     │  set_1   │     {3,5}   {'a',1}
  │  ┌────┐  │     │  ┌────┐  │
  │  │set2│  │     │  │set2│  │     No overlap at all
  │  └────┘  │     │  └────┘  │
  └──────────┘     └──────────┘
  set2 inside      set1 is the
  set1 → True      big one → True
```
 
| Method | Question it answers | True when |
|--------|-------------------|-----------|
| `set2.issubset(set1)` | Is set2 inside set1? | set2 ⊆ set1 |
| `set1.issuperset(set2)` | Does set1 contain set2? | set1 ⊇ set2 |
| `set1.isdisjoint(set2)` | Do they share nothing? | set1 ∩ set2 = {} |
 
---
 
## 🔑 Key Takeaways
 
| Topic | Operator/Method | What it does |
|-------|----------------|-------------|
| **Union** | `\|` or `.union()` | All elements from both sets |
| **Intersection** | `&` or `.intersection()` | Only common elements |
| **Difference** | `-` or `.difference()` | Elements in first set only |
| **Symmetric Difference** | `^` or `.symmetric_difference()` | All non-common elements |
| **issubset()** | `set2.issubset(set1)` | Is set2 fully inside set1? |
| **issuperset()** | `set1.issuperset(set2)` | Does set1 fully contain set2? |
| **isdisjoint()** | `set1.isdisjoint(set2)` | Do sets share NO elements? |
| **Method versions** | `.union()`, `.intersection()` etc. | Accept any sequence (list, tuple, string) |
 
