"""
LeetCode Q158: Read N Characters Given read4 II - Call Multiple Times
Given a file and assume that you can only read the file using a given method read4, implement a method read 
to read n characters. Your method read may be called multiple times.
Method read4:
The API read4 reads four consecutive characters from file, then writes those characters into the buffer array buf4.
The return value is the number of actual characters read.
Note that read4() has its own file pointer, much like FILE *fp in C.
"""

# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.buffer = []
        self.buffer_index = 0
    
    def read(self, buf, n: int) -> int:
        total_read = 0
        
        while total_read < n:
            if self.buffer_index < len(self.buffer):
                buf[total_read] = self.buffer[self.buffer_index]
                self.buffer_index += 1
                total_read += 1
            else:
                self.buffer = [''] * 4
                chars_read = read4(self.buffer)
                if chars_read == 0:
                    break
                self.buffer = self.buffer[:chars_read]
                self.buffer_index = 0
        
        return total_read

