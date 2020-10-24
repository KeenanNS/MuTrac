#include <gps.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>
#include <errno.h>

int main(void) {
struct timeval tv;
struct gps_data_t gps_data;
char str[50];

FILE *fp = fopen("gps_data.txt", "w");
if (fp == NULL){
printf("couldn't open file for GPS data");
return EXIT_FAILURE;
}

if ((gps_open("localhost", "2947", &gps_data)) == -1) {
//fflush(stdout);
    sprintf(str, "code: %d, reason: %s\n", errno, gps_errstr(errno));
    printf(str);
fwrite(str, 1, sizeof(str), fp);
    fclose(fp);
    return EXIT_FAILURE;
}
gps_stream(&gps_data, WATCH_ENABLE | WATCH_JSON, NULL);

while (1) {
    /* wait for 2 seconds to receive data */
    if (gps_waiting (&gps_data, 2000000)) {
        /* read data */
        if ((gps_read(&gps_data)) == -1) {
		//fflush(stdout);
	    sprintf(str, "error occured reading gps data. code: %d, reason: %s\n", errno, gps_errstr(errno));
            fwrite(str, 1, sizeof(str), fp);
        } else {
            /* Display data from the GPS receiver. */
            if ((gps_data.status == STATUS_FIX) && 
                (gps_data.fix.mode == MODE_2D || gps_data.fix.mode == MODE_3D) &&
                !isnan(gps_data.fix.latitude) && 
                !isnan(gps_data.fix.longitude)) {
                    //gettimeofday(&tv, NULL); EDIT: tv.tv_sec isn't actually the timestamp!
		//fflush(stdout);
printf(str);	        
sprintf(str, "%f,%f,%f,%lf", gps_data.fix.latitude, gps_data.fix.longitude, gps_data.fix.speed, gps_data.fix.time); 
		fwrite(str, 1, sizeof(str), fp);
            } else {
		//fflush(stdout);
printf(str);		
sprintf(str,"No GPS data available");
                fwrite(str,1,sizeof(str), fp);
            }
        }
    }

    sleep(1);
}

/* When you are done... */
gps_stream(&gps_data, WATCH_DISABLE, NULL);
gps_close (&gps_data);

return EXIT_SUCCESS;
}
