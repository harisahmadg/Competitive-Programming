from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        outgoing_count = {}

        for path in paths:
            city_a, city_b = path
            outgoing_count[city_a] = outgoing_count.get(city_a, 0) + 1
            outgoing_count[city_b] = outgoing_count.get(city_b, 0)
        
        current = 0

        for city_key in outgoing_count:
            if outgoing_count[city_key] == 0:
                return city_key


obj = Solution()

input = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
print(obj.destCity(input))