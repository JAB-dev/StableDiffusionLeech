import multiprocessing
from multiprocessing.dummy import Process
import requests

def scrape(start,end):
    for x in range(start,end):
        y= requests.get('https://'+ str(x) + '.gradio.app/')
        #check if the response is 200
        if (y.status_code == 200):
            #TODO Before printing also check if the title of the page from y is Stable Diffusion
            print('https://'+ str(x) + '.gradio.app/')
            
if __name__ == "__main__":
    #best range is 10000 to 30000
    start=10000
    end=30000
    diff=(end-start)
    #Just make threads a big number, your internet is probably the limiting factor and not the threadcount
    threadcount=5000
    offset=round(diff/threadcount)
    for x in range(1,threadcount):
        t = Process(target=scrape, args=(start+(x*offset),start+((x+1)*offset)))
        t.start()




