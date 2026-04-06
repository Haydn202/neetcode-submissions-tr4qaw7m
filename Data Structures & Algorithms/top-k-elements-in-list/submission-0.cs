public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        var freq = new Dictionary<int, int>();

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

        return freq.Keys.OrderByDescending(key => freq[key]).Take(k).ToArray();
    }
}
