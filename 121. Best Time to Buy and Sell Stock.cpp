class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_profit = 0;
        int right = 1;
        int left = 0;
        int n = prices.size();
        while (right < n){
            if(prices[left] < prices[right]){
                int current_profit = prices[right] - prices[left];
                max_profit = max(max_profit,current_profit);
            }
            else{
                left = right;
            }
            right++;
        }
        return max_profit;
    }
};