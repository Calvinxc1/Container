class Container:
    def __init__(self, **kwargs):
        self._stored_keys = set()
        
        for key, val in kwargs.items():
            self.__setattr__(key, val)
    
    def __setattr__(self, name, value):
        self.__dict__[name] = value
        if not name.startswith('_'): self._stored_keys.add(name)
            
    def __setitem__(self, key, val):
        self.__setattr__(key, val)
            
    def __getitem__(self, key):
        return self.__getattribute__(key)
        
    def __iter__(self):
        return iter(sorted(self._stored_keys))