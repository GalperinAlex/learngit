import os


##################################################

def print_all_file_names(dirpath, indent):
    item_list = get_dir_content(dirpath)
    for item in item_list:
        if is_this_dir(dirpath + '/' + item):
            print('listing dir: ', item)
            print_all_file_names(dirpath + '/' + item, indent + '    ')
        else:
            print(indent + item)

##################################################


def get_dir_content(dirpath):
    content = os.listdir(dirpath)
    return content

def is_this_dir(dirpath):
    return os.path.isdir(dirpath)




print_all_file_names('/home/alex/pyt', '')