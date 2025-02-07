class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        my_dict = {}
        value_count = {}
        distinct_values = set()
        count = []

        for i in range(len(queries)):
            key, value = queries[i]
            
            if key in my_dict:
                old_value = my_dict[key]
                value_count[old_value] -= 1
                if value_count[old_value] == 0:
                    distinct_values.remove(old_value)
            
            my_dict[key] = value
            value_count[value] = value_count.get(value, 0) + 1
            distinct_values.add(value)
            
            count.append(len(distinct_values))

        return count