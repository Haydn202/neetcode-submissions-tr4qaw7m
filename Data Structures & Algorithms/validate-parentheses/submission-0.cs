public class Solution
{
    private readonly HashSet<char> open = new HashSet<char> { '{', '[', '(' };
    private readonly HashSet<char> close = new HashSet<char> { '}', ']', ')' };

    public bool IsValid(string s)
    {
        var stack = new Stack<char>();

        foreach (char letter in s)
        {
            if (open.Contains(letter))
            {
                stack.Push(letter);
            }
            else if (close.Contains(letter))
            {
                if (stack.Count == 0 || !BracketsMatch(stack.Peek(), letter))
                {
                    return false;
                }
                stack.Pop();
            }
        }

        return stack.Count == 0;
    }

    private bool BracketsMatch(char open, char closed)
    {
        return (open == '{' && closed == '}') ||
               (open == '[' && closed == ']') ||
               (open == '(' && closed == ')');
    }
}