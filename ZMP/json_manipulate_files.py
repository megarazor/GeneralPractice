import json
import time

start_time = time.time()

for i in range(0, 10):
    with open('json_data/' + str(i) + '.json') as json_file:
        data = json.load(json_file)

        new_data= {}

        for key in data:
            index= key[7]
            feature= key[9:]
            if index not in new_data:
                new_data[index]= {}
            new_data[index][feature]= data[key]  

        JSON_B= json.dumps(new_data, indent=4, sort_keys=True)
        # print(JSON_B)
        with open('json_data_converted/' + str(i) + '.json', 'w') as outfile:
            json.dump(new_data, outfile, indent=4, sort_keys=True)


print("--- %s seconds ---" % (time.time() - start_time))