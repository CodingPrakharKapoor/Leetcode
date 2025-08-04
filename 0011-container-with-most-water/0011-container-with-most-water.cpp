class Solution {
public:
    int maxArea(vector<int>& height) {
        int a=0;
        int b=height.size()-1;
        int maxi=0;
        while(a<b)
        {
            int w=b-a;
            int h=min(height[a],height[b]);
            int ar=h*w;
            maxi=max(maxi,ar);
            if(height[a]<height[b])
            {
                a++;
            }
            else if(height[a]>height[b])
            {
                b--;
            }
            else
            {
                a++;
                b--;
            }
        }
        return maxi;
    }
};
