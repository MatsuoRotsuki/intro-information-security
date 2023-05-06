#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int random(int minN, int maxN){// Ham random t?o 2 bit 0 ,1 
    return minN + rand() % (maxN + 1 - minN);
}
int main(){
    srand((int)time(0));
    int A[93];// thanh ghi A
    int B[84];// thanh ghi B
    int C[111];// thanh ghi C
    int keybd[80];
    int afront,anext,bfront,bnext,cfront,cnext;// gi?i thich trong hinh ?nh ?inh kem
    int i;
    for (i=0;i<80;i++){// Sinh IV ng?u nhien 
        A[i] = random(0,1);
    }
    for (i=80;i<93;i++){
        A[i]=0;
    }
    for (i=0;i<80;i++){// Sinh khoa k( gi? s? c?ng la ng?u nhien,ta l?u tr? khoa k sinh ng?u nhien nay vao chu?i keybd)
        B[i] = random(0,1); 
        keybd[i]= B[i];       
    }
    for (i=80;i<84;i++){
        B[i]=0;
    }
    for (i=0;i<108;i++){// Sinh bit thanh ghi C
        C[i]=0;
    }
    C[108]=C[109]=C[110]=1;
    int S[80];// key stream sau khi ma hoa
    int k;
    for (k=0;k<80;k++){
        S[k]=2;
    }
    for (k=0;k<80;k++){// ham ma hoa (Nh? trong s? ?? trivium)
        afront=(A[90] & A[91])^A[92]^A[65];
        bfront=(B[81] & B[82])^B[83]^B[68];
        cfront=(C[108] & C[109])^C[110]^C[65];
        S[k]= afront ^ bfront ^ cfront;
        anext=cfront^A[68];
        bnext=afront^B[77];
        cnext=bfront^C[86];
        for (i=92;i>=1;i--){//m?i khi x? ly xong cac bit nh? tren s? ??, ta s? d?ch ph?i m?i bit 1 ??n v?, c? nh? th? h?t 80 l?n ?? ra key stream
            A[i]=A[i-1];
        }
        A[0]=anext;
        for (i=83;i>=1;i--){
            B[i]=B[i-1];
        }
        B[0]=bnext;
        for (i=110;i>=1;i--){
            C[i]=C[i-1];
        }
        C[0]=cnext;
    }
    for (k=0;k<80;k++){ // In ra khoa k tr??c khi ma hoa
        printf("%d ",keybd[k]);
    }
    printf("\n");
    for (k=0;k<80;k++){// In ra khoa k sau khi ma hoa
        printf("%d ",S[k]);
    }
    return 0;
}
