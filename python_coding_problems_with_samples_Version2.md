# Python Coding Problems: Questions, Sample Inputs, Code, and Outputs

## 1. Extract Digits and Find Sum, Min, and Max

**Question:**  
Given a string, extract all the digits, convert them to integers, and print the sum, minimum, and maximum of these digits, each on a new line.

**Sample Input:**
```
c9u3db
```

**Code:**
```python
x = list(input()) 
digits = []
for i in x:
    if i.isdigit():
        digits = digits + [int(i)] 
print(sum(digits)) 
print(min(digits))
print(max(digits))
```

**Sample Output:**
```
12
3
9
```

---

## 2. Sort a List of Integers in Descending Order

**Question:**  
Given a comma-separated list of integers as input, print the list sorted in descending order.

**Sample Input:**
```
5,7,2,9,1
```

**Code:**
```python
x = list(map(int, input().split(",")))
print(sorted(x, reverse=True))
```

**Sample Output:**
```
[9, 7, 5, 2, 1]
```

---

## 3. Sum of the Largest 5 Numbers

**Question:**  
Given a comma-separated list of integers as input, print the sum of the largest 5 numbers.

**Sample Input:**
```
5,7,2,9,1,6,3
```

**Code:**
```python
x = sorted(list(map(int, input().split(","))), reverse=True)
total = 0
for i in range(5):
    total += x[i]
print(total)
```

**Sample Output:**
```
30
```
*(Explanation: Largest five numbers are 9, 7, 6, 5, 3; their sum is 9+7+6+5+3=30)*

---

## 4. Find the k-th Largest Number

**Question:**  
Given a comma-separated list of integers as input, and then an integer `k`, print the k-th largest number in the list.

**Sample Input:**
```
5,7,2,9,1,6,3
3
```

**Code:**
```python
x = sorted(list(map(int, input().split(","))), reverse=True)
k = int(input()) - 1
print(x[k])
```

**Sample Output:**
```
6
```
*(Explanation: Sorted descending: 9, 7, 6, 5, 3, 2, 1; 3rd largest is 6)*

---