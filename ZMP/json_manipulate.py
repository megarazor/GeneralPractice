import json

JSON_A= """{
    "locker_5_light": 1,
    "locker_5_unlock": 2,
    "locker_6_light": 1,
    "locker_6_unlock": 1,
    "locker_1_door": 1,
    "locker_1_item": 1,
    "locker_2_door": 1,
    "locker_2_item": 2,
    "locker_5_door": 1,
    "locker_5_item": 5,
    "locker_6_door": 1,
    "locker_6_item": 1,
    "locker_1_light": 0,
    "locker_1_unlock": 1,
    "locker_2_light": 1,
    "locker_2_unlock": 1,
    "locker_3_light": 1,
    "locker_3_unlock": 1,
    "locker_4_light": 1,
    "locker_4_unlock": 1,
    "locker_3_door": 1,
    "locker_3_item":3,
    "locker_4_door": 1,
    "locker_4_item": 0
}
"""
data= json.loads(JSON_A)
new_data= {}

for key in data:
    index= key[7]
    feature= key[9:]
    if index not in new_data:
        new_data[index]= {}
    new_data[index][feature]= data[key]  

JSON_B= json.dumps(new_data, indent=4, sort_keys=True)
print(JSON_B)