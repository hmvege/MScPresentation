import re
import os
import shutil

def natural_sort(l):
    """
    Natural sorting function.

    Args:
        l: list of strings where each string contains a number, either on 
            format of 1,2,3... or 00001, 00002 ect.

    Returns:
        A sorted list.
    """

    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split(r'(\d+)', key)]
    return sorted(l, key=alphanum_key)

files = []

for f in os.listdir(os.getcwd()):
	if not "resized" in f.lower(): continue
	if f == "reorder.py": continue
	files.append(f)

files_sorted = natural_sort(files)

print (files_sorted)

for f in files_sorted:
	new_num = int(f.split("-")[-1].split(".")[0])
	f_new = "flowTimeResized_TE21-%02d.png" % new_num 
	shutil.move(f, f_new)
	print ("> mv %s %s" % (f, f_new))
