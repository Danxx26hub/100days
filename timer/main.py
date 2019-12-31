from reader import feed

def main():
    """download the latest tutorial from RP"""


    tutorial = feed.get_article(0)
    print(tutorial)


if __name__=='__main__':
    main()