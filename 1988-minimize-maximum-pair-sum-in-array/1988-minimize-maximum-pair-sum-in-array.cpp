class Solution {
public:
    int minPairSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        int ans=0;
        int n=nums.size();
        for(int x=0;x<n/2;x++)
        {
            ans=max(ans,nums[x]+nums[n-x-1]);
        }
        return ans;
    }
};