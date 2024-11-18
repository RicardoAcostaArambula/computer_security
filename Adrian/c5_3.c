#include <stdio.h>
#include <string.h>

void Saruman(){
    printf("Y0u 4r3 f00l15h t0 h4v3 c0m3 h3r3 s33k1n9 th3 4ddr355.");
    char army[3][4] = {
        "orc",
        "orc",
        "orc"
    };
}
void Radagast(){
    const char *animals[] = {
        "Hedgehog",
        "Rabbit",
        "Bear",
        "Bird",
        "Squirrel"
    };
    int numAnimals = sizeof(animals) / sizeof(animals[0]);
    printf("H3r3 4r3 4ll my fr13nd5:\n");
    for (int i = 0; i < numAnimals; i++) {
        printf("%s\n", animals[i]);
    }
}
void Gandalf(){
    printf("4 w1z4rd 15 n3v3r l4t3, or 34rly, h3 4rr1v35 pr3c1c3ly 4t th3 8uff3r 4ddr355");
    char bufferAddress[] = "0x7fff00000000";
}

int main(){
    printf("G4nd4lf, y35, th4t 15 wh4t th3y u53d t0 c4ll m3...");
    //CH3CK TH3 P4TH5
    Gandalf();
    Saruman();
    Radagast();
    return 0;
}