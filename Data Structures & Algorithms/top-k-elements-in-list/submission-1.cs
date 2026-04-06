public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        var freq = new Dictionary<int, int>();
        var priorityQueue = new PriorityQueue<int, int>();
        var result = new List<int>();

        foreach (var num in nums)
        {
            if (freq.TryGetValue(num, out var value))
            {
                freq[num] = ++value;
            }
            else
            {
                freq.Add(num, 1);
            }
        }
        
        foreach (var kv in freq)
        {
            priorityQueue.Enqueue(kv.Key, kv.Value);
            if (priorityQueue.Count > k)
            {
                priorityQueue.Dequeue();
            }
        }
        
        while (k > 0)
        {
            result.Add(priorityQueue.Dequeue());
            k--;
        }

        return result.ToArray();
    }
}
