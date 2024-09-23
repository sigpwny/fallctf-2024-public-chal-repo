#include <stdio.h>
#include <string.h>
const int seq1[] = {179, 79, 225, 210, 147, 107, 119, 181, 181, 33, 78, 240, 238, 64, 185, 7, 71, 219, 86, 165, 21, 34, 117, 19, 26, 194, 152, 136, 109, 56, 208, 210, 175, 142};
const int seq3[] = {1, 1, 2, 3, 2, 3, 1, 4, 4, 1, 4, 4, 1, 2, 3, 2, 3, 3, 4, 4, 2, 4, 3, 1, 1, 3, 4, 4, 3, 4, 2, 4, 2, 4};
const int seq4[] = {3408, 716, 432, 308, 2256, 920, 768, 1424, 352, 370, 448, 1672, 2224, 56, 3472, 2496, 1536, 1480, 448, 912, 984, 206, 3152, 608, 450, 3392, 272, 104, 368, 792, 240, 668, 50, 350};

int main() {
    puts("welcome to another generic flag checker (TM)!\n");
    char user_input[1024];
    fgets(user_input, 1024, stdin);
    user_input[strcspn(user_input, "\n")] = 0;
    if (strlen(user_input) != 34) {
        printf("Silly intern, clearly that's not the right length flag (length %lu).\n", strlen(user_input));
        return 1;
    }

    int bad = 0;
    for (int i = 0; i < 34; i++) {
        if (((seq4[i] >> seq3[33 - i]) ^ seq1[(3 * i) % 34]) != user_input[i]) {
	    bad = 1;
        }
    }
    if (bad) {
	    puts("Silly intern, that's not the right flag.");
	    return 1;
    }
    puts("Good job! You found the flag!");
}
