class Solution {
public:
    bool checkDivisibility(int n) {
        int s=0;
        int p=1;
        int on=n;
        while(n>0){
            int r=n%10;
            s+=r;
            p*=r;
            n=(int)(n/10);
        }
        if (on%(s+p)==0){
            return true;
        }else{
            return false;
        }
    }
};