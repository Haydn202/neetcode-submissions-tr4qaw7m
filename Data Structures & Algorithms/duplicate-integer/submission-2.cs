public class Solution {
    public bool hasDuplicate(int[] nums) {
        var valuesDict = new Dictionary<int, int>();

        foreach(var num in nums)
        {
            if(!valuesDict.TryAdd(num, 1))
            {
                valuesDict[num] += 1;
            }
        }

        return valuesDict.Values.Any(n => n is not 1);
    }
}
