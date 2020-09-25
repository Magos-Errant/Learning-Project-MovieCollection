# Milestone project - move archive

data_storage = {

}

def menu():
    print('''
    Hello dear User, this is the "Short Memory Movie Collection!"
    We will keep track of your movies until you close this program!
    To quit simply write "Q" and confirm with Enter key.
    
    1 - Add movie to your collection
    2 - View your movie collection
    3 - Search for movie by title
    ''')
    menu_selection = input('What would you like to do?: ')
    while menu_selection != 'Q':
        if menu_selection == '1':
            add_movie()
        elif menu_selection == '2':
            list_movies()
        elif menu_selection == '3':
            find_movie()
        else:
            print('I am sorry, this is an unknown command.')
            return_to_menu()

def return_to_menu():
    print('To return to menu write "R" and confirm with Enter key')
    _ = input()
    if _ == 'R':
        menu()
    else:
        return_to_menu()


def add_movie():
    x = len(data_storage) + 1
    a = str(input('What is the movie title?: '))
    b = str(input('What is the movie director?: '))
    c = str(input('What is the movie year?: '))
    data_storage[x] = {'title': a, 'director': b, 'year': c}
    return_to_menu()


def list_movies():
    for movie in data_storage:
        title = data_storage[movie]['title']
        director = data_storage[movie]['director']
        year = data_storage[movie]['year']
        print(f'Movie number {movie} is {title}, directed by {director} in year {year}.')
    return_to_menu()



def find_movie():
    _ = input('Please provide movie title you are looking for: ')
    for movie in data_storage:
        if data_storage[movie]['title'] == _ :
            director = data_storage[movie]['director']
            year = data_storage[movie]['year']
            print(f'Movie you are looking for is movie number {movie} directed by {director} in year {year}.')
            return_to_menu()
        else:
            continue
    else:
        print("There appear to be no such movie, check the spelling an try again")
        return_to_menu()

menu()




