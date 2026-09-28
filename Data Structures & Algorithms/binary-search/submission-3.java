class Solution {
    public int search(int[] nums, int target) {
        // Base case: if the array is empty, return -1 (target not found)
        if (nums.length == 0) {
            return -1;
        }

        return searchHelper(nums, target, 0, nums.length - 1);
    }

    private int searchHelper(int[] nums, int target, int left, int right) {
        if (left > right) {
            return -1;  // Target not found
        }

        int mid = left + (right - left) / 2;

        if (nums[mid] == target) {
            return mid;  // Found the target
        }

        if (nums[mid] < target) {
            return searchHelper(nums, target, mid + 1, right);  // Search in the right half
        } else {
            return searchHelper(nums, target, left, mid - 1);  // Search in the left half
        }
    }
}
