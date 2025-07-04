def count_down_generator(start=10):
    current = start
    while current >= 0:
        yield current 
        current -=1

for c in count_down_generator(5):
    print(c)        