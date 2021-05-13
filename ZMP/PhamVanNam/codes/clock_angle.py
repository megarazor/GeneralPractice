def get_angle(hour, minute): # hour: 0~23, minute: 0~59
    min_angle= minute / 60 * 360
    if hour >= 12:
        hour= hour - 12
    hour_angle= hour / 12 * 360 + min_angle / 12
    angle= min_angle - hour_angle
    if angle < 0:
        return angle * -1
    return angle

print("00:15 ->", get_angle(0, 15))
print("01:59 ->", get_angle(1, 59))
print("07:26 ->", get_angle(7, 26))
print("19:19 ->", get_angle(19, 19))
print("22:07 ->", get_angle(22, 7))
print("11:00 ->", get_angle(11, 00))
print("14:30 ->", get_angle(14, 30))