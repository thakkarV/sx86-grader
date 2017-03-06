# sx86-grader

1. Un-zip multiple .zip files into separte folders:

```bash
for zipfile in *.zip; do
    exdir="${zipfile%.zip}"
    mkdir "$exdir"
    unzip -d "$exdir" "$zipfile"
done
```  
  The result should be each student has a studentID_HW1 folder containing Q1.xlsx, Q2.xlsx, Q3.xlsx and Q4.xlsx.

2. Update main.py rootdir to be the folder of folders

3. run in terminal:
```bash
python main.py
```

4. format data.json
add single quote and remove trailing whitespace
```json
var data = '[{"studentID": "sample1", "Q1": "903F50005000500050005000B0000000", "Q2": "900A904F908490C3B002B043900A904F9100C080C0C15082510351035103B002B0440000", "Q3": "90049043908690C29101B1001004B1011004B1021004B10390019042908390C4C000C041C082C0C3A10091418045403A50041005203560835002905EB0400000", "Q4": "901B9043B0409003C000904790808002403C90818002403C90828002403C90828002403C90848002403C90858002403C90868002403C6001202590D6B0C00000"}, {"studentID": "sample2", "Q1": "9000904090a090ff5003100180423023b0000000", "Q2": "90019042908a90cfb080b0c1c002c043910091425000b080500110048105302bb0c00000", "Q3": "90019042b00190029045b00190039047b00190049041b0019101c0049142c045908090c050c01002808130319103c0049144c045600150c0901eb0030000", "Q4": "900b9043b0409043c001908790d690408040403d90418040403d90428040403d90438040403d90448040403d90458040403d90468040403d60022026b0c10000"}]'
```

open index.html

finalResults JSON

https://json-csv.com/

to do
validate input better -- no submission
remove globals, modularize