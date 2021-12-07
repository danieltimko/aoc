
def run():
    with open('input') as file:
        arr = list(map(int, file.readlines()[0].split(',')))
        print(min(sum(abs(x-y) for y in arr) for x in arr),
              min(sum(abs(x-y)*(abs(x-y)+1)//2 for y in arr) for x in arr))


run()
