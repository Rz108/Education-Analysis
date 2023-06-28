import numpy as np
#Creating the function needed for data analysis
class functionsNeeded:
    def __init__(self,np):
        self.np = np
        pass
    #Check the data type of each columns
    def columnInArr(self,n,j):
        
        for i in n:
            nan = False
            if 'U' not in str(j[i].dtype):
                nan = (np.isnan(j[i]).any())
            arr = j[i].astype('U8')
            print(f'- {i} {type(j[i].dtype)} isnumeric: {np.unique(np.char.isnumeric(arr))[0]}, null values: {nan} ')
    #Check the unique values of each columns
    def uniqueValues(self,n,j):
        print('\nThe unique values of each column are:')
        for i in n:
            print(f'{len(self.np.unique(j[i]))} unique values in {i}')
    #Desrcibe the overall characteristics according to numpy library
    def characteristics(self, arr):
        max = self.np.max(arr)
        mean = self.np.mean(arr)
        min = self.np.min(arr)
        varriation = self.np.var(arr)
        std = self.np.std(arr)
        count = self.np.count_nonzero(arr)
        upperQuartile = self.np.quantile(arr,0.75)
        LowerQuartile = self.np.quantile(arr,0.25)
        median = self.np.median(arr)
        print(f'The number of elements is: {count:15}\nThe min is: {min:15}\nThe max is: {max:15}\nThe mean is: {mean:15.2f}\nThe variance is: {varriation:15.2f}\nThe median is {median:15.3f}\nThe standard deviation is: {std:15.3f}\nThe lower quartile is {LowerQuartile:15.3f}\nThe upper quartile is {upperQuartile:15.3f}')
        print()
        return min, max, mean, varriation, std, count,median,upperQuartile,LowerQuartile
functionNeed = functionsNeeded(np)