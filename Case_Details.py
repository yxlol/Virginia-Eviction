import pandas as pd
class Case_Details():
    def __init__(self):
        self.__df = None
        self.__error = []
    
    def get_data(self, cases):
        if len(cases) == 26:
            return  self.clean_table(cases)
            
        else:
            self.__error.append(cases[0][3])
            return self.__error

        

    def clean_table(self, cases):
        rows = []
        case_list = []
        title = ['Case Number', 'Filed Date', 'Plaintiff Name 1', 
        'DBA/TA', 'Address', 'Attorney', 'Plaintiff Name 2', 'DBA/TA', 
        'Address', 'Defendant Name 1', 'DBA/TA', 'Address', 'Defendant Name 2', 
        'DBA/TA', 'Address', 'Defendant Name 3', 'DBA/TA', 'Address','Hearing Date', 
        'Time', 'Result', 'Hearing Type', 'Courtroom', 'Judgement', 'Costs', 'Attorney Fees', 
        'Principal Amount', 'Other Amount', 'Interest Award', 'Possession', 
        'Writ of Eviction Issued Date', 'Writ of Fieri Facias Issued Date', 'Notes']
        
    
        if cases[0][1] == ['Case Information']:
            case_list.append(cases[0][2][1]) #Case Number
            case_list.append(cases[0][2][3]) #Filed Date
        else: 
            case_list.append(cases[0][3][1]) #Case Number
            case_list.append(cases[0][3][3]) #Filed Date
        case_list+= cases[2][4][:3] # Plaintiff Information 1
        case_list.append(cases[2][4][4])

        if len(cases[2]) == 5:
            case_list += ['', '', '']
        else:
            case_list += cases[2][5][:3]

        case_list += cases[5][4][:3] #Defendant Information 1
        if len(cases[5]) == 5:
            case_list += ['', '', '', '', '', ''] # Fill in the blanks if there's only one defendant
        elif len(cases[5]) == 6:
            case_list += cases[5][5][:3] # Second Defendant
            case_list += ['', '', ''] # Fill in the Blank
        elif len(cases[5]) >= 7:
            case_list+= cases[5][5][:3] # Second Defendant
            case_list += cases[5][6][:3] # Third Defendant
        else:
            pass
        case_list += cases[8][4] # Hearing Date, Time, Judgement
        case_list.append(cases[17][3][1]) # Judgement
        case_list.append(cases[17][3][3]) # Costs
        case_list.append(cases[17][3][5]) # Attorney Fees
        case_list.append(cases[17][4][1]) # Principals
        case_list.append(cases[17][4][3]) # Other Amount
        case_list.append(cases[17][4][5]) # Interest Awarded
        case_list.append(cases[17][5][1]) # Possession
        case_list.append(cases[17][5][3]) # Writ of Eviction Issued Date
        case_list.append(cases[17][5][5]) # Writ of Fieri Facias Issued Date
        if len(cases[0]) == 5: # When there is a Note
            case_list += cases[0][1]
        elif len(cases[0]) == 4:
            case_list.append('') # When there isn't a Note
        elif len(cases[5]) >= 8:
            case_list.append('revisit this case!!!' + str(cases[0][2][1]))

        rows.append(case_list)
        df = pd.DataFrame(columns = title, data = rows)
        frames = [self.__df, df]
        self.__df = pd.concat(frames)
        

    def data_frame(self):
        return self.__df
    
    def to_excel(self):
        return self.__df.to_excel('20220725.xlsx')
    
    def errors(self):
        return self.__error


    
    