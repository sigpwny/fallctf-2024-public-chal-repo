#include <stdlib.h>
#include <stdio.h>

int main() {
    unsigned int nums[] = {1804289281, 846930855, 1681692677, 1714636831, 1957747762, 424238219, 719885356, 1649760407, 596516677, 1189641384, 1025202391, 1350490054, 783368599, 1102519972, 2044897665, 1967513897, 1365180430, 1540383408, 304089147, 1303455631, 35005252, 521595293, 294702485, 1726956498, 336465691, 861021499, 278722887, 233665037, 2145174101, 468703213, 1101513896, 1801979895, 1315633923, 635723117, 1369133183, 1125898194, 1059961424, 2089018420, 628175100, 1656477995, 1131176272, 1653377332, 859484518, 1914545020, 608413733};
    for (int i=0;i<45;i++) {
        printf("%c", nums[i] ^ rand());
    }
    printf("\n");
}