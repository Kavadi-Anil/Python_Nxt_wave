# Function Call Stack & Recursion

---

## Stack

A **stack** is a data structure that stores items in a **Last-In/First-Out (LIFO)** manner.

---

## Calling a Function

You can call one function inside another function.

**Example:**

```python
def function_1():
    def function_2():
        function_1()  # calling a function inside another function
```

---

## Example: Functions Calling Other Functions

```python
def get_largest_sqr(list_x):  
    len_list = len(list_x)
    for i in range(len_list):
        x = list_x[i]
        list_x[i] = x * x
    largest = max(list_x)
    return largest

list_a = [1, -3, 2]
result = get_largest_sqr(list_a)
print(result)
```

**Output:**
```
9
```
- In the above code, `len()` and `max()` are called inside `get_largest_sqr()`.

---

## Example: Nested Function Calls

```python
def get_sqrd_val(x): 
    return (x * x)

def get_sum_of_sqrs(list_a): 
    sqrs_sum = 0
    for i in list_a:
        sqrs_sum += get_sqrd_val(i)
    return sqrs_sum

list_a = [1, 2, 3]
sum_of_sqrs = get_sum_of_sqrs(list_a)
print(sum_of_sqrs)
```

**Output:**
```
14
```

---

## Function Call Stack

The **Function Call Stack** keeps track of function calls currently in progress. When a function is called, it is placed (pushed) on top of the call stack. When the function finishes, it is removed (popped) from the stack.

---

## Recursion

**Recursion** is when a function calls itself.

**General Structure:**
```python
def function_2():
    function_2()  # function calling itself
```

---

### Example: Multiply N Numbers (Factorial)

```python
def factorial(n):  # Recursive Function
    if n == 1:      # Base Case
        return 1
    return n * factorial(n - 1)  # Recursive Call

num = int(input())
result = factorial(num)
print(result)
```

**Base Case:**
- A recursive function terminates when the base condition is met.

**Sample Input:**
```
3
```
**Sample Output:**
```
6
```

---

### Without Base Case (Problem Example)

```python
def factorial(n):
    return n * factorial(n - 1)

num = int(input())
result = factorial(num)
print(result)
```

**Sample Input:**
```
3
```
**Output:**
```
RecursionError: maximum recursion depth exceeded
```

*Without a base case, the recursive function never stops and results in a recursion error.*

---
