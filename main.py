from time import sleep

print("this is my file to demo best pract")

def process_data(data):
    print("begining data processing..")
    modified_data = data + "---- is modified"
    sleep(3)
    print("data processing")
    return modified_data

