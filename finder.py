

def findN(text, string, n):
    pos = 0
    for i in range(0, n + 1):

        pos = text[pos + len(string):].find(string)
        print("Loop: " + str(i) + " Pos: " + str(pos))
        #text = text[pos + len(string):]
    return pos


def findExclude(text, find, start):
        return text[start:].find(find)
