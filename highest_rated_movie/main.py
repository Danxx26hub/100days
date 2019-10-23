import requests
from collections import namedtuple, Counter
import csv


def main():
    data = get_data_set()
    write_csv(data)
    file = 'movie_dataset.csv' 
    read_the_data(file)
    

def get_data_set():
    url = 'https://raw.githubusercontent.com/sundeepblue/movie_rating_prediction/master/movie_metadata.csv'
    try:
        response = requests.get(url)
    
        return response.text
    except:
        print('error data not available') 
    
def write_csv(data):
    print('please wait writing data to file...... ')
    with open('movie_dataset.csv', 'w') as csv_file:
        csv_file.write(data)
    print('done!')
        

def read_the_data(file):
    print(file)

    fields = ('title', 'year', 'score')
    Movie = namedtuple('Movie',fields)
    with open(file, 'r') as csv_file:
        #csv_file.readline()
        reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in reader:
            if line_count == 0:
                print(f'{",".join(row)}')
                line_count = line_count + 1
                break
            else:
                print(row)
                line_count = line_count + 1


        for data in map(Movie._make, reader):
            print(data.title)










if __name__ == '__main__':
    main()