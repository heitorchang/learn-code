Create a new C file, code.c

gcc -o code.o code.c
./code.o


#include <stdio.h>

int main() {
    int bottles = 99;
    printf("%d bottles on the wall", bottles);
    
    return 0;
}
    
