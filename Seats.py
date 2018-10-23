
class Seats():
    def __init__(self):
        self.Economical = 0
        self.Business = 0
        self.FirstClass = 0

    def SetEconomical(self, number):
        self.Economical = number

    def SetBusiness(self, number):
        self.Business = number

    def SetFirstClass(self, number):
        self.FirstClass = number

    def GetEconomical(self):
        return self.Economical

    def GetBusiness(self):
        return self.Business

    def GetFirstClass(self):
        return self.FirstClass

    def PAX(self):
        return self.Economical + 2 * self.Business + 4 * self.FirstClass
    