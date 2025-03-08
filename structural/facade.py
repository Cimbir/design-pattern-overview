class FileReader:
    def __init__(self, filename: str):
        self._filename = filename
    
    def read_all(self) -> str:
        return f"Read info from {self._filename}"

class FileOpener:
    def __init__(self, filename: str):
        self._filename = filename
        
    def get_reader(self) -> FileReader:
        return FileReader(self._filename)
    
class ConvertToJson:
    def convert(self, data: str) -> str:
        return f"Converted data to json: {data}"

    
class ConvertToXml:
    def convert(self, data: str) -> str:
        return f"Converted data to xml: {data}"
    
class Converter:
    def convert_file_info(self, filename: str, convert_type: str) -> str:
        file_opener = FileOpener(filename)
        file_reader = file_opener.get_reader()
        data = file_reader.read_all()
        if convert_type == "json":
            return ConvertToJson().convert(data)
        elif convert_type == "xml":
            return ConvertToXml().convert(data)
        return "Invalid convert type"
    
converter = Converter()

print(converter.convert_file_info("file.txt", "json"))
print(converter.convert_file_info("file.txt", "xml"))