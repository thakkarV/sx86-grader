import xlrd
from collections import OrderedDict
import simplejson as json
import os

# List to hold dictionaries
answer_list = []
# Open the workbook and select the first worksheet
rootdir = ('submissions')
for subdir, dirs, files in os.walk(rootdir):
    files = [f for f in files if not f[0] == '.']
    dirs[:] = [d for d in dirs if not d[0] == '.' or str(d) == rootdirstr]
    # not root
    path = str(subdir)
    if len(path) > 11:
        username = path.split("/")[1].split("_")[0]
        answer = OrderedDict()
        print(username)
        answer['student-id'] = username
        for file in files:
            filestr = str(file)
            fullpath = path + "/" + filestr
            question = filestr.split(".")[0]
            print(question)
            print(fullpath)
            wb = xlrd.open_workbook(fullpath)
            sh = wb.sheet_by_index(0)
            row_values = sh.row_values(1)
            answer[question] = row_values[6]
        # END FILE LOOP
        answer_list.append(answer)
# END DIRECTORY LOOP
# Serialize the list of dicts to JSON
j = json.dumps(answer_list)

# Write to file
with open('data.json', 'w') as f:
    f.write(j)
