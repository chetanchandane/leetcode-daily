### 4Sum Problem

#### Problem Description
The **4Sum** problem involves finding all unique quadruplets \((a, b, c, d)\) in a given array `nums` such that the sum of \(a + b + c + d = \text{target}\). The goal is to return all such quadruplets without duplicates.

---

#### Input and Output
- **Input**:
  - `nums`: An integer array of size \(n\) (\(n \geq 4\)).
  - `target`: An integer representing the target sum.

- **Output**:
  - A list of lists, where each inner list is a unique quadruplet whose sum equals the target.

---

#### Algorithm
1. **Sort the Array**: Sorting simplifies pointer manipulation and duplicate avoidance.
2. **Use Nested Loops**:
   - Use two nested loops to fix the first two numbers in the quadruplet.
3. **Two-Pointer Approach**:
   - For the remaining two numbers, use two pointers (`k` and `m`) to find pairs that complete the target sum.
4. **Handle Duplicates**:
   - Skip duplicate values for all four numbers to ensure unique quadruplets.
5. **Return Results**:
   - Store the quadruplets in a result list and return it after iterating through all possibilities.

---

#### Complexity
- **Time Complexity**: \(O(n^3)\) — Sorting takes \(O(n \log n)\), and the three nested loops take \(O(n^3)\).
- **Space Complexity**: \(O(1)\) — Excludes the result list storage.

---

#### Example
**Input**:  
`nums = [1, 0, -1, 0, -2, 2], target = 0`  

**Output**:  
`[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]`

---

#### Pseudocode
1. Sort the array.
2. Iterate over the array with two nested loops:
   - First loop: Fix the first number \(i\).
   - Second loop: Fix the second number \(j\).
3. Use two pointers (`k` and `m`) to find the remaining two numbers:
   - If the sum is equal to the target, store the quadruplet and move both pointers to avoid duplicates.
   - If the sum is less than the target, move the `k` pointer forward.
   - If the sum is greater than the target, move the `m` pointer backward.
4. Return the list of quadruplets.

---

#### Key Considerations
- Ensure no duplicate quadruplets by skipping repeated numbers in the loop and pointers.
- Use a sorted array to simplify the two-pointer logic.
- Handle edge cases like:
  - Arrays with fewer than 4 elements.
  - Arrays with negative numbers.
  - Large target values.

---

#### Key Points to Highlight in an Interview
1. Explain the use of sorting and the two-pointer technique.
2. Discuss how duplicates are avoided to ensure unique quadruplets.
3. Provide an example and walk through the logic step-by-step.
4. Mention the \(O(n^3)\) complexity and how it balances between correctness and efficiency. 

