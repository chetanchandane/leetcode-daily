
### Explanation of the `threeSum` Algorithm

#### Problem Statement:
The goal is to find all unique triplets in the array `nums` that sum to zero. Each triplet must be unique, meaning the same elements in a different order are not allowed.

---

### Algorithm Description:

1. **Sort the Input Array**:
   - The array is sorted to make it easier to handle duplicates and use the two-pointer technique for finding pairs efficiently.

2. **Iterate Through the Array**:
   - A for-loop iterates through the array with the index `i`, considering `nums[i]` as the first element of the triplet.
   - Skip duplicate elements for `nums[i]` by checking `nums[i] == nums[i - 1]` to avoid generating duplicate triplets.

3. **Two-Pointer Technique**:
   - For each `nums[i]`, initialize two pointers: `j` (pointing to the element immediately after `i`) and `k` (pointing to the last element in the array).
   - Compute the sum of the triplet: `nums[i] + nums[j] + nums[k]`.

4. **Adjust the Pointers**:
   - If the sum is greater than 0, decrement `k` to reduce the sum.
   - If the sum is less than 0, increment `j` to increase the sum.
   - If the sum equals 0:
     - Append the triplet `[nums[i], nums[j], nums[k]]` to the output list `out`.
     - Increment `j` to look for the next potential pair but skip duplicate values for `nums[j]` by checking `nums[j] == nums[j - 1]`.

5. **Return the Result**:
   - After the loop completes, `out` contains all unique triplets that sum to zero.

---

### Key Points:
1. **Avoiding Duplicates**:
   - Duplicate triplets are avoided by:
     - Skipping duplicate `nums[i]` in the outer loop.
     - Skipping duplicate `nums[j]` when adding triplets.

2. **Efficiency**:
   - Sorting the array ensures efficient pair finding using the two-pointer approach.
   - The algorithm runs in \(O(n^2)\) time:
     - \(O(n)\) for the outer loop.
     - \(O(n)\) for the two-pointer traversal in the inner loop.

3. **Edge Cases**:
   - Handles arrays with fewer than three elements by returning an empty list.
   - Works correctly even with multiple duplicates or no valid triplets.

---

### Code Complexity:
- **Time Complexity**: \(O(n^2)\), where \(n\) is the number of elements in `nums`. Sorting takes \(O(n \log n)\), and the two-pointer search takes \(O(n^2)\).
- **Space Complexity**: \(O(n)\) for sorting if it’s not done in-place (depends on the sorting algorithm).

