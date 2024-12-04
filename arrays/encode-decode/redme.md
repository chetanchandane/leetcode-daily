# String Encode and Decode Solution

## Overview
This project implements a solution for encoding and decoding a list of strings. It provides two functions:

1. **`encode(strs: List[str]) -> str`**:
   - Converts a list of strings into a single encoded string.
   - Each string is prefixed with its length and a delimiter `"#"`.
   - Example: `encode(["hello", "world"])` outputs `"5#hello5#world"`.

2. **`decode(s: str) -> List[str]`**:
   - Decodes the encoded string back into the original list of strings.
   - Parses the length prefix to extract each string.
   - Example: `decode("5#hello5#world")` outputs `["hello", "world"]`.

---

## Time Complexity

1. **`encode` Function**:
   - Iterates through the list of strings and concatenates each string with its length.
   - **Time Complexity**: `O(n)`, where `n` is the total length of all strings.

2. **`decode` Function**:
   - Scans the encoded string, parses lengths, and extracts substrings.
   - **Time Complexity**: `O(n)`, where `n` is the length of the encoded string.

---

## Space Complexity

1. **`encode` Function**:
   - Constructs a single encoded string.
   - **Space Complexity**: `O(n)`.

2. **`decode` Function**:
   - Creates a list to store the decoded strings.
   - **Space Complexity**: `O(n)`.

---

## Example Usage

```python
solution = Solution()

# Encode
strs = ["hello", "world"]
encoded = solution.encode(strs)
print("Encoded:", encoded)  # Output: "5#hello5#world"

# Decode
decoded = solution.decode(encoded)
print("Decoded:", decoded)  # Output: ["hello", "world"]
```

