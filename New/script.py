
def findSum(x):
    return sum([abs(i-j) for i, j in zip(x, x[1:])])

if __name__ == "__main__":
    print(findSum([5,2,8]))

class NewClass():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def prints(self):
        return self.x * self.y

C = NewClass(5, 5)
print(C.prints())