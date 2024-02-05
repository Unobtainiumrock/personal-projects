import os

def print_dir_tree(startpath):
    # First, print the files that are in the same directory as the script.
    print("project_root/")
    print("|")
    # Now, handle all directories and files within them.
    for root, dirs, files in os.walk(startpath, topdown=True):
        if root == startpath:
            continue  # We already handled files in the root directory
        
        level = root.replace(startpath, '').count(os.sep)
        indent = '|   ' * level
        base_name = os.path.basename(root)
        
        print(f'{indent}|── {base_name}/')
        
        subindent = '|   ' * (level + 1)
        dirs.sort()
        files.sort()
        
        # Process files within subdirectories.
        for i, f in enumerate(files):
            print(f"{subindent}|── {f}")
        
        if dirs:
            print(subindent)

    
    files_in_root = [f for f in os.listdir(startpath) if os.path.isfile(os.path.join(startpath, f))]
    files_in_root.sort()  # Sort the files in root for a consistent order
    
    # print(f'{os.path.basename(startpath)}/')
    
    for f in range(len(files_in_root)):
        if not f == len(files_in_root) - 1:
            print(f'|── {files_in_root[f]}')
        else:
           print(f'└──  {files_in_root[f]}') 

# Start from the current directory
print_dir_tree('.')
