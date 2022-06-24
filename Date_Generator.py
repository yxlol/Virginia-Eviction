from datetime import date, timedelta

class Date_Generator:
    def __init__(self):
        self.__day = None
        self.__month = None
        self.__year = None
        self.__list = []
    
    ## Given valid date, month, and year, generate a string that 
    ## would be filled in the form when searching hearing date
    
    def date_input(self, day, month, year, delta):
        new_date = Date_Generator()
        curr_date =  date(year,month,day)
        for i in range(delta+1):
            curr_date = date(year, month, day) + timedelta(days = i)
            if curr_date.weekday() <5 :
                self.__list.append(str(new_date.__generate_date(curr_date.day, curr_date.month, curr_date.year)))
        return  self.__list

    def __generate_date(self, day, month, year):
        if day < 10:
            self.__day = '0' + str(day)
        else:
            self.__day = str(day)
        if month < 10:
            self.__month = '0' + str(month)
        else:
            self.__month = str(month)
        self.__year = str(year)
        string_date =  self.__month + '/' + self.__day + '/' + self.__year
        return str(string_date)
    
    def __str__(self):
        return str(self.__list)
    
    def len(self):
        return len(self.__list)

if __name__ == "__main__":
    test = Date_Generator()
    date = test.date_input(1,1,2001,40)
    print("Date generated is", date, "and there are", test.len(), "weekdays")