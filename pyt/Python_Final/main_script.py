import File_Handler


folder_to_scan = '/home/alex/pyt'
files_detailed = {}

# files_list = {}
# files_list = {Scan_Files.scan_all_files(folder_to_scan): Scan_Files.get_file_size(folder_to_scan)}

files_list = File_Handler.scan_all_files(folder_to_scan)
files_size = File_Handler.get_file_size(folder_to_scan)


for file in File_Handler.scan_all_files(folder_to_scan):
    file_stats = {}
    file_stats.append = File_Handler.get_file_size

print(files_list)