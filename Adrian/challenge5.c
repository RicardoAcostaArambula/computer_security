#include <stdio.h>
#include <string.h>

#define CORRECT_BUFFER_SIZE 250   
#define CORRECT_BUFFER_LOCATION 0x7fff00000000
#define CORRECT_EBP_LOCATION 0x7fff000007E4

void check_input(unsigned int buffer_size, unsigned long buffer_location, unsigned long ebp_location) {
    unsigned int offset;
    
    // Check if both inputs are correct
    if (buffer_size == CORRECT_BUFFER_SIZE && ebp_location == CORRECT_EBP_LOCATION && buffer_location == CORRECT_BUFFER_LOCATION) {
        // Calculate offset: EBP location - Buffer size
        offset = (unsigned int)(ebp_location - buffer_location + 4);
        
        // Success message with offset
        printf("You have all the tools necessary for your buffer overflow attack!\n");
        printf("The offset value is: %u\n", offset);
        printf("You have completed the House Targaryen Fall 2024 CTF! To end the keylogger, press 'ctrl+q' and contact a member of House Targaryen.\n");
    } else {
        // If incorrect, inform the user
        printf("Incorrect buffer size, buffer location or EBP location. Try again.\n");
    }
}

int main() {
    unsigned int user_buffer_size;
    unsigned long user_buffer_location;
    unsigned long user_ebp_location;
    
    // Prompt for buffer size
    printf("Enter buffer size: ");
    scanf("%u", &user_buffer_size);

    // Prompt for buffer location
    printf("Enter buffer location (e.g., 0x7fffdeadbeef): ");
    scanf("%lx", &user_buffer_location);
    
    // Prompt for EBP location
    printf("Enter EBP location (e.g., 0x7fffdeadbeef): ");
    scanf("%lx", &user_ebp_location);
    
    // Check the inputs
    check_input(user_buffer_size, user_buffer_location, user_ebp_location);
    
    return 0;
}
