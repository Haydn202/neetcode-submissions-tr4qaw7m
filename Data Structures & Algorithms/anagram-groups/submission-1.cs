public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        var groups = new Dictionary<string, List<string>>();
        foreach (var word in strs) {
            var hash = new string (word.OrderBy(c => c).ToArray());
            
            if (groups.ContainsKey(hash)) {
                groups[hash].Add(word);
            } else {
                groups.Add(hash, new List<string>{word});
            }
        }

        return groups.Values.ToList();
    }
}
