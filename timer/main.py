import time
from reader import feed

def main():
    """download the latest tutorial from RP"""
    tic = time.perf_counter() # start counter 


    tutorial = feed.get_article(0)
    toc = time.perf_counter() # stop timing

    print(f"Downloaded the tutorial in {toc - tic:0.4f} seconds")
    print(tutorial)


if __name__=='__main__':
    main()