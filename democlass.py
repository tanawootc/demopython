class demo:
    productid=0
    
    def __init__(self,name):
        super().__init__()
        self.name=name
    
    def printname(self):
        print(self.name)

class demo2(demo):
    def shape(self):
        print('shape')

book=demo('jame')
book.printname()

pen=demo2('ada')
pen.printname()
pen.shape()
    