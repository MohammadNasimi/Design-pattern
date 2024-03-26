
import xmltodict # convert xml to dict

class Aplication:
    def send_request(self):
        return 'data.xml'
    
    
class Analytic:
    def receive_request(self,json):
        return json
    

class Adapter:
    def convert_xml_to_json(self,file):
        with open(file,'r') as f:
            obj = xmltodict.parse(f.read())
        return obj
    
def client_adapter():
    sender = Aplication().send_request()
    convert_data = Adapter().convert_xml_to_json(sender)
    result = Analytic().receive_request(convert_data)
    return result

print(client_adapter())