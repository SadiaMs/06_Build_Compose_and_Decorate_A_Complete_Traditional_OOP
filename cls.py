class Counter:
    count = 0
    def __init__ (self):
        Counter.count += 1

    @classmethod
    def newadd(cls):
        return cls.count 

if __name__ == "__main__":
    c1 = Counter()
    c2 = Counter()
    c3 = Counter()
    c4 = Counter()
    print(f"total number of counter is : {Counter.count}")