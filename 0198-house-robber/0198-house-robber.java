class Solution {
    public int rob(int[] nums) {
        int dp[]=new int[nums.length];
        Arrays.fill(dp,-1);
        return robbing(0,nums,dp);
    }
    public int robbing(int i,int nums[],int dp[])
    {
        if(i>=dp.length) return 0;
        if(dp[i]!=-1) return dp[i];

        int take=nums[i]+robbing(i+2,nums,dp);
        int dont=robbing(i+1,nums,dp);

        dp[i]=Math.max(take,dont);
        return dp[i];
    }
}