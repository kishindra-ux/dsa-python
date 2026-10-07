# Merge Strings Alternately
## Intuition
The goal was to merge two string alternating characters. 
For handeling this when one is larger than the other without getting a error, I itrate through the maximum length of both strings and insert space placeholders for the shorter string, which can be cleaned up at the end.

## Approach
1. Determine the maximum length between word1 and word2.
2. Initialize an empty list merged to collect the characters.
3. Loop from 0 to max_length - 1. In each iteration:
	• Check if the index i is within the bounds of word1. If yes, append the character; otherwise, append a space placeholder " ".
	• Check if the index i is within the bounds of word2. If yes, append the character; otherwise, append a space placeholder " ".
4. Combine the list into a single string.
5. Use .replace(" ", "") to strip out all the blank space placeholders before returning the final merged string.

## Complexity

- Time complexity:
\(O(\max (N,M))\)
Where \(N\) is the length of word1 and \(M\) is the length of word2. The loop runs exactly \(\max(N, M)\) times, and the final .replace() operation takes linear time relative to the size of the combined string.

- Space complexity:
\(O(\max (N,M))\)
The merged list holds up to \(2 \times \max(N, M)\) characters (including placeholders) before joining, which scales linearly with the maximum input length.

## How to Run 
```python3 []
```
