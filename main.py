from time import sleep

print("this is my file to demo best pract")

def process_data(data):
    print("begining data processing..")
    modified_data = data + "---- is modified"
    sleep(3)
    print("data processing")
    return modified_data

def read_data_from_web():
    print('read data from the web')
    data = "data from the web"
    return data

def write_data_to_database(data):
    print('writing data to the DATABASE')
    print(data)

def main():
    data = read_data_from_web()
    modified_data = process_data(data)
    write_data_to_database(modified_data)

if __name__ == '__main__':
    main()