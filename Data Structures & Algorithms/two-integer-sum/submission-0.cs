public class Solution {
    public int[] TwoSum(int[] nums, int target)
    {
        var numDict = new Dictionary<int, int>();
        var index = 0;

        foreach (var num in nums)
        {
            if (numDict.ContainsKey(target - num))
            {
                return new int[] {numDict[target - num], index};
            }
            
            numDict.Add(num, index);
            index++;
        }

        return null;
    }
}
