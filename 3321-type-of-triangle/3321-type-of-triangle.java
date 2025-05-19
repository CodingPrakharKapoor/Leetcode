class Solution {
    public String triangleType(int[] nums) {
        if(!valid(nums)) return "none";
        
        if(nums[0]!=nums[1] && nums[1]!=nums[2] && nums[2]!=nums[0]) return "scalene";
        
        if(nums[0]==nums[1] && nums[1]==nums[2]) return "equilateral";
        
        return "isosceles";
    }
    
    public boolean valid(int nums[])
    {
        if(nums[0]+nums[1]>nums[2] && nums[0]+nums[2]>nums[1] && nums[1]+nums[2]>nums[0]) return true;
        return false;
    }
}