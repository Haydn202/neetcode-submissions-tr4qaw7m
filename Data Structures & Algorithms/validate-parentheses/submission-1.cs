public class Solution
{
    private static readonly Dictionary<char, char> bracketPairs = new Dictionary<char, char>
    {
        { '}', '{' },
        { ']', '[' },
        { ')', '(' }
    };

    public bool IsValid(string s)
    {
        var stack = new Stack<char>();

        foreach (char letter in s)
        {
            if (bracketPairs.ContainsValue(letter)) // Opening bracket
            {
                stack.Push(letter);
            }
            else if (bracketPairs.TryGetValue(letter, out char expectedOpen)) // Closing bracket
            {
                if (stack.Count == 0 || stack.Pop() != expectedOpen)
                {
                    return false;
                }
            }
        }

        return stack.Count == 0;
    }
}