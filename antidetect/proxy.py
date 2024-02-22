import os


def read_proxy_from_file(file_path):
    parent_dir = os.path.abspath(os.path.join(file_path, os.pardir))
    file_to_read = os.path.join(parent_dir, file_path)

    try:
        with open(file_to_read, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File not found!"


class SetProxy:
    """Class for reading proxy from file and set up proxy"""
    def __init__(self, file_path):
        self.path = file_path
        self.proxy = []
        self.content = ""

    def read_proxy_file(self):
        self.content = read_proxy_from_file(self.path)
    
    