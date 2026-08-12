class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+ 1)]
        print(freq)

        for n in nums:
            count[n] = 1 + count.get(n,0)
        print(count)

        for number, c in count.items(): #gives key,value pair
            freq[c].append(number)

        print(freq)
        result = []
        for i in range(len(freq)- 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result

        