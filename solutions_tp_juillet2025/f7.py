class MyCountDown:
    def __init__(self,inclStart=10):
        self.count=inclStart+1

    def __iter__(self):
        return self
    
    def __next__(self):
        self.count -=1
        if self.count <0:
            raise StopIteration
        return self.count

for c in MyCountDown(5):
    print(c)