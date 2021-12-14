class Solution {
public:
    void sortColors(vector<int>& nums) {
        int red=0,white=0,blue=0;
        for(int i=0; i<nums.size(); i++)
        {
            if(nums[i]==0)
                red++;
            else if (nums[i]==1)
                white++;
            else
                blue++;
        }
        
        
        for(int i=0; i<red; i++)
            nums[i]=0;
        
        for(int i=red; i < white+red; i++)
            nums[i]=1;
        
        for(int i=white+red; i < nums.size(); i++)
            nums[i]=2;
        
        
    }
};
