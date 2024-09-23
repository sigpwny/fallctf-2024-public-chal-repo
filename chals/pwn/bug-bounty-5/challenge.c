#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

void setup();
void print_stack(char *name_addr, char *info_addr);
                                   

const char *pwn5 = "\n"
" _______   __       __  __    __        _______  \n"
"|       \\ |  \\  _  |  \\|  \\  |  \\      |       \\ \n"
"| $$$$$$$\\| $$ / \\ | $$| $$\\ | $$      | $$$$$$$\\\n"
"| $$__/ $$| $$/  $\\| $$| $$$\\| $$      | $$____  \n"
"| $$    $$| $$  $$$\\ $$| $$$$\\ $$      | $$    \\ \n"
"| $$$$$$$ | $$ $$\\$$\\$$| $$\\$$ $$       \\$$$$$$$\\\n"
"| $$      | $$$$  \\$$$$| $$ \\$$$$      |  \\__| $$\n"
"| $$      | $$$    \\$$$| $$  \\$$$       \\$$    $$\n"
" \\$$       \\$$      \\$$ \\$$   \\$$        \\$$$$$$ \n";




void vuln() {
    char info[32];
    char name[32];

    printf("What's your name?\n");
    printf("> ");

    fgets(name, 32, stdin);
    printf("Hello, ");
    printf(name); // there's a vulnerability here
    printf("\n");

    puts("Give me all your personal information (credit card number, SSN, all of it):");
    printf("> ");
    fgets(info, 64, stdin);

    puts("Here's what the stack looks like after your input:");
    print_stack(name, info);
}

int main() {
    setup();
    puts(pwn5);
    vuln();
    return 0;                                                            
}





/**
* You can ignore everything below this
*/

// Just to make things work over the network
void setup() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
}

// Creates a visual representation of the stack
void print_stack(char *name_addr, char *info_addr) {
    // get return address of previous frame
    char **rbp;
    __asm__("movq %%rbp, %0" : "=r"(rbp));
    char *prev_rbp = *rbp;
    char *return_addr = prev_rbp + 8;

    uint64_t *stack = (uint64_t *)name_addr;
    printf("\n");
    puts("----------------------------------------------------------------");
    for (int i = 0; i < 10; i++) {
        
        printf("|   %p: ", &stack[i]);
        for (int j = 0; j < 8; j++) {
            printf("%02hhx ", ((char *)&stack[i])[j]);
        }
      
        if ((char *)&stack[i] == name_addr) {
            printf("%-18s", "<-- name");
        } else if ((char *)&stack[i] == info_addr) {
            printf("%-18s", "<-- info");
        } else if ((char *)&stack[i] == return_addr) {
            printf("%-18s", "<-- return address");
        } else {
            printf("%18s", "");
        }

        printf(" |\n");
    }
    puts("----------------------------------------------------------------");
    printf("\n");
}