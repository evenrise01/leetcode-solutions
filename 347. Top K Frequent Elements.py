class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each element
        frequency = Counter(nums)
        
        # Step 2: Create buckets (list of lists) to store elements by frequency
        max_frequency = max(frequency.values())
        buckets = [[] for _ in range(max_frequency + 1)]
        
        for num, freq in frequency.items():
            buckets[freq].append(num)
        
        # Step 3: Collect the top k frequent elements
        result = []
        for i in range(len(buckets) - 1, 0, -1):  # Traverse buckets in reverse (highest frequency first)
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:  # Stop once we've found k elements
                    return result