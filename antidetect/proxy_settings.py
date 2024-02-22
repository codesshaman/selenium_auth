from core.debug import dd
import random
import os


@dd
def read_proxy_from_file(file_path):
    content = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            content.append(line)
    return content


class SetProxy:
    """Class for reading proxy from file and set up proxy"""
    def __init__(self):
        self.path = '.PROXY.list'
        self.proxy_list = []

    @dd
    def read_proxy_file(self):
        proxy_list = read_proxy_from_file(self.path)
        for proxy in proxy_list:
            self.proxy_list.append(proxy)

    @dd
    def get_random_proxy(self):
        return random.choice(self.proxy_list)
    
    @dd
    def get_proxy_addr(self):
        self.read_proxy_file()
        return self.get_random_proxy()
        
    @dd
    def get_proxy(self):
        proxy = self.get_proxy_addr()
        proxy_array = proxy.split(":")
        if len(proxy_array) == 4:
            return proxy_array
        elif len(proxy_array) == 2:
            return proxy_array
        else:
            raise ValueError("Incorrect proxy record: " + str(proxy))
