#include <iostream>

using namespace std;

float getAngle(int hour, int minute){
    float min_angle= float(minute) / 60 * 360;
    if (hour >= 12){
        hour= hour - 12;
    }        
    float hour_angle= float(hour) / 12 * 360 + min_angle / 12;
    float angle= min_angle - hour_angle;
    
    if (angle < 0){
        return angle * -1;
    }
    return angle;
}

int main() {
    printf("00:15 -> %f\n", getAngle(0, 15));
    printf("01:59 -> %f\n", getAngle(1, 59));
    printf("07:26 -> %f\n", getAngle(7, 26));
    printf("19:19 -> %f\n", getAngle(19, 19));
    printf("22:07 -> %f\n", getAngle(22, 7));
    printf("11:00 -> %f\n", getAngle(11, 00));
    printf("14:30 -> %f\n", getAngle(14, 30));
    return 0;
}