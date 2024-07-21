#!/usr/bin/env python3

f = open("./plume/Downloads/filesystem.raw", "rb")
def read_file_entry(f, position):
    f.seek(position)
    
    # 다음 항목으로 이동하는 포인터를 읽음
    next_entry_pointer_data = f.read(4)
    next_entry_pointer = int.from_bytes(next_entry_pointer_data, byteorder='little')

    
    # 파일 이름의 크기를 읽음
    filename_size_data = f.read(1)
    filename_size = int.from_bytes(filename_size_data, byteorder='little')
    
    # 파일 이름을 읽음
    filename = f.read(filename_size).decode('utf-8')
    
    # MD5 해시를 읽음
    file_hash = f.read(16).hex()
    
    # 데이터 크기를 읽음
    data_size_data = f.read(4)
    data_size = int.from_bytes(data_size_data, byteorder='little')
    
    # 데이터를 읽음
    data = f.read(data_size)
    
    return {
        'next_entry_pointer': next_entry_pointer,
        'filename': filename,
        'file_hash': file_hash,
        'data_size': data_size,
        'data': data
    }

def read_filesystem(file_path):
    with open(file_path, 'rb') as f:
        # 첫 4바이트를 읽어 마지막 파일 항목에 대한 포인터를 얻음
        last_entry_pointer_data = f.read(4)
        last_entry_pointer = int.from_bytes(last_entry_pointer_data, byteorder='little')
        
        # 파일 항목들을 저장할 리스트
        file_entries = []
        
        # 파일 항목을 탐색
        current_pointer = last_entry_pointer
        while current_pointer != 0:
            file_entry = read_file_entry(f, current_pointer)
            file_entries.append(file_entry)
            current_pointer = file_entry['next_entry_pointer']
        
        return file_entries

# 파일 시스템을 읽고 각 파일 항목을 출력
file_entries = read_filesystem('./plume/Downloads/filesystem.raw')
for entry in file_entries:
    print(f"Filename: {entry['filename']}")
    print(f"Hash: {entry['file_hash']}")
    print(f"Data size: {entry['data_size']}")
    print(f"Data: {entry['data'][:100]}...")  # 데이터의 앞 100바이트만 출력
    print()
