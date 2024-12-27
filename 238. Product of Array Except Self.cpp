class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n=nums.size();
        int fromBegin=1;
        int fromLast=1;
        vector<int> res(n,1);
        
        for(int i=0;i<n;i++){
            res[i]*=fromBegin;
            fromBegin*=nums[i];
        }
        //res[0] = 1; fromBegin = 1*1 = 1;
        //res[1] = 1; fromBegin = 1*2 = 2;
        //res[2] = 2; frombegin = 2*3 = 6;
        //res[3] = 6; frombegin = 6*4 = 24;
        //res == [1,1,2,6]
        for(int i=n-1;i>=0;i--)
        {
            res[i]*=fromLast;
            fromLast*=nums[i];
        }
        //i = 3
        //res[3] = 6; fromLast = 1*4 = 4
        //res[2] = 8; fromLast = 4*3 = 12
        //res[1] = 12; fromLast = 12*2 = 24
        //res[0] = 24; fromlast = 24*1 = 24
        //res = 6,8,12,24
        return res;
    }
};