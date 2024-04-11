import java.util.Arrays;
import java.util.Comparator;

class Solution {
    static class Pair {
        int value;
        int index;

        public Pair(int value, int index) {
            this.value = value;
            this.index = index;
        }
    }

    public int[] twoSum(int[] nums, int target) {
        // Create an array of pairs containing the value and its original index
        Pair[] pairs = new Pair[nums.length];
        for (int i = 0; i < nums.length; i++) {
            pairs[i] = new Pair(nums[i], i);
        }

        // Sort the pairs array based on the values
        Arrays.sort(pairs, Comparator.comparingInt(p -> p.value));

        // Initialize two pointers: one at the beginning and one at the end
        int left = 0;
        int right = nums.length - 1;

        // Iterate until the pointers meet
        while (left < right) {
            int sum = pairs[left].value + pairs[right].value;
            if (sum == target) {
                // If the sum matches the target, return the original indices of the elements
                return new int[]{pairs[left].index, pairs[right].index};
            } else if (sum < target) {
                // If the sum is less than the target, move the left pointer to the right
                left++;
            } else {
                // If the sum is greater than the target, move the right pointer to the left
                right--;
            }
        }

        // If no solution is found, return an empty array
        throw new IllegalArgumentException("No two sum solution");
    }

    public static void main(String[] args) {
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        Solution solution = new Solution();
        int[] result = solution.twoSum(nums, target);
        System.out.println("Output: [" + result[0] + ", " + result[1] + "]");
    }
}
    
