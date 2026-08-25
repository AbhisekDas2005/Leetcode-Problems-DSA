class Solution {
    public int missingMultiple(int[] nums, int k) {
        int c=1;
        while(true){
            boolean flag=false;
            for(int i=0;i<nums.length;i++){
                if (nums[i]==c*k){
                    flag=true;
                    break;
                }
            }
            if(!flag){
                return c*k;
            }else{
                c+=1;
            }
        }
    }
}