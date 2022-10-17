import multiprocessing
from multiprocessing.dummy import Process
import requests


def scrape(start, end):
    #Given start and end string, contact 'https://' + str(x) + '.gradio.app/', if the response is 200 and does not contain the text "No", print the url
    #The given start and end string are in the format of 16 characters consisting of numbers and lowercase letters such as e6dcf16a29a50cac
    for x in range(int(start, 16), int(end, 16)):
        url = 'https://' + str(hex(x))[2:] + '.gradio.app/'
        r = requests.get(url)
        if r.status_code == 200 and 'No' not in r.text:
            print(url)

if __name__ == "__main__":
    #Range is now 16 length hexadecimal digits
    start = 'cccccccccccccccc'
    end = 'ffffffffffffffff'
    #Split the range into x parts
    x=1000
    #Calculate the length of each part
    length = int(int(end, 16) / x)
    #Create a list of processes
    processes = []
    #Create a process for each part
    for i in range(x):
        #Calculate the start and end of each part
        start_part = int(start, 16) + i * length
        end_part = int(start, 16) + (i + 1) * length
        #Create a process for each part
        processes.append(Process(target=scrape, args=(str(hex(start_part))[2:] , str(hex(end_part))[2:] )))
    #Start all processes
    for process in processes:
        process.start()