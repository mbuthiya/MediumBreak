#!virtual/bin/python3.6
import random
import time
import webbrowser  # module to open web browser


def read_posts(sessions):
    '''
    Function that reads through the links
    Shuffles the links
    and creates a random list of articles to read for each sessions
    '''

    with open('articles.txt', 'r') as handle:
        articles = handle.readlines()
        random.shuffle(articles)  # shuffles all the articles
        # chooses a select number of articles for that session
        chosen_articles = random.sample(articles, k=sessions)

    return chosen_articles


def open_browser(link):
    '''
    Function that opens a browser tab and displays the link
    '''

    webbrowser.open_new_tab(link)  # Opens a new browser tab


def get_int_input():
    '''
    Function to get a user Input convert it to
    an Integer and validates it
    '''

    while True:
        try:
            number = int(input())
            return number
        except ValueError:
            print('Please Enter an Integer Input')
            continue


def main():
    print('Welcome To Take a break How many sessions will you be working?')
    sessions = get_int_input()

    print('How many Minutes per session?')
    time_per_session = get_int_input() * 60

    posts = read_posts(sessions)
    sessions_run = 0

    while sessions_run < sessions:
        time.sleep(time_per_session)
        post = posts[sessions_run]
        open_browser(post)
        sessions_run += 1


if __name__ == '__main__':
    main()
