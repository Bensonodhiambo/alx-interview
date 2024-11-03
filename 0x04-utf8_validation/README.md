For the UTF-8 validation project, here’s an outline that might help as you start developing the validUTF8 function:

1. Understanding UTF-8 Encoding Rules
Each character in UTF-8 is encoded as 1 to 4 bytes. Here's a summary of how each byte should look based on the number of bytes per character:

1-byte character: Starts with 0xxxxxxx.
2-byte character: Starts with 110xxxxx followed by 10xxxxxx.
3-byte character: Starts with 1110xxxx followed by two 10xxxxxx bytes.
4-byte character: Starts with 11110xxx followed by three 10xxxxxx bytes.
2. Bitwise Operations to Check Each Byte
To validate each byte:

Use bitwise operations to check if each byte matches the expected pattern for UTF-8.
Specifically, for each byte:
Check if it starts with the expected prefix (e.g., 110, 1110, etc.).
For multi-byte characters, verify that each subsequent byte starts with 10.
3. Implementing validUTF8(data)
Initialize a counter for expected continuation bytes.
Iterate through each byte in the list:
If num_continuation_bytes is zero, determine the number of bytes for the current character based on its prefix.
For continuation bytes, verify they start with 10 and decrement the counter.
If you finish with num_continuation_bytes equal to zero, the encoding is valid.
