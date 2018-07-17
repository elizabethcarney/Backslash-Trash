#SheHacks: Backslash Trash
#This code cleans up the data file into readable Javascript

import json

review_json = '/Users/Elizabeth/Desktop/shehacks/big-belly.json'


def extract_lat_and_long():
    global all_coordinates
    all_coordinates = open(review_json, encoding = 'utf8').readlines()
    file = open('locations.js', 'w')
    file.write('var locations = [')
    for line in all_coordinates:
        line = line[:-2]
        x = json.loads(line)
        loc = x['Location']
        loc = '[' + loc[1:-1] + '],' + '\n'
        file.write(loc)
        print(loc)
    file.write('];')
    file.close()

    return all_coordinates
    
extract_lat_and_long()
