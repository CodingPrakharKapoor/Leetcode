class Solution {
    public String gcdOfStrings(String str1, String str2) {
        if(!(str1+str2).equals(str2+str1))
        {
            return "";
        }
        int l1=str1.length();
        int l2=str2.length();
        int gcd=1;
        int min=Math.min(l1,l2);
        for(int x=2;x<=min;x++)
        {
            if(l1%x==0 && l2%x==0)
            {
                gcd=x;
            }
        }
        return str2.substring(0,gcd);
    }
}