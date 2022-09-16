class Solution {
    public int removeElement(int[] nums, int val) {
        int idx = 1;
        for(int x = nums.length - 1; x >= 0; x--){
            if(nums[x] == val){
                int hold = nums[nums.length - idx];
                nums[nums.length - idx] = val;
                nums[x] = hold;
                idx++;
            }
        }
        return nums.length - (idx - 1);
    }
}