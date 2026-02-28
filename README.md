<!-- # Logarithmic‑Time

**Explanation of Logarithmic Time Complexity (O(log n))**

This repository provides examples and explanations related to **logarithmic time complexity**, often written as **O(log n)** — a highly efficient type of algorithmic complexity.

---

## 📊 What Is Logarithmic Time (O(log n))?

In algorithm analysis, **logarithmic time complexity** means that the running time of an algorithm **grows logarithmically with the size of the input**. This occurs when the algorithm repeatedly reduces the size of the input by a factor (like halving it) at each step. Because of this repeated reduction, the number of operations increases **very slowly** even as the input becomes large.



## 📌 Common Examples of O(log n) Algorithms

Here are typical situations where logarithmic time complexity appears:

- **Binary Search:** An efficient search algorithm for sorted data that *halves* the search space at each step. 
- **Operations on Balanced Trees:** Search, insert, and delete operations in balanced binary search tree structures often run in O(log n) time. 

*(These examples work by cutting the problem size significantly with each operation.)* 

---

## 📁 Source Code
```python
import math

def binary_search_explanation(data_list, target):
    """
    This function demonstrates O(log n) - Logarithmic Time Complexity.
    
    Logarithmic time means that the time (number of steps) increases 
    proportionally to the logarithm of the input size (n). 
    In practical terms: every time you double the size of the input, 
    you only add ONE additional step to the process.
    """

    low = 0
    high = len(data_list) - 1
    steps = 0

    print(f"Searching for {target} in a list of size {len(data_list)}....")

    while low <= high:
        steps += 1
        # In each step we find the middle of the current range
        mid = (low + high) // 2
        guess = data_list[mid]

        print(f"Step {steps}: Checkd index {mid} (Value: {guess})")

        if guess == target:
            print(f"-> Sucess! Found {target} in {steps} steps")

            return steps
        
        # LOGARITHMIC MAGIC HAPPENS HERE
        # We don't just move one item at a time (which would be O(n))
        # We discord HALF of the remaining search area in every single step

        if guess > target:
            # Target is in lower half, discard the upper half
            high = mid + 1
        else: 
            # Target is in the uper half, discard the lower half
            low = mid + 1

    print(f"-> {target} not found after {steps} steps.")

    return steps





def run_demonstration():
    # 1. Setup an input of size 1,000 (n = 1000)
    # Since log2(1000) is approx 10, it should take ~10 steps max
    size_n = 1000
    test_data = list(range(size_n))

    print("-" * 30)
    print(f"SCENARIO 1: n = {size_n}")
    print("-" * 30)
    steps_small = binary_search_explanation(test_data, 999)

    # 2. Setup an input of size 1,000,000 (n = 1,000,000)
    # Even though the size increased by 1,000x, the steps will barely increase
    # log2(1,000,000) is approx 20
    size_huge = 1_000_000
    test_data_huge = list(range(size_huge))

    print("-" * 30)
    print(f"SCENARIO 2: n = {size_huge} (1,000x target!)")
    print("-" * 30)
    steps_large = binary_search_explanation(test_data_huge,999999)

    print("-" * 30)
    print("THE LOGARITHMIC CONCLUSION")
    print(f"Input size increased by: {size_huge // size_n} x")
    print(f"Steps only increased by : {steps_large - steps_small} additional steps.")
    print("Thi is why O( log n) is extremely efficient for large datasets")
    print("-" *30)



if __name__ == "__main__":
    run_demonstration()



"""
WHY IS THIS LOGARITHMIC?
------------------------
Imagine you have 128 items.
Step 1: 128 -> 64  left
Step 2: 64  -> 32  left
Step 3: 32  -> 16  left
Step 4: 16  -> 8   left
Step 5: 8   -> 4   left
Step 6: 4   -> 2   left
Step 7: 2   -> 1   left (Found!)

Mathematically: 2^7 = 128. 
Therefore, log2(128) = 7.
The number of steps is the exponent you need to raise 2 to in order to get n.
"""
```

---

## 🧠 Why It Matters

O(log n) is considered **very efficient**, especially compared to linear (O(n)), quadratic (O(n²)), or worse time complexities. Algorithms with logarithmic time complexity are able to handle large inputs without scanning every element — they instead reduce the problem size quickly at each step. 

---


-->







<!-- # 📘 Logarithmic Time – README -->

<h1 align="center">Logarithmic Time</h2>

## Overview

**Logarithmic Time** refers to an algorithm whose runtime grows proportionally to the logarithm of the input size.

If the input size doubles, the running time only increases by one step (in base 2 logarithm).

In algorithm analysis, this is written as:

```
O(log n)
```

Logarithmic time is highly efficient and common in algorithms that divide the problem in half each step.

<a href="/src/main.py">Check out for source code</a>

---

## ⚙️ What Logarithmic Time Means

An algorithm runs in logarithmic time when each operation reduces the problem size significantly, usually by a constant fraction.

Common examples:

* Binary Search
* Searching in a balanced binary tree
* Finding an item in a sorted array using divide-and-conquer
* Some divide-and-conquer algorithms

For an input of **n elements**, the algorithm performs about log₂(n) steps.

---

## 🧠 Python Examples

### Example 1 — Binary Search

```python id="bslog1"
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1


arr = [1, 3, 5, 7, 9, 11]
print(binary_search(arr, 7))  # Output: 3
```

Each step halves the search space → **O(log n)** time.

---

### Example 2 — Finding the Exponent

```python id="logexp2"
def power_of_two(n):
    count = 0
    while n > 1:
        n = n // 2
        count += 1
    return count


print(power_of_two(16))  # Output: 4
```

Number of divisions grows logarithmically → **O(log n)**.

---

### Example 3 — Searching in a Balanced Binary Tree

```python id="logbtree3"
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def search(node, target):
    if node is None:
        return False
    if node.value == target:
        return True
    elif target < node.value:
        return search(node.left, target)
    else:
        return search(node.right, target)
```

Each level halves the search space → **O(log n)**.

---

## ⏱️ Time Complexity Comparison

| Complexity   | Meaning           |
| ------------ | ----------------- |
| O(1)         | Constant time     |
| **O(log n)** | Logarithmic time  |
| O(n)         | Linear time       |
| O(n log n)   | Linearithmic time |
| O(n²)        | Quadratic time    |

Logarithmic algorithms scale exceptionally well for large datasets.

---

## 👍 Advantages

* Extremely fast for large inputs
* Efficient search and divide-and-conquer algorithms
* Reduces problem size quickly
* Works well with sorted data

## 👎 Disadvantages

* Usually requires the data to be **sorted**
* Slightly more complex to implement than linear algorithms
* Not all problems can be solved logarithmically

---

## 📌 When Logarithmic Time Occurs

Logarithmic time operations appear in:

* Binary search in sorted arrays
* Searching in balanced binary search trees
* Some divide-and-conquer algorithms
* Certain mathematical computations

---

## 🏁 Summary

Logarithmic time complexity **O(log n)** means the runtime increases very slowly as input size grows.
Algorithms with logarithmic time are extremely efficient and highly desirable for large datasets.
