import zipfile


zip_file_path = 'data.zip'


extract_to_path = 'data'


with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to_path)

