from json import load, JSONDecodeError

class ReadJson():
    def ReadToDict(self, path):
        try:
            with open(path) as file:
                data = load(file)
                return data
        except FileNotFoundError:
            print("dosya bulunamadı...")
        except JSONDecodeError:
            print("json formatı hatalı")