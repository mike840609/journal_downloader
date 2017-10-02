import urllib2
import re
import requests
import os
import errno

import time
import datetime

def loadUrlFromTxtOrUrl(path):
    file = open(path) 
    return file.read() 

def getUrls(str_temp):

    urlsArr = []

    # print str_temp
    arr = [s.strip() for s in str_temp.splitlines()]

     # Source : Institute for Operations Research and the Management Sciences (INFORMS) 
    for x in (y for y in arr if "http://pubsonline.informs.org" in y and 'full' in y ):
        # print x
        # example
        # http://pubsonline.informs.org/doi/pdf/10.1287/orsc.2017.1140
        
        startIndex = x.index('http')
        x = x[startIndex:]
        x = x.replace("full", "pdf")
        urlsArr.append(x)
    
    return urlsArr

def downloadPDF(urlsArr):

    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H-%M-%S')
    directory = './' + st + '/'

    if not os.path.exists(directory):
        os.makedirs(directory)

    for url in urlsArr:

        file_name = directory + url.split('/')[-1] + '.pdf'

        r = requests.get(url, stream=True)

        with open( file_name , 'wb') as f:
            
            for chunk in r.iter_content(chunk_size=1024): 
                 if chunk: 
                    f.write(chunk)

    print("Completed")
    


def main():

    # test_code ===========================================================
    # str_temp =  loadUrlFromTxtOrUrl('informs_mksc36_471.txt')
    # str_temp =  loadUrlFromTxtOrUrl('informs_orsc22_1369.txt')
    # str_temp =  loadUrlFromTxtOrUrl('informs_orsc28_597.txt')
    str_temp = loadUrlFromTxtOrUrl('./urls_file/test.txt')
    urls = getUrls(str_temp)
    downloadPDF(urls)


    #  batch download  ===========================================================
    '''
    all_files = os.listdir("./urls_file/")

    for file_name in all_files:
        str_temp =  loadUrlFromTxtOrUrl("./urls_file/" + file_name)
        urls = getUrls(str_temp)
        downloadPDF(urls)
    '''

if __name__ == '__main__':
    main()