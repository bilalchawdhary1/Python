# 10/29/24 today python learning 
# 1: pip it's ue to indstall pakages 
# 2: how to create python file 
# 3: how to run  


print("hello world")
print(48*3)

# Check if the current directory exists
import os
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# Check if a file exists in the current directory
file_name = "example.txt"
file_exists = os.path.isfile(file_name)
print(f"{file_name} exists: {file_exists}")

# Create a new directory
new_dir_name = "new_directory"
os.makedirs(new_dir_name, exist_ok=True)
print(f"Directory '{new_dir_name}' created.")

# List all files in the current directory
files = os.listdir()
print("Files in the current directory:")
for file in files:
    print(file)