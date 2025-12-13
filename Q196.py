"""
LeetCode Q196: Delete Duplicate Emails
SQL Problem - Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.
For SQL users, please note that you are supposed to write a DELETE statement and not a SELECT one.
"""

# SQL Solution:
# DELETE p1 FROM Person p1
# INNER JOIN Person p2
# WHERE p1.id > p2.id AND p1.email = p2.email

# Python solution for reference:
class Solution:
    def deleteDuplicateEmails(self, persons: list[dict]) -> list[dict]:
        seen_emails = {}
        result = []
        
        for person in sorted(persons, key=lambda x: x['id']):
            email = person['email']
            if email not in seen_emails:
                seen_emails[email] = person['id']
                result.append(person)
        
        return result

