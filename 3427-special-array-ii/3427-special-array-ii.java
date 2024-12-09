class Solution {
    public boolean[] isArraySpecial(int[] nums, int[][] queries) {
        boolean ar[]=new boolean[queries.length];
        int check[]=new int[nums.length];
        int count=0;
        for(int x=1;x<nums.length;x++)
        {
            if(nums[x]%2==nums[x-1]%2) count++;
            check[x]=count;
        }
        int index=0;
        for(int x[]:queries)
        {
            int mis=check[x[1]]-check[x[0]];
            if(mis==0) ar[index]=true;
            index++;
        }
        return ar;
    }
}