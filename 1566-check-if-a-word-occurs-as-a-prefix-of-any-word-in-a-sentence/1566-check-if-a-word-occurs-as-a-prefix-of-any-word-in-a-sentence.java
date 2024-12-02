import java.util.*;
class Solution {
    public int isPrefixOfWord(String sentence, String searchWord) {
        StringTokenizer st=new StringTokenizer(sentence," ");
        int count=1;
        while(st.hasMoreTokens())
        {
            String str=st.nextToken();
            if(str.indexOf(searchWord)==0)
            {
                return count;
            }
            else count++;
        }
        return -1;
    }
}