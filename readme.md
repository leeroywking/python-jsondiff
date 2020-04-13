This is a one file json diff tool with no required tools to download or install.

usage if file is installed in same directory

`python3 json_diff.py json1.json json2.json`

desired output should show clearly what differences are present between each json file.

example
JSONfile1[0]["isactive]: False
JSONfile2[0]["isactive]: True

JSONfile1[2]["friends"][5]["friends"][79]["name"]: Mildred Fulton
JSONfile2[2]["friends"][5]["friends"][79]["name"]: Mildred Falton

JSONfile1[0]["zanzibar"]: defined
JSONfile2[0]["zanzibar"]: undefined
