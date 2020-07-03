# Scrape data of CSGO matches
import pandas as pd
from bs4 import BeautifulSoup as bs
import codecs

class Scrape():
    def __init__(self):
        super().__init__()

    # function to scrape data from HLTV.com
    def scrapeFromHLTV(self):

        html_doc = codecs.open("hltv.html", "r", "utf-8")

        root = bs(html_doc.read(), "html.parser")
        root.prettify()
        table = (str)(root.find("table",class_='stats-table no-sort'))
        data = pd.read_html(table)[0]

        # removes 'date' 'event' and 'year' coloumns
        data = data.drop(data.columns[[0,2,1]], axis=1)
        # Give columns proper names
        data.columns = ['Opponent', 'Map', 'result', 'Outcome']
        # Clean win/loss data and turn to numeric format for compatibilty with machine learning classifier
        data.loc[data.Outcome == 'W', 'Outcome'] = 1
        data.loc[data.Outcome == 'L', 'Outcome'] = 0
        data.loc[data.Outcome == 'T', 'Outcome'] = 0

        # Misc sanitation (datetime conversion, typecasting)
        data['Outcome'] = data['Outcome'].astype(str).astype(int)
        #data['Event'] = data['Event'].astype(str)
        #data['Date'] = pd.to_datetime(data['Date'])

        # convert team names to number
        data.loc[data.Opponent == 'Liquid', 'Opponent'] = 1
        data.loc[data.Opponent == 'Natus Vincere', 'Opponent'] = 2
        data.loc[data.Opponent == 'Vega Squadron', 'Opponent'] = 3
        data.loc[data.Opponent == 'FURIA', 'Opponent'] = 4
        data.loc[data.Opponent == 'Luminosity', 'Opponent'] = 5
        data.loc[data.Opponent == 'mousesports', 'Opponent'] = 6
        data.loc[data.Opponent == 'Cloud9', 'Opponent'] = 7
        data.loc[data.Opponent == 'FaZe', 'Opponent'] = 8
        data.loc[data.Opponent == 'NRG', 'Opponent'] = 9
        data.loc[data.Opponent == 'fnatic', 'Opponent'] = 10
        data.loc[data.Opponent == 'G2', 'Opponent'] = 11
        data.loc[data.Opponent == 'Envy', 'Opponent'] = 12
        data.loc[data.Opponent == 'Gambit', 'Opponent'] = 13
        data.loc[data.Opponent == 'HellRaisers', 'Opponent'] = 14
        data.loc[data.Opponent == 'North', 'Opponent'] = 15
        data.loc[data.Opponent == 'ENCE', 'Opponent'] = 16
        data.loc[data.Opponent == 'NiP', 'Opponent'] = 17
        data.loc[data.Opponent == 'Virtus.pro', 'Opponent'] = 18
        data.loc[data.Opponent == 'Dignitas', 'Opponent'] = 19
        data.loc[data.Opponent == 'x6tence', 'Opponent'] = 20
        data.loc[data.Opponent == 'FlipSid3', 'Opponent'] = 21
        data.loc[data.Opponent == 'CLG', 'Opponent'] = 22
        data.loc[data.Opponent == 'Method', 'Opponent'] = 23
        data.loc[data.Opponent == 'OpTic', 'Opponent'] = 24
        data.loc[data.Opponent == 'MIBR', 'Opponent'] = 25
        data.loc[data.Opponent == 'SK', 'Opponent'] = 26
        data.loc[data.Opponent == 'Heroic', 'Opponent'] = 27
        data.loc[data.Opponent == '100 Thieves', 'Opponent'] = 28
        data.loc[data.Opponent == 'GODSENT', 'Opponent'] = 29
        data.loc[data.Opponent == 'BIG', 'Opponent'] = 30
        data.loc[data.Opponent == 'Grayhound', 'Opponent'] = 31
        data.loc[data.Opponent == 'LDLC', 'Opponent'] = 32
        data.loc[data.Opponent == 'Complexity', 'Opponent'] = 33
        data.loc[data.Opponent == 'Vitality', 'Opponent'] = 34
        data.loc[data.Opponent == 'AGO', 'Opponent'] = 35
        data.loc[data.Opponent == 'Immortals', 'Opponent'] = 36
        data.loc[data.Opponent == 'PENTA', 'Opponent'] = 37
        data.loc[data.Opponent == 'Space Soldiers', 'Opponent'] = 38
        data.loc[data.Opponent == 'TYLOO', 'Opponent'] = 39
        data.loc[data.Opponent == 'AVANGAR', 'Opponent'] = 40
        data.loc[data.Opponent == 'CSGL', 'Opponent'] = 41
        data.loc[data.Opponent == 'Chiefs', 'Opponent'] = 42
        data.loc[data.Opponent == 'ViCi', 'Opponent'] = 43
        data.loc[data.Opponent == 'CR4ZY', 'Opponent'] = 44
        data.loc[data.Opponent == 'Spirit', 'Opponent'] = 45
        data.loc[data.Opponent == 'Renegades', 'Opponent'] = 46
        data.loc[data.Opponent == 'Evil Geniuses', 'Opponent'] = 47
        data.loc[data.Opponent == 'ex-3DMAX', 'Opponent'] = 48
        data.loc[data.Opponent == 'Tricked', 'Opponent'] = 49
        data.loc[data.Opponent == 'Windigo', 'Opponent'] = 50
        data.loc[data.Opponent == 'Giants', 'Opponent'] = 51
        data.loc[data.Opponent == 'Wizards', 'Opponent'] = 52
        data.loc[data.Opponent == 'TSM', 'Opponent'] = 53
        data.loc[data.Opponent == 'Kinguin', 'Opponent'] = 54
        data.loc[data.Opponent == 'Sharks', 'Opponent'] = 55
        data.loc[data.Opponent == 'OG', 'Opponent'] = 56
        data.loc[data.Opponent == 'MVP PK', 'Opponent'] = 57
        data.loc[data.Opponent == 'Torpedo', 'Opponent'] = 58
        data.loc[data.Opponent == 'Heretics', 'Opponent'] = 59
        data.loc[data.Opponent == 'Tempo Storm', 'Opponent'] = 60
        data.loc[data.Opponent == 'ALTERNATE aTTaX', 'Opponent'] = 61
        data.loc[data.Opponent == 'm1x', 'Opponent'] = 62
        data.loc[data.Opponent == 'HOLLYWOOD', 'Opponent'] = 63
        data.loc[data.Opponent == 'TheMongolz', 'Opponent'] = 64
        data.loc[data.Opponent == 'Rogue', 'Opponent'] = 65
        data.loc[data.Opponent == 'fish123', 'Opponent'] = 66
        data.loc[data.Opponent == 'DreamEaters', 'Opponent'] = 67
        data.loc[data.Opponent == 'Ghost', 'Opponent'] = 68
        data.loc[data.Opponent == 'X', 'Opponent'] = 69
        data.loc[data.Opponent == 'Aristocracy', 'Opponent'] = 70
        data.loc[data.Opponent == 'NewStyle', 'Opponent'] = 71
        data.loc[data.Opponent == 'sAw', 'Opponent'] = 72
        data.loc[data.Opponent == 'E-frag.net', 'Opponent'] = 73

        print(data)
        # Print resultant dataframe of all merged together top 10 team historic match results
        return data


if __name__ == '__main__':
    scrape = Scrape()
    scrape.scrapeFromHLTV()

