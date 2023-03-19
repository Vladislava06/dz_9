import pandas as pd
def main():
     file = pandas.read_csv('california_housing_test.csv')
     print(file[file['population'] < 500][['median_house_value']].median()) #40
     print(file[file['population'] == file['population'].min()][['households']].max()) #42

if __name__=='__main__':
     main()