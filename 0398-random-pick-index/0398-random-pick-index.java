class Solution {
    HashMap<Integer,List<Integer>> map=new HashMap<>();
    public Solution(int[] nums) {
        for(int x=0;x<nums.length;x++)
        {
            int num=nums[x];
            if(map.containsKey(num))
            {
                map.get(num).add(x);
            }
            else
            {
                map.put(num,new ArrayList<>());
                map.get(num).add(x);
            }
        }
    }
    
    public int pick(int target) {
        List<Integer> list=map.get(target);
        int n=list.size();
        int index=(int)Math.floor(Math.random()*(n-1-0+1))+0;
        return list.get(index);
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int param_1 = obj.pick(target);
 */