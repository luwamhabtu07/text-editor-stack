class TextOperation:
    def __init__(self, op_type, char=None):
        self.op_type =op_type
        self.char=char

class TextEditor:
    def __init__(self):
        self.text=''
        self.history=[]
    
    def add_char(self, char):
        self.text +=char
        self.history.append(TextOperation("add", char))
        self.display()
    
    def delete_char(self):
        if self.text:
            removed_char = self.text[-1]
            self.text=self.text[:-1]
            self.history.append(TextOperation("delete", removed_char))
        self.display()

    def undo(self):
        if not self.history:
            print("Nothing to undo.")
            return
        last_op= self.history.pop()

        if last_op.op_type == "add":
            self.text=self.text[:-1]
        elif last_op.op_type =="delete":
            self.text +=last_op.char
        self.display()

    def display(self):
        print("Current Text:",self.text)
            