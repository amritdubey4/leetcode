"""
LeetCode Q170: Two Sum III - Data structure design
Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.
Implement the TwoSum class:
- TwoSum() Initializes the TwoSum object, with an empty array initially.
- void add(int number) Adds number to the data structure.
- boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false.
"""

class TwoSum:
    def __init__(self):
        self.numbers = {}
    
    def add(self, number: int) -> None:
        self.numbers[number] = self.numbers.get(number, 0) + 1
    
    def find(self, value: int) -> bool:
        for num in self.numbers:
            complement = value - num
            if complement in self.numbers:
                if complement != num or self.numbers[complement] > 1:
                    return True
        return False

