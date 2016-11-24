import zipfile
import sys
import shutil
import json
import string

def find_strings(data, minimum_length, maximum_length):
	printable = list(map(ord, set(string.printable)))
	found_str = ""
	found = []
	for char in data:
		if char in printable:
			found_str += chr(char)
		elif (len(found_str) >= minimum_length and
			  len(found_str) <= maximum_length):
			found.append(found_str)
			found_str = ""
		else:
			found_str = ""
	return found
	
def unzip(file, target):
	with zipfile.ZipFile(file,"r") as zip_ref:
		zip_ref.extractall(target)
	

def find_secrets(lib, minimum_length, maximum_length):
	dump_data = {}
	with open(lib,"rb") as lib_ref:
		data = lib_ref.read()
		strings = find_strings(data, minimum_length, maximum_length)
		secrets = list(filter(lambda x: x[0].isalpha(), strings))
		dump_data["strings"] = secrets
	return dump_data
	
	
def save_json(data, path):
	with open(path,"w") as dump_ref:
		json.dump(data, dump_ref)
		
def delete_dir(dir):
	shutil.rmtree(dir)


if len(sys.argv) <= 3:
	print("Usage: python3 " + sys.argv[0] + " <filename.apk> <libname.so> <minimum length> <maximum length>")
	exit()

file = sys.argv[1]
lib_name = sys.argv[2]
minimum_length = int(sys.argv[3])
maximum_length = int(sys.argv[4:] or sys.argv[3])
target = "unzip"
lib_location = "/lib/armeabi-v7a/" + lib_name
dump = "dump.json"

full_lib_path = target + lib_location

unzip(file, target)
strings = find_secrets(full_lib_path, minimum_length, maximum_length)
save_json(strings, dump)
delete_dir(target)
	