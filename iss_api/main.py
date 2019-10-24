from api_data import provide_endpoints, get_astronauts



def main():
    people = provide_endpoints().astronauts
    get_astronauts(people)
    print(get_astronauts(people))






if __name__ == "__main__":
    main()
