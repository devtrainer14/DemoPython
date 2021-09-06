from abs_hidden import document
class word(document):
       def __init__(self):
              super(word,self).__init__("word doc1")
       def show(self):
              print("show word content")

class pdf(document):
       def __init__(self):
              super(pdf,self).__init__("pdf doc")
       def show(self):
              print("show pdf content1111")

obj = word()


obj1 = pdf()




