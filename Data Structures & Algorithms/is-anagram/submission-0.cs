public class Solution {
    public bool IsAnagram(string s, string t)
    {
        var firstStringDict = GetLetterDictionary(s);
        var secondStringDict = GetLetterDictionary(t);

        return firstStringDict.OrderBy(kv => kv.Key)
            .SequenceEqual(secondStringDict.OrderBy(kv => kv.Key));
    }

    private Dictionary<char, int> GetLetterDictionary(string word)
    {
        var stringDict = new Dictionary<char, int>();
        
        foreach (var letter in word.ToCharArray())
        {
            if (!stringDict.TryAdd(letter, 1))
            {
                stringDict[letter] += stringDict[letter];
            }
        }

        return stringDict;
    }
}
