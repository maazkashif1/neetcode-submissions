class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a hash, store number as key and it's occurances as value in the map
        # sort the map in descending
        # return top k values from the map

        map = {}

        for num in nums:
            map[num]=map.get(num,0)+1

        sorted_items = sorted(map.items(), key=lambda x: x[1], reverse=True)

        return [num for (num, count) in sorted_items[:k]]