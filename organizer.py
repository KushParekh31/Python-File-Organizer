import os
import shutil
from pathlib import Path
from config import FILE_TYPES

def organize_folder(folder_path):
    folder = Path(folder_path)

    if not folder.exists():
        print("Folder does not exist!")
        return

    moved = 0

    for file in folder.iterdir():

        if file.is_dir():
            continue

        extension = file.suffix.lower()

        category = None

        for folder_name, extensions in FILE_TYPES.items():
            if extension in extensions:
                category = folder_name
                break

        if category is None:
            category = "Others"

        destination = folder / category
        destination.mkdir(exist_ok=True)

        shutil.move(str(file), str(destination / file.name))
        moved += 1

    print(f"\n✅ Organized {moved} files successfully!")

if __name__ == "__main__":
    path = input("Enter Folder Path: ").strip()
    organize_folder(path)
