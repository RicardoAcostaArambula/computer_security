#include <stdio.h>
#include <string.h>

struct Account {
    char username[20];
    char password[20];
};

void displayAccounts(struct Account accounts[], int size) {
    printf("\nDisplaying Accounts and Passwords:\n");
    for (int i = 0; i < size; i++) {
        printf("Username: %s, Password: %s\n", accounts[i].username, accounts[i].password);
    }
}

int main() {
    struct Account accounts[3] = {
        {"admin", "admin123"},
        {"user1", "pass1"},
        {"user2", "pass2"}
    };
    
    char inputPassword[20];
    
    printf("Enter the admin password: ");
    fgets(inputPassword, sizeof(inputPassword), stdin);  
    inputPassword[strcspn(inputPassword, "\n")] = 0;

    if (strcmp(inputPassword, "admin123") == 0) {
        printf("\nAccess Granted!\n");
        displayAccounts(accounts, 3);
    } else {
        printf("\nAccess Denied!\n");
    }

    return 0;
}
