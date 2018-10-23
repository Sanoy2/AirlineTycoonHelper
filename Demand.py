from Seats import Seats

class Demand():
    def __init__(self):
        self.Seats = Seats()

    def Results(self):
        for i in range(1,10):
            print(self.PaxDistribution(i))
            print()

    def GetData(self):
        economical = int(input("Economic demand: "))
        self.Seats.SetEconomical(economical)
        
        business = int(input("Business demand: "))
        self.Seats.SetBusiness(business)

        firstClass = int(input("First class demand: "))
        self.Seats.SetFirstClass(firstClass)

    def PaxDistribution(self, howManyCourses):  # 1 course is 2 flights
        Economical = self.Seats.GetEconomical() / (howManyCourses * 2)
        Business = self.Seats.GetBusiness() / (howManyCourses * 2)
        FirstClass = self.Seats.GetFirstClass() / (howManyCourses * 2)
        Pax = self.Seats.PAX() / (howManyCourses * 2)

        return """Results for courses: {numberOfCourses}
Economical: {economical}
Business  : {business}
FirstClass: {firstClass}
Total PAX : {pax}

    """.format(
            numberOfCourses = howManyCourses,
            economical = round(Economical),
            business = round(Business),
            firstClass = round(FirstClass),
            pax = round(Economical) + round(Business) + round(FirstClass)
        )