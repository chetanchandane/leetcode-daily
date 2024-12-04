**Time and Space Complexity**

`O(n^2)`


1. Iterating through each and every number in the grid
2. As we iterate we check if the currect element already exists in the dictionaries.
3. if not we add the element in the respective dict.
4. As for the 3x3 blocks, we will be grouping the elements by dividing the indices by 3, that way we will be certainly getting the 3x3 block location for each element so we can store it in the respective dict.key.

`block[[r//3, c//3]]`