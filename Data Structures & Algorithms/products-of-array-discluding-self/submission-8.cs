public class Solution {
    public int[] ProductExceptSelf(int[] nums)
    {
        var result = new List<int>();

        var totalProduct = nums[0];

        for (var i = 1; i < nums.Length; i++)
        {
            if (nums[i] is not 0)
            {
                totalProduct *= nums[i];
            }
        }

        foreach (var num in nums)
        {
            if (num is 0)
            {
                if (nums.Where(n => n == 0).Count() > 1)
                {
                    result.Add(0);
                } else {
                    result.Add(totalProduct);
                }
            }
            else
            {
                if (nums.Contains(0))
                {
                    result.Add(0);
                }
                else
                {
                    result.Add(totalProduct / num);
                }
            }
        }
        return result.ToArray();
    }
}
