import os


def mk_dir(file_path):
    if not os.path.exists(file_path):
        os.makedirs(file_path)
