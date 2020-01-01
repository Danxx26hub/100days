from reader import feed
from timer import Timer


t = Timer()

def main():
    """download the latest tutorial from RP"""
    #tic = time.perf_counter() # start counter
    t.start() 


    tutorial = feed.get_article(0)
    #toc = time.perf_counter() # stop timing
    t.stop()

    
    print()
    print()
    #print(tutorial)


if __name__=='__main__':
    main()