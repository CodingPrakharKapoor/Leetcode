class Solution {
    public int rob(int[] nums) {
        if(nums.length==1) return nums[0];
        if(nums.length==2) return Math.max(nums[0],nums[1]);

        int dp[]=new int[nums.length];
        Arrays.fill(dp,-1);
        int a=robbing(0,nums.length-2,nums,dp);
        Arrays.fill(dp,-1);
        int b=robbing(1,nums.length-1,nums,dp);
        return Math.max(a,b);
    }
    public int robbing(int start,int end,int nums[],int dp[])
    {
        if(start>end) return 0;
        if(dp[start]!=-1) return dp[start];

        int take=nums[start]+robbing(start+2,end,nums,dp);
        int dont=robbing(start+1,end,nums,dp);

        dp[start]=Math.max(take,dont);
        return dp[start];
    }
}