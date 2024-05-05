#include <vector>

using namespace std;

class Solution {
   public:
	int firstMissingPositive(vector<int>& nums) {
		// we need to be able to modify nums, otherwise we can't solve it with
		// constant space to the best of my knowledge. All we do is shuffle the
		// contents
		for (size_t i = 0; i < nums.size(); i++) {
			if (nums[i] > nums.size() || nums[i] <= 0) {
				continue;
			}
			const auto val = nums[i];
			if (nums[val - 1] == val) {
				continue;
			}
			std::swap(nums[val - 1], nums[i]);
			i--;
		}
		for (size_t i = 0; i < nums.size(); i++) {
			if (nums[i] != static_cast<int>(i)) {
				return static_cast<int>(i) + 1;
			}
		}
		return nums.size() + 1;
	}
};