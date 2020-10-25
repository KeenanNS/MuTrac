
#include <gps.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <math.h>
#include <errno.h>

int main() {
struct timeval tv;
struct gps_data_t gps_data;
FILE * fp = fopen("/home/pi/MuTrac/GPS/gps_data.txt","w+");
if (!fp){
	printf("bad file open");
	fclose(fp);
	return EXIT_FAILURE;
}

if ((gps_open("localhost", "2947", &gps_data)) == -1) {
    printf("code: %d, reason: %s\n", errno, gps_errstr(errno));
    return EXIT_FAILURE;
}
gps_stream(&gps_data, WATCH_ENABLE | WATCH_JSON, NULL);

while (1) {
	FILE * fp = fopen("/home/pi/MuTrac/GPS/gps_data.txt","w+");
    /* wait for 2 seconds to receive data */
    if (gps_waiting (&gps_data, 2000000)) {
        /* read data */
        if ((gps_read(&gps_data)) == -1) {
            printf("error occured reading gps data. code: %d, reason: %s\n", errno, gps_errstr(errno));
        } else {
            /* Display data from the GPS receiver. */
            if ((gps_data.status == STATUS_FIX) && 
                (gps_data.fix.mode == MODE_2D || gps_data.fix.mode == MODE_3D) &&
                !isnan(gps_data.fix.latitude) && 
                !isnan(gps_data.fix.longitude)) {
                    //gettimeofday(&tv, NULL); EDIT: tv.tv_sec isn't actually the timestamp!
                    fprintf(fp,"%f,%f,%f\n", gps_data.fix.latitude, gps_data.fix.longitude, gps_data.fix.speed); //EDIT: Replaced tv.tv_sec with gps_data.fix.time
            } else {
                printf("no GPS data available\n");
            }
        }
    }
    fclose(fp);

    sleep(1);
}

/* When you are done... */
gps_stream(&gps_data, WATCH_DISABLE, NULL);
gps_close (&gps_data);

return EXIT_SUCCESS;
}

