import time,datetime
class Room:
    clock = 9
    print(123)
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')

    def __init__(self,name):
        x="hi"
        self.name=name

    def __repr__(self):
        return (f'brand a clock is:{self.name}, time is: {self.st}')

print(Room("mizan"))

print(Room("switch"))
print(Room("violet"))