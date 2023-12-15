import os

def get_recent_files(directory, num_files=3, file_extensions=("jpg", "jpeg", "png")):

    files = [file for file in os.listdir(directory) if file.lower().endswith(file_extensions)]
    files.sort(key=lambda x: os.path.getmtime(os.path.join(directory, x)), reverse=True)
    recent_files = files[:num_files]
    recent_file_paths = [os.path.join(directory, file) for file in recent_files]

    while len(recent_file_paths) < num_files:
        recent_file_paths.append('temp.jpg')

    return recent_file_paths

directory_path = "D:\\Downloads MSI GF63_2\\Test\\"
recent_files = get_recent_files(directory_path)

r1, r2, r3 = recent_files[:3]




directory_path = "D:\\Downloads MSI GF63_2\\Test\\"

