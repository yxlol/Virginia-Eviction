class Date_Generator:
    def __init__(self):
        self.__date = None
        self.__month = None
        self.__year = None
        self.__duration = None
    
    ## Given valid date, month, and year, generate a string that 
    ## would be filled in the form when searching hearing date
    def generate_date(self, date, month, year):
        if date < 10:
            self.__date = '0' + str(date)
        else:
            self.__date = str(date)
        if month < 10:
            self.__month = '0' + str(month)
        else:
            self.__month = str(month)
        self.__year = str(year)
        string_date = self.__date + self.__month + self.__year
        return string_date 

if __name__ == "__main__":
    test = Date_Generator()
    date = test.generate_date(1,1,2022)
    print("Date generated is", date)