public class Solution {
    public int LongestConsecutive(int[] nums) {
        var result = 0;

        var numSet = nums.ToHashSet();

        foreach (var num in numSet)
        {
            if (!numSet.Contains(num - 1))
            {
                var currentNum = num;
                var contigLength = 0;
                while (numSet.Contains(currentNum))
                {
                    contigLength++;
                    if (contigLength > result)
                    {
                        result = contigLength;
                    }

                    currentNum++;
                }
            }
        }
        
        return result;
    }
}
