import functools

def pd(func=None):
    """Proxy decorator"""
    from antidetect.proxy_settings import SetProxy
    from core.settings import proxy
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self):
            if proxy:
                proxy_array = SetProxy.get_proxy()
                if len(proxy_array) == 4:
                    user = proxy_array[0]
                    pswd = proxy_array[1]
                    host = proxy_array[2]
                    port = proxy_array[3]
                    proxy_addr = f"{user}:{pswd}@{host}:{port}"
                    self.options.add_argument(f'--proxy-server=http://{proxy_addr}')
                else:
                    host = proxy_array[0]
                    port = proxy_array[1]
                    proxy_addr = f"{host}:{port}"
                    self.options.add_argument(f'--proxy-server=http://{proxy_addr}')
            return func(self)
        return wrapper
    return decorator
