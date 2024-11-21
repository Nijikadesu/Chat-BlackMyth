import os


def _create_file_if_not_exists(file_path: str):
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            f.write("")
        print(f"created file: {file_path}")


def _create_folder_if_not_exists(folder_path: str):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"created folder: {folder_path}")
