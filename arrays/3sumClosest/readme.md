### README: 3Sum Closest Problem

#### Problem Description
The **3Sum Closest** problem requires finding the sum of three integers in a given array `nums` that is closest to a target value `target`. The goal is to return this sum. You may assume that each input would have exactly one solution.

---

#### Input and Output
- **Input**:
  - An integer array `nums` of length \(n\) (\(n \geq 3\)).
  - An integer `target`.

- **Output**:
  - An integer representing the closest sum of three numbers to `target`.

---

#### Algorithm
1. **Sort the Array**: Start by sorting the array `nums` to enable a two-pointer approach.
2. **Iterate with Three Pointers**:
   - Use a fixed pointer `i` to iterate over the array.
   - Use two pointers, `j` (start of the remaining array) and `k` (end of the array), to search for the best pair that minimizes the difference to `target`.
3. **Adjust Pointers**:
   - If the current sum is less than the `target`, move `j` forward to increase the sum.
   - If the current sum is greater than the `target`, move `k` backward to decrease the sum.
   - If an exact match is found, return the sum immediately.
4. **Track Closest Sum**:
   - Maintain a variable to store the closest sum and update it whenever a smaller difference is found.

---

#### Complexity Analysis
- **Time Complexity**: \(O(n^2)\), where \(n\) is the length of `nums`. Sorting takes \(O(n \log n)\), and iterating with two pointers takes \(O(n^2)\).
- **Space Complexity**: \(O(1)\), as no extra space is used apart from variables.

---

#### Example
Input:  
`nums = [1, 1, 1, 0], target = 100`  

Execution:  
- Closest sum is \(1 + 1 + 1 = 3\).  

Output:  
`3`

---

#### Key Points to Highlight in an Interview
1. The array is sorted first to simplify pointer manipulation.
2. The two-pointer approach ensures an efficient \(O(n^2)\) solution.
3. Handle edge cases like negative numbers, duplicates, or large target values. 

---

Let me know if you'd like any refinements!