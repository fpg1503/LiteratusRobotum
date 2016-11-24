import zipfile
import sys
import shutil
import json
import string
from argparse import ArgumentParser
from argparse import RawTextHelpFormatter

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
		secrets = list(filter(lambda x: x[0].isalnum(), strings))
		dump_data["strings"] = secrets
	return dump_data
	
	
def save_json(data, path):
	with open(path,"w") as dump_ref:
		json.dump(data, dump_ref)
		
def delete_dir(dir):
	shutil.rmtree(dir)


parser = ArgumentParser(formatter_class=RawTextHelpFormatter)
parser.add_argument("-f", "--file", dest="file",
			help="your APK file", metavar="FILE")
parser.add_argument("-l", "--lib-name", dest="lib_name",
			help="the name of the library")
parser.add_argument("-s", "--size", dest="length",
			type=int, nargs='+',
			help="length of the strings to be found\nusage: [-s LENGTH] or [-s MININUM_LENGTH MAXIMUM_LENGTH]")
			
args = parser.parse_args()
file = args.file
lib_name = args.lib_name
minimum_length = args.length[0]
maximum_length = args.length[1] if len(args.length) > 1 else args.length[0]

target = "unzip"
lib_location = "/lib/armeabi-v7a/" + lib_name
dump = "dump.json"

full_lib_path = target + lib_location

unzip(file, target)
strings = find_secrets(full_lib_path, minimum_length, maximum_length)
save_json(strings, dump)
delete_dir(target)
	