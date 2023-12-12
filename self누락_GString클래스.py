str = "Not Class Member"
class GString:
    def __init__(self):
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        #버그 수정
        #print(str)
        print(self.str)

g = GString()
g.set("First Message")
g.print()
