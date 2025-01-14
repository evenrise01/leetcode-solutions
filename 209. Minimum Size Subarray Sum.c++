class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int n = nums.size();
        int length = INT_MAX; //Set length to max infinity
        int current_sum = 0;
        int start = 0;

        for (int end = 0; end < n; end++){
            current_sum += nums[end]; //Calculate current sum while traversing the array

            //If current_sum >= target, check the current length of the window, subtract the leftmost element and shrink the window from left side
            while(current_sum >= target){
                length = min(length, end-start+1);
                current_sum-=nums[start];
                start++;
            }
        }
        //At the end check if the length is still infinity, if yes return 0 - meaning we didn't find any subarrays
        if(length == INT_MAX){
                return 0;
            }
            //if there is any other value of length than infinity, return that value
        else return length;
    }
};