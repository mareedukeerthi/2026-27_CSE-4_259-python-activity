# Text Compression Using Character Runs – Python Project

## 1. Problem Statement

Text Compression Using Character Runs is a program designed to reduce the size of a text string by grouping consecutive repeated characters.

The system uses a technique called Run-Length Encoding (RLE). In this technique, consecutive occurrences of the same character are replaced with the character followed by its repetition count.

For example:

- Original string: `aaabbcccc`
- Encoded string: `a3b2c4`

The program accepts a string, identifies consecutive repeated characters, and generates the compressed string. It then compares the original string length with the encoded string length.

If the encoded string is shorter than the original string, compression is considered beneficial. Otherwise, the program displays that compression is not beneficial.

Objectives:

- Accept a text string from the user.
- Identify consecutive repeated characters.
- Encode repeated characters using character counts.
- Calculate original and encoded string lengths.
- Compare compression efficiency.
- Identify cases where compression is not beneficial.

## 2. Algorithm

1. Start the program.
2. Accept a string from the user.
3. Check whether the input string is empty.
4. Initialize an empty encoded string.
5. Initialize a counter with 1.
6. Traverse the input string character by character.
7. Compare the current character with the next character.
8. If both characters are equal, increment the counter.
9. Otherwise:
   - Append the current character to the encoded string.
   - Append its count if the count is greater than 1.
   - Reset the counter to 1.
10. Repeat until all characters are processed.
11. Calculate the original string length.
12. Calculate the encoded string length.
13. Compare both lengths.
14. If encoded length is smaller, display compression is beneficial.
15. Otherwise, display compression is not beneficial.
16. Display the original string, encoded string, and their lengths.
17. Stop the program.



## 5. Sample Input

Example 1: Compression is beneficial

```
===== TEXT COMPRESSION USING CHARACTER RUNS =====

Enter a string: aaabbcccc
```

## 6. Sample Output

```
========== COMPRESSION RESULT ==========

Original String   : aaabbcccc
Encoded String    : a3b2c4

Original Length   : 9
Encoded Length    : 6
Characters Saved  : 3

Compression Status: Beneficial
Space Saved       : 33.33 %

========================================
```

## 7. Sample Input – Compression Not Beneficial

```
===== TEXT COMPRESSION USING CHARACTER RUNS =====

Enter a string: abcdef
```

Sample Output:

```
========== COMPRESSION RESULT ==========

Original String   : abcdef
Encoded String    : abcdef

Original Length   : 6
Encoded Length    : 6
Characters Saved  : 0

Compression Status: Not Beneficial
Space Saved       : 0%

========================================
```

## 8. Additional Test Cases

| Input string | Encoded string | Original length | Encoded length | Result         |
| ------------ | -------------- | --------------- | -------------- | -------------- |
| `aaaaa`      | `a5`           | 5               | 2              | Beneficial     |
| `aabbcc`     | `a2b2c2`       | 6               | 6              | Not beneficial |
| `abcd`       | `abcd`         | 4               | 4              | Not beneficial |
| `aaabbbccc`  | `a3b3c3`       | 9               | 6              | Beneficial     |
| `xxxxxxxxxx` | `x10`          | 10              | 3              | Beneficial     |

## 9. Mermaid Flowchart Code
``` mermaid

flowchart TD
    A([Start]) --> B[/Enter Input String/]

    B --> C{Is String Empty?}

    C -- Yes --> D[/Display Empty String Error/]
    D --> Z([Stop])

    C -- No --> E[Initialize Encoded String and Counter]

    E --> F[Traverse Input String]

    F --> G{More Characters to Compare?}

    G -- Yes --> H{Current Character Equals Previous?}

    H -- Yes --> I[Increment Counter]
    I --> F

    H -- No --> J[Append Previous Character and Count]
    J --> K[Reset Counter to 1]
    K --> F

    G -- No --> L[Append Final Character and Count]

    L --> M[Calculate Original Length]

    M --> N[Calculate Encoded Length]

    N --> O{Encoded Length < Original Length?}

    O -- Yes --> P[Display Compression Beneficial]

    O -- No --> Q[Display Compression Not Beneficial]

    P --> R[/Display Original and Encoded Strings and Lengths/]
    Q --> R

    R --> Z([Stop])

```
## 10. Result and Conclusion

The Text Compression Using Character Runs program successfully implements Run-Length Encoding (RLE) to compress strings containing consecutive repeated characters.

It calculates the original and compressed string lengths and determines whether compression is beneficial.

Advantages:

- Simple and efficient compression technique.
- Reduces repeated character sequences.
- Easy to implement using Python.
- Identifies cases where compression does not save space.

Time Complexity: \\(O(n)\\), where `n` is the length of the input string.

Space Complexity: \\(O(n)\\), for storing the encoded string.

Conclusion: Run-Length Encoding is an effective basic compression technique for strings containing many consecutive repeated characters. It is less effective for strings containing mostly unique or non-consecutive characters.
