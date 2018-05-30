from multiprocessing import Pool
from time import time
import requests as req
import pandas as pd

def get_url(url):
    page = req.get(url)
    return page.content

def main():

    urls = pd.read_csv('./data/websites.csv')
    urls_subset = list(urls.iloc[:20,0].values)
    urls_subset_full = []
    for url in urls_subset:
        urls_subset_full.append('http://'+url)
    # print(urls_subset)

    print('Normal')
    time1 = time()
    contents = list(map(get_url, urls_subset_full))
    time2 = time()
    print('Took %0.3f s' % (time2-time1))

    print('-'*50)

    pool = Pool(8)
    print('Multiprocessing')
    time1 = time()
    contents = pool.map(get_url, urls_subset_full)
    time2 = time()
    print('Took %0.3f s' % (time2-time1))

if __name__ == '__main__':
    main()
