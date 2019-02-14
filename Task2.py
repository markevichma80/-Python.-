
from collections import Counter
from collections import namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")

class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"

def huffman_encode(s):
    h = []
    for x,y in Counter(s).items():
        h.append([y,len(h), Leaf(x)])
        h=sorted(h)
    count=len(h)
    for i in range(len(h)):
        if len(h)>1:
            freg1,_count1,left=h.pop(0)
            freg2, _count2, right = h.pop(0)
            h.append([freg1 + freg2, count, Node(left,right)])
            h=sorted(h)
            count+=1
    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")
    return code

def main():
    s = input()
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)

    print(len(code), len(encoded))
    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))
    print(encoded)  

if __name__ == "__main__":
    main()