import ipdb

class Person:
    def __init__(self, name, gender) -> None:
        self._name = name
        self.gender = gender
        
    def get_name(self):
        return self._name
    
    name = property(get_name)
    # user role: data entry
    # super admin

if __name__ == "__main__":
    print("Am run directly")
    
    ipdb.set_trace()
    