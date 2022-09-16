class Solution {
    public int[] twoSum(int[] nums, int target) {
         HashMap<Integer,Integer> hMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            Integer rem = (Integer) target - nums[i];
            if(hMap.containsKey(rem))
            {
                int[] list = {hMap.get(rem),i};
                return list;
            }
            hMap.put(nums[i],i);
        }
        return null;
    }
}
