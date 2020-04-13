import json
import sys

with open("./simple.json") as file1:
    json_simple = json.load(file1)

with open(sys.argv[1]) as file1:
    json1 = json.load(file1)

with open(sys.argv[2]) as file2:
    json2 = json.load(file2)

string_and_int_count = 0
error_count = 0


def get_by_path(dict_to_check, list_of_keys):
    try:
        for k in list_of_keys:
            dict_to_check = dict_to_check[k]
        return dict_to_check
    except:
        return "ERROR: Value is undefined"


def depth_first_search(current, compare, pathlist=[]):
    global string_and_int_count
    global error_count
    current_path_list = pathlist.copy()
    if isinstance(current, str) or isinstance(current, int):
        try:
            string_and_int_count += 1
            if current == get_by_path(compare, pathlist):
                pathlist.pop()
            else:
                delimiter = "]["
                fancy_str = delimiter.join(str(x) for x in pathlist)
                print(f"json[{fancy_str}]")
                print("\033[36m" + f"< {current}", "\033[0m")
                print("\033[95m" + f"> {get_by_path(compare, pathlist)}" + "\033[0m")
                print("---")
                print("")
                pathlist.pop()
        except:
            print(pathlist)
            pathlist.pop()
            error_count += 1
            if error_count > 5:
                exit()

    elif isinstance(current, list):
        for index, item in enumerate(current):
            current_path_list.append(index)
            depth_first_search(item, compare, current_path_list)
        if len(pathlist) > 0:
            pathlist.pop()

    elif isinstance(current, dict):
        for key in current:
            current_path_list.append(key)
            depth_first_search(current[key], compare, current_path_list)
        if len(pathlist) > 0:
            pathlist.pop()


depth_first_search(json1, json2)
print(f"{error_count} Errors")
print(f"{string_and_int_count} Values checked")
