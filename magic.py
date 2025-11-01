class students:
    def __init__(self):
        self.royxat = []
    
    def add(self, ism):
        self.royxat.append(ism)
    
    # __len__ without
    def count(self):
        return len(self.royxat)
    
    # __len__ with
    def __len__(self):
        return len(self.royxat)

guruh = students()
guruh.add("Ali")
guruh.add("Vali")

print(guruh.count())  # out 2 - special metod
print(len(guruh))    # out 2 - len() function   