import argparse

from library import data_parser
from library import session

INPUT_FILE = 'data/Consumer_Complaints_sm.csv'

parser = argparse.ArgumentParser(description='Parse consumer complaints.')
parser.add_argument('--input_file', type=str, default=INPUT_FILE, help='input csv file of consumer complaints')


def main() -> None:
    args = parser.parse_args()
    consumer_complaints = data_parser.parse(args.input_file)

    client_session = session.Session(consumer_complaints)
    print('you\'re in the consumer complaints parser cli! type `help` to get started.')
    while True:
        command, *args = input('> ').split()
        if command == 'help':
            print('exit - exit the cli\n'
                  'search <keywords> - search state and/or year (e.g. `search NJ 2015`)\n'
                  'history - show list of previous searches\n'
                  'show <index> - show search results for history item at index\n'
                  'remove <index> - remove history item at index')
        elif command == 'exit':
            break
        elif command == 'search':
            keywords = args[:2]  # truncate keywords to at most 2 (state and/or year)
            client_session.show_results(keywords)
        elif command == 'history':
            client_session.show_history()
        elif command == 'show':
            index = int(args[0])  # raises ValueError if not int
            client_session.show_history_item(index)
        elif command == 'remove':
            index = int(args[0])  # raises ValueError if not int
            client_session.remove_history_item(index)


if __name__ == '__main__':
    main()
