import sys
import os
from time import sleep
import pickle

actual_dir = os.getcwd()
opsys = sys.platform

if opsys in ["linux", "darwin"]:
	os.chdir("/home")
	print(opsys)
elif opsys == "win32":
	os.chdir("c:\\")
	print(opsys)
else:
	print(f"Warning: Listing may start in the current directory instead of the home directory in {opsys}.")


dirs_files = list(os.walk(os.getcwd()))

with open(f"{actual_dir}/my_dirs.pkl" , "wb") as f:
	pickle.dump(dirs_files, f)

