"""
Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.

For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”.
"""

class ReadableFile:
    def __init__(self, path) -> None:
        self.path_name = path
        self.cursor_position = 0

    def read7(self) -> str:
        ret = ""
        with open(self.path_name) as file:
            read_data = file.read()
            ret += read_data[self.cursor_position: self.cursor_position+7]
        self.cursor_position += 7
        return ret
    
    def readN(self, n) -> str:
        ret = ""
        with open(self.path_name) as file:
            read_data = file.read()
            ret += read_data[self.cursor_position: self.cursor_position+n]
        self.cursor_position += n
        return ret
            

if __name__ == "__main__":
    entry = "./text.txt"
    file = ReadableFile(entry)
    print(file.read7())
    print(file.readN(15))
    print(file.readN(15))
    