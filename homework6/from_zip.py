import zipfile

# Путь к архиву
zip_file_path = 'data.zip'


extract_to_path = 'data'

# Открытие и разархивирование
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to_path)

print(f"Files have been extracted to {extract_to_path}")