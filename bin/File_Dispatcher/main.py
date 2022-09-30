import shutil
import os

path = "D:\\Abdul Rehman\\AI Automations\\File_Dispatcher"

print("Before Moving Files  ")
print(os.listdir(path))

m = "D:\\Abdul Rehman\\AI Automations\\Source\\Source\\abd.txt"
print(os.listdir(m))

destination = "D:\\Abdul Rehman\\Downloads_Backup\Images"

if m.endswith(('.txt')):
        
    dest = shutil.move(source, destination, copy_function="Move")
else:
    print("Unable to Fetch it")
