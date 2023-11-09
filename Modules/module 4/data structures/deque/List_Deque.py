class ListDeque:
    def __init__(self):
        self.L = []

    def addfirst(self, item):
        self.L.insert(0, item)

    def addlast(self, item):
        self.L.append(item)

    def removefirst(self):
        return self.L.pop(0)

    def removelast(self):
        return self.L.pop()

    def __len__(self):
        return len(self.L)