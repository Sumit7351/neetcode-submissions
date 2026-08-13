class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        /*sort(nums.begin(),nums.end());
        int l=0,r=l+1;
        while(r<nums.size()){
            if(nums[l]==nums[r]){
                return true;
            }
            l++;
            r++;
        }
        if(r==nums.size())
        return false;*/
        unordered_map<int,int> mp;
        for(int num:nums){
            if(mp[num]=>1) return true;
            mp[num]++;
    }
    return false;
    }
};