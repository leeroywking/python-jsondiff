import json
import sys

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


def print_message(current, compare, current_path_list):
    delimiter = "]["
    path_str = delimiter.join(str(x) for x in current_path_list)
    print(f"json[{path_str}]")
    print("\033[36m" + f"< {current}", "\033[0m")
    print("\033[95m" + f"> {get_by_path(compare, current_path_list)}" + "\033[0m")
    print("---")
    print("")


def depth_first_search(current, compare, pathlist):
    global string_and_int_count
    global error_count
    global stack

    if isinstance(current, str) or isinstance(current, int):
        try:
            string_and_int_count += 1
            if current == get_by_path(compare, pathlist):
                pass
            else:
                print_message(current, compare, pathlist)

        except:
            print(current_path_list)
            error_count += 1
            if error_count > 5:
                exit()

    elif isinstance(current, list):
        current.reverse()  # so items stack in correct order
        for index, item in enumerate(current):
            current_path_list = pathlist.copy()
            current_path_list.append(len(current) - index -1) # reverse index
            stack.append((item, compare, current_path_list))

    elif isinstance(current, dict):
        for key in reversed(list(current.keys())):  # so they stack properly
            current_path_list = pathlist.copy()
            current_path_list.append(key)
            stack.append((current[key], compare, current_path_list))


stack = []
stack.append((json1, json2, []))

print("")
while len(stack) > 0:
    (item, compare, path_list) = stack.pop()
    current_path_list = path_list.copy()
    depth_first_search(item, compare, current_path_list)


print(f"{error_count} Errors")
print(f"{string_and_int_count} Values checked")
