"""
LeetCode Q183: Customers Who Never Order
SQL Problem - Write a solution to find all customers who never order anything.
Return the result table in any order.
"""

# SQL Solution:
# SELECT c.name AS Customers
# FROM Customers c
# LEFT JOIN Orders o ON c.id = o.customerId
# WHERE o.id IS NULL


# Python solution for reference:
class Solution:
    def customersWhoNeverOrder(
        self, customers: list[dict], orders: list[dict]
    ) -> list[str]:
        ordered_customer_ids = {order["customerId"] for order in orders}
        return [
            customer["name"]
            for customer in customers
            if customer["id"] not in ordered_customer_ids
        ]
