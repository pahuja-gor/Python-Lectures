import requests
from pprint import pprint


class Game:

    def __init__(self, iPlayers, iOnline, iSales, iScore, iPublisher, iTitle, iPrice, iConsole):
        self.__numPlayers = iPlayers
        self.__isOnline = iOnline
        self.__sales = int(iSales) * 1000000
        self.__score = iScore
        self.__publisher = iPublisher
        self.__title = iTitle
        self.__price = iPrice
        self.__console = iConsole

    def __str__(self):
        record = self.__title + "\n" + "=====" + "\n"
        record += "Score: " + str(self.__score) + "\n" + "Sales: " + str(self.__sales) + " \n"
        record += self.__console + "\n" + "Price: " + str(self.__price) + "\n\n"
        return record

    def getScore(self):
        return self.__score

    def getConsole(self):
        return self.__console

def loadGames(data):
    games = []

    for item in data:
        g = Game(item['Features']['Max Players'], item['Features']['Online?'], item['Metrics']['Sales'],
                 item['Metrics']['Review Score'], item['Metadata']['Publishers'], item['Title'],
                 item['Metrics']['Used Price'], item['Release']['Console'])
        games.append(g)

    return games

def filterGamesByScore(games, bound):
    for game in games:
        if game.getScore() >= bound:
            print(game)

def filterGamesByConsole(games, console):
    for game in games:
        if game.getConsole() == console:
            print(game)

def main():
    response = requests.get('https://corgis-edu.github.io/corgis/datasets/json/video_games/video_games.json')
    data = response.json()

    # pprint(data[0])
    games = loadGames(data)

    # print(type(games))
    # print(type(games[0]))

    # print(games[0])

    filterGamesByScore(games, 95)
    filterGamesByConsole(games, "Playstation 3")

main()