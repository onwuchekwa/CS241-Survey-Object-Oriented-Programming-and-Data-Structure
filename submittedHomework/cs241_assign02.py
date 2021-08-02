import csv

def prompt_filename():
    filename = input("Please enter the data file: ")
    return filename
 
def get_data():
    get_file = prompt_filename()
    read_file = csv.reader(open(get_file, newline=''))
    next(read_file)
    return list(read_file)
        
        
def compute_average(data):
    arr = [float(line[6]) for line in data]
    average = sum(arr) / len(arr)
    print("The average commercial rate is: {0}".format(average))
    return arr

def compute_max(data, data_array):
    data_index = data_array.index(max(data_array))
    data_row = data[data_index]
    print("The highest rate is:\n{0} ({1}, {2}) - ${3}".format(data_row[2], data_row[0], data_row[3], str(float(data_row[6]))))
    
def compute_min(data, data_array):
    data_index = data_array.index(min(data_array))
    data_row = data[data_index]
    print("The lowest rate is:\n{0} ({1}, {2}) - ${3}".format(data_row[2], data_row[0], data_row[3], str(float(data_row[6]))))    
  
def main():
    data = get_data()
    print("")
    data_array = compute_average(data)
    print("")
    compute_max(data, data_array)
    print("")
    compute_min(data, data_array)

if __name__ == "__main__":
    main()

