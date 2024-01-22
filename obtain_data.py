import os
import threading

def search_in_directory(root, target_filename, result_holder):
    for dirpath, _, filenames in os.walk(root):
        if target_filename in filenames:
            file_path = os.path.join(dirpath, target_filename)
            result_holder['file_path'] = file_path
            result_holder['found'] = True
            stop_event.set()  # set the event and notice other threads to stop
            break
        if stop_event.is_set():  
            break

#init root dir and the target filename
root_directories = ['ProcessedData', 'RawData', 'SummaryData']
filename = '49.tiff'

result = {'file_path': None, 'found': False}


#init event
stop_event = threading.Event()

#init threads
threads = []
for root_dir in root_directories:
    thread = threading.Thread(target=search_in_directory, args=(root_dir, filename, result))
    threads.append(thread)
    thread.start()

#wait for all threads to finish
for thread in threads:
    thread.join()

file_path = result['file_path']
found = result['found']

if found:
    print(f"File '{filename}' is found")
    print(f"File Path: {file_path}")
    print(f"File Path: {os.path.basename(file_path)}")

else:
    print(f"File '{filename}' not found")
