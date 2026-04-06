public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        var anaSet = new Dictionary<string, List<string>>();
        foreach (var word in strs) {
            var ordererd = String.Concat(word.OrderBy(c => c));
            
            if (anaSet.ContainsKey(ordererd)) {
                anaSet[ordererd].Add(word);
            } else {
                anaSet.Add(ordererd, new List<string>{word});
            }
        }

        return anaSet.Values.ToList();
    }
}
