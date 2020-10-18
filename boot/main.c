#include <stdlib.h>
#include <stdio.h>
#include <wiringPi.h>
#include <unistd.h>
int main(void){

int i;
char buffer[45];
char buffertwo[20];
//system("mkdir /home/pi/MuTrac/boot/69_haha");

while(1){
i++;
//FILE *fptr;
//fptr = fopen("testdata", "a+");
//snprintf(buffertwo, sizeof(buffertwo), "The iteration %d\n", i);
//printf("hello world");
//fseek(fptr, sizeof(buffertwo), SEEK_SET);
//fwrite(buffertwo , 1 , sizeof(buffertwo) , fptr );
//fclose(fptr);

snprintf(buffer, sizeof(buffer), "/home/pi/codes/test/printNumbers %d", i);
//snprintf(buffer, sizeof(buffer), "mkdir /home/pi/boot/dir%d", i);
system(buffer);
sleep(1);
}
return 0;
}
