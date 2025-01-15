class Solution {
    public boolean isAnagram(String s, String t) {
        int sf[]=new int[26];
        int tf[]=new int[26];
        for(int x:s.toCharArray())
        {
            sf[x-'a']++;
        }
        for(int x:t.toCharArray())
        {
            tf[x-'a']++;
        }
        for(int x=0;x<26;x++)
        {
            if(sf[x]!=tf[x]) return false;
        }
        return true;
    }
}