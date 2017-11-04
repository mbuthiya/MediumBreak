#!virtual/bin/python3.6
import random
import webbrowser


def read_posts(sessions):

    with open('articles.txt', 'r') as handle:
        articles = handle.readlines()
        random.shuffle(articles)
        chosen_articles = random.sample(articles, k=sessions)

    return chosen_articles


def open_browser(link):
    webbrowser.open_new_tab(link)

    # if __name__ == '__main__':
    #     print('Welcome To Take a break How many sessions will you be working?')
    #     sessions = int(input())
    #     print('How many Minutes per session?')
    #     time_per_session = int(input())
