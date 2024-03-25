from abc import ABC,abstractmethod

class File(ABC): # creator
    def __init__(self,file):
        self.file = file
    @abstractmethod    
    def make(self):
        pass
    
    def call_edit(self):
        product = self.make()
        result = product.edit(self.file)
        return result


class JsonFile(File): # creator
    
    def make(self):
        return Json()
    
class XmlFile(File): # creator
    
    def make(self):
        return Xml()
    

class Json: # product
    def edit(self,file):
        return f'working on  {file} json'
        

class Xml: # product
    def edit(self,file):
        return f'working on {file} xml'
    
    
def client(file,format): # client
    formats ={
        'json':JsonFile,
        'xml':XmlFile
    }
    result = formats[format](file)
    return result.call_edit()

print(client('namefile','json'))
print(client('namefile','xml'))