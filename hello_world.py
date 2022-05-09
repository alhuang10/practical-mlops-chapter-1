def hello_world():
    print("Hello World!")

def add(x: int, y: int):
    return x+y


if __name__ == "__main__":
    hello_world()
    
    print(f"3 +4 is {add(3,4)}")
