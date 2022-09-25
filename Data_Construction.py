import pandas as pd
import openpyxl


class Data_Construction:
    def __init__(self):
        self.__date = None
        self.__df = None
    
    def clean_data(self,raw_data, date):
        self.__date = date
        title = ['Case Number','Defendant','Plaintiff','Case Type','Hearing Time']
        rows = []
        n = 1
        m = 0
        ## Screen for only eviction cases
        while n < len(raw_data[0]):
            if raw_data[0][n][4] == 'Unlawful Detainer':
                rows.append(raw_data[0][n][1:])
                m += 1
            n +=1
        dates = [str(self.__date)]*m # Hearing Date Col
        ## Constructing pandas dataframe
        df = pd.DataFrame(columns = title, data = rows)
        df.index = df['Case Number'] # Set the index to case number 
        df['Hearing Date'] = dates
        frames = [self.__df, df]
        self.__df = pd.concat(frames)
        #df.to_excel('test.xlxs')
        
    def dataframe(self):
        return self.__df

    def to_csv(self):
        return self.__df.to_excel('220725.xlsx')
