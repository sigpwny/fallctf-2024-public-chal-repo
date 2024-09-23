#include <stdio.h>
#include <string.h>

const char* flag = "f \x01 a \x01 l \x01 l \x01 c \x01 t \x01 f \x01 { \x01 f \x01 l \x01 a \x01 g \x01 _ \x01 p \x01 r \x01 i \x01 n \x01 t \x01 e \x01 r \x01 _ \x01 3 \x01 0 \x01 0 \x01 0 \x01 }";
int main() {
    puts("Welcome to the space-printer-3000!\n");
    puts("Our program guarantees at least 50 percent spaces per string!\n");
    puts("Here's a sample of our spaces:\n");
    for (int i = 1; i < strlen(flag); i+=4) {
        printf("%c", flag[i]);
    }
    puts("");
}