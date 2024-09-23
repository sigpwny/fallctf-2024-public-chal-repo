#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

void add_item();
void remove_item();
void view_cart();
void settings();
void info();
void admin_console();

static char *cart[] = {NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL};
const int CART_SIZE = 10;
static char *items[] = {"Milk", "Eggs", "Rice", "Beans", "Chicken", "Ice Cream", "Bottled Water", "Cheese", "Bread", "Pasta"};
const int ITEMS_SIZE = 10;
static void (*operations[])() = {add_item, remove_item, view_cart, settings, info}; // PwnyMart will support more operations in the future
const int OPERATIONS_SIZE = 5;

void add_item() {
    printf("What position do you want to add the item to?\n");
    printf("> ");
    unsigned int position;
    scanf("%d", &position);
    if (position < 0 || position >= CART_SIZE || cart[position] != NULL) {
        printf("Can't add at this position\n");
        return;
    }
    printf("What is the index of the item you want to add?\n");
    printf("> ");
    unsigned int item_index;
    scanf("%d", &item_index);
    if (item_index < 0 || item_index >= ITEMS_SIZE) {
        printf("Can't add item at this index\n");
        return;
    }
    cart[position] = items[item_index];
}


void remove_item() {
    puts("What position do you want to remove the item from?");
    printf("> ");
    unsigned int position;
    scanf("%d", &position);
    if (position < 0 || position >= CART_SIZE || cart[position] == NULL) {
        printf("Can't remove from this position\n");
        return;
    }
    cart[position] = NULL;
}

void view_cart() {
    printf("Here's the cart: \n");
    printf("> ");
    for (int i = 0; i < CART_SIZE; i++) {
        printf("%d: ", i);
        if (cart[i] != NULL) {
            printf("%s\n", cart[i]);
        } else {
            printf("%s\n", "Empty");
        }
    }

}

void settings() {
    puts("What do you want to do?");
    puts("0: Remove Operation");
    puts("1: Add Operation");
    printf("> ");
    int option;
    scanf("%d", &option);
    if (option == 0) {
        puts("Which operation do you want to remove?");
        printf("> ");
        int index;
        scanf("%d", &index);
        if (index < 0 || index > OPERATIONS_SIZE) {
            puts("Bad index");
            return;
        }
        operations[index] = NULL;
    } else if (option == 1) {
        puts("What position do you want to add the new operation to?");
        printf("> ");
        int index;
        scanf("%d", &index);
        if (index < 0 || index > OPERATIONS_SIZE || operations[index] != NULL) {
            puts("Bad index");
            return;
        }
        unsigned long op;
        printf("> ");
        scanf("%lx", &op);
        operations[index] = op;
    }
}

void info() {
    printf("How much info do you want?\n0: A little\n1: A lot\n");
    printf("> ");
    unsigned int info_level;
    scanf("%d", &info_level);
    if (!(info_level == 0 || info_level == 1)) {
        printf("Info level must be 0 or 1\n");
    }
    if (info_level == 0) {
        printf("Operations\n");
        puts("Code: 0, Operation: add item to cart");
        puts("Code: 1, Operation: remove item from cart");
        puts("Code: 2, Operation: view cart");
        puts("Code: 3: Operation: settings");
        puts("Code: 4: Operation: info");
        puts("Admin operation: admin console");
    } else if (info_level == 1) {
        printf("Operations\n");
        printf("Code: 0, Operation: add item to cart, Address: %p\n", operations[0]);
        printf("Code: 1, Operation: remove item from cart, Address: %p\n", operations[1]);
        printf("Code: 2, Operation: view cart, Address: %p\n", operations[2]);
        printf("Code: 3: Operation: settings, Address: %p\n", operations[3]);
        printf("Code: 4: Operation: info, Address: %p\n", operations[4]);
        printf("Admin operation: admin console, Address: %p\n", admin_console);
    }
}

void admin_console() {
    puts("Welcome to the PwnyMart admin console!");
    execve("/bin/sh", NULL, NULL);
}

void setup() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
}

int main() {
    setup();
    while(1) {
        puts("Welcome to PwnyMart! Which operation do you want to do (enter 4 for more info and -1 to exit)?");
        printf("> ");
        int option;
        scanf("%d", &option);
        if (option == -1) {
            puts("Thank you for visiting PwnyMart");
            exit(0);
        }
        if (option < 0 || option > 4) {
            puts("Hacker Detected!!!");
            exit(1);
        }
        operations[option]();
    }
    return 0;
}
