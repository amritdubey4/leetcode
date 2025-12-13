"""
LeetCode Q197: Rising Temperature
SQL Problem - Write a solution to find all dates' Id with higher temperatures compared to its previous dates (yesterday).
Return the result table in any order.
"""

# SQL Solution:
# SELECT w1.id
# FROM Weather w1
# JOIN Weather w2 ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
# WHERE w1.temperature > w2.temperature

# Python solution for reference:
class Solution:
    def risingTemperature(self, weather: list[dict]) -> list[int]:
        from datetime import datetime, timedelta
        result = []
        weather_sorted = sorted(weather, key=lambda x: x['recordDate'])
        
        for i in range(1, len(weather_sorted)):
            if weather_sorted[i]['temperature'] > weather_sorted[i - 1]['temperature']:
                date1 = datetime.strptime(weather_sorted[i]['recordDate'], '%Y-%m-%d')
                date2 = datetime.strptime(weather_sorted[i - 1]['recordDate'], '%Y-%m-%d')
                if (date1 - date2).days == 1:
                    result.append(weather_sorted[i]['id'])
        
        return result

