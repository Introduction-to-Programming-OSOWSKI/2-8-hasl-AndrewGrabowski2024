#WRITE YOUR CODE IN THIS FILE
def hasL(w):
    i = 0
    for i in range(0, len(w)):
        if w[i] == "l":
            return True
    else:
         return False

print(hasL("meon"))