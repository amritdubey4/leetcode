"""
LeetCode Q157: Read N Characters Given Read4
Given a file and assume that you can only read the file using a given method read4, implement a method to read n characters.
Method read4:
The API read4 reads four consecutive characters from file, then writes those characters into the buffer array buf4.
The return value is the number of actual characters read.
Note that read4() has its own file pointer, much like FILE *fp in C.
"""

# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def read(self, buf, n: int) -> int:
        total_read = 0
        buf4 = [''] * 4
        
        while total_read < n:
            chars_read = read4(buf4)
            if chars_read == 0:
                break
            
            for i in range(min(chars_read, n - total_read)):
                buf[total_read] = buf4[i]
                total_read += 1
        
        return total_read

