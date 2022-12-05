import os
import shutil
from pathlib import Path
from collections import defaultdict

path_downloads = Path.home() / 'Downloads'

items_type = defaultdict(list)

for item in os.listdir(path_downloads):
    path_item = os.path.join(path_downloads, item)
    item_is_file = os.path.isfile(path_item)
    if item_is_file:
        file_name, extension = os.path.splitext(item)
        items_type[extension[1:]].append(item)

for ext, files in items_type.items():
    os.mkdir(path_downloads / f'{ext}')
    new_dir_path = path_downloads / f'{ext}'
    for file in files:
        file_path = os.path.join(path_downloads, file)
        shutil.move(file_path, new_dir_path)
