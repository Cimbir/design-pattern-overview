import json


class JsonObject:
    def __init__(self, content: list[str]):
        self.content = content
        
    def get_json(self) -> str:
        return json.dumps(self.content)
    
class XmlObject:
    def __init__(self, content: list[str]):
        self.content = content
        
    def get_xml(self) -> str:
        return f"<xml>{''.join(self.content)}</xml>"
    
class JsonAdapter(XmlObject):
    def __init__(self, json_object: JsonObject):
        self.json_object = json_object
    
    def get_xml(self) -> str:
        return f"<xml>{self.json_object.get_json()}</xml>"
    
json_object = JsonObject(["Hello", "World"])
xml_object = XmlObject(["Hello", "World"])
json_adapter = JsonAdapter(json_object)

print("json :", json_object.get_json())
print("xml :", xml_object.get_xml())
print("json adapter :", json_adapter.get_xml())