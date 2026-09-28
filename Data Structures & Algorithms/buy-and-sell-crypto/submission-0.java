class Solution {
    public int maxProfit(int[] prices) {
        int maxPrice = 0;
        int minBuy = prices[0];
        for(int i = 0; i < prices.length; i++){
            if (maxPrice < prices[i] - minBuy){
                maxPrice = (prices[i] - minBuy);
            }

            if (minBuy > prices[i]){
                minBuy = prices[i];
            }
        }

        return maxPrice;
    }
}
