import json

# Reads in the file as JSON.
# Pulls out the following four fields:
#  name
#  html_url
#  updated_at
#  visibility
# Assembles these four fields into a comma-separated line.
# Appends this line to a new text file named chacon.csv
# LIMIT the output to 5 lines only. Do not parse all 30 lines into the new CSV file.

#open data source file
with open('../../data/schacon.repos.json', 'r') as file:
    data = json.load(file)

#create new file for data output
file2 = open('../../data/chacon.csv', "w")

#iterate through data, stop after 5 times
n = 0
for item in data:
    if n >= 5:
        break
    file2.write( item["name"] + ',' + item["html_url"] + ',' + item["updated_at"] + ',' + item["visibility"] + '\n')

    n += 1


file2.close()

