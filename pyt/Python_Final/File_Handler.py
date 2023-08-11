import os

########################################################
def print_all_file_names(dirpath):
    list_of_files = []
    item_list = get_dir_content(dirpath)
    for item in item_list:
        if is_this_dir(dirpath + '/' + item,):
            item_list2 = print_all_file_names(dirpath + '/' + item)
            list_of_files.append(item_list2)
        else:
            list_of_files.append(item)
    print(list_of_files)

#########################################################

def get_dir_content(dirpath):
    content = os.listdir(dirpath)
    return content

def is_this_dir(dirpath):
    return os.path.isdir(dirpath)

print_all_file_names('/home/alex/pyt')





######################################################################

# file_path=[]
# def scan_all_files(files_dir):
#     for file in os.listdir(files_dir):
        
#         return(file)


# file_size=[]

# def get_file_size(files_list):
#     for size in os.stat(files_list):
#         file_size.append(size)
#     return(file_size)



# files_dir2 = '/home/alex/pyt'

# files_list = scan_all_files(files_dir2)
# print(files_list)



    

