public class Solution {
    public string Encode(IList<string> strs)
    {
        return string.Concat(strs.SelectMany(s=>  $"{s.Length}#{s}"));
    }

    public List<string> Decode(string s)
    {
        var result = new List<string>();

        var i = 0;

        while (i < s.Length)
        {
            var j = i;
            while (s[j] is not '#')
            {
                j++;
            }
            
            int.TryParse(s.AsSpan(i, j-i), out var len);

            j++;
            result.Add(s.Substring(j, len));

            i = j + len;
        }

        return result;
    }
}
