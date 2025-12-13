"""
LeetCode Q182: Duplicate Emails
SQL Problem - Write a solution to report all the duplicate emails. Note that it's guaranteed that the email field is not NULL.
Return the result table in any order.
"""

# SQL Solution:
# SELECT email
# FROM Person
# GROUP BY email
# HAVING COUNT(*) > 1

# Python solution for reference:
class Solution:
    def duplicateEmails(self, emails: list[str]) -> list[str]:
        from collections import Counter
        email_count = Counter(emails)
        return [email for email, count in email_count.items() if count > 1]

