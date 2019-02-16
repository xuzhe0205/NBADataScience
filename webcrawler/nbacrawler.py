"""
Author: Zhe Xu
"""
import requests
import lxml.html as lh
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import collections
import time
import csv
import urllib

class NBACrawler(object):
    def __init__(self, myURL):
        self.driver = webdriver.Chrome(executable_path='/Users/Oliver/Miscellaneous/chromedriver')
        self.driver.get(myURL)
        time.sleep(2)
    def scrapeTeamStats(self, fileName):
        fpath = '/Users/Oliver/Desktop/NEU/IS6105/001443089_5_Zhe_Xu/data/'
        csv_file = open(fpath + fileName, 'wb')
        writer = csv.writer(csv_file)
        writer.writerow(['TEAM', 'GP', 'W', 'L', 'WIN%', 'MIN', 'PTS', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', \
                        'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', '+/-'])

        teamStats = self.driver.find_elements_by_xpath('/html/body/main/div[2]/div/div[2]/div/div/nba-stat-table/div[2]/div[1]/table/tbody/tr')
       
        cnt = 0
        for stats in teamStats:
            teams_dict = collections.OrderedDict()
            link = stats.find_element_by_xpath('.//td[2]/a').get_attribute('href')
            teamName = stats.find_element_by_xpath('.//td[2]').text
            gp = stats.find_element_by_xpath('.//td[3]').text
            w = stats.find_element_by_xpath('.//td[4]').text
            l = stats.find_element_by_xpath('.//td[5]').text
            Winper = stats.find_element_by_xpath('.//td[6]').text
            Min = stats.find_element_by_xpath('.//td[7]').text
            Pts = stats.find_element_by_xpath('.//td[8]').text
            FGM = stats.find_element_by_xpath('.//td[9]').text
            FGA = stats.find_element_by_xpath('.//td[10]').text
            FGper = stats.find_element_by_xpath('.//td[11]').text
            threePM = stats.find_element_by_xpath('.//td[12]').text
            threePA = stats.find_element_by_xpath('.//td[13]').text
            threePper = stats.find_element_by_xpath('.//td[14]').text
            FTM = stats.find_element_by_xpath('.//td[15]').text
            FTA = stats.find_element_by_xpath('.//td[16]').text
            FTper = stats.find_element_by_xpath('.//td[17]').text
            OReb = stats.find_element_by_xpath('.//td[18]').text
            DReb = stats.find_element_by_xpath('.//td[19]').text
            Reb = stats.find_element_by_xpath('.//td[20]').text
            Ast = stats.find_element_by_xpath('.//td[21]').text
            TOv = stats.find_element_by_xpath('.//td[22]').text
            Stl = stats.find_element_by_xpath('.//td[23]').text
            Blk = stats.find_element_by_xpath('.//td[24]').text
            BlkA = stats.find_element_by_xpath('.//td[25]').text
            PF = stats.find_element_by_xpath('.//td[26]').text
            PFD = stats.find_element_by_xpath('.//td[27]').text
            plusMinus = stats.find_element_by_xpath('.//td[28]').text
            teams_dict['Team'+str(cnt)] = teamName
            teams_dict['GP'+str(cnt)] = gp
            teams_dict['W'] = w
            teams_dict['L'] = l
            teams_dict['Winper'] = Winper
            teams_dict['Min'] = Min
            teams_dict['Pts'] = Pts
            teams_dict['FGM'] = FGM
            teams_dict['FGA'] = FGA
            teams_dict['FGper'] = FGper
            teams_dict['threePM'] = threePM
            teams_dict['threePA'] = threePA
            teams_dict['threePper'] = threePper
            teams_dict['FTM'] = FTM
            teams_dict['FTA'] = FTA
            teams_dict['FTper'] = FTper
            teams_dict['OReb'] = OReb
            teams_dict['DReb'] = DReb
            teams_dict['Reb'] = Reb
            teams_dict['Ast'] = Ast
            teams_dict['TOv'] = TOv
            teams_dict['Stl'] = Stl
            teams_dict['Blk'] = Blk
            teams_dict['BlkA'] = BlkA
            teams_dict['PF'] = PF
            teams_dict['PFD'] = PFD
            teams_dict['plusMinus'] = plusMinus
            writer.writerow(teams_dict.values())
            cnt += 1
        csv_file.close()

    def scrapeTeamAdvStats(self, fileName):
        fpath = '/Users/Oliver/Desktop/NEU/IS6105/001443089_5_Zhe_Xu/data/'
        csv_file = open(fpath + fileName, 'wb')
        writer = csv.writer(csv_file)
        writer.writerow(['TEAM', 'GP', 'W', 'L', 'MIN', 'OFFRTG', 'DEFRTG', 'NETRTG', 'AST%', 'AST/TO', 'AST RATIO', 'OREB%', 'DREB%', 
                        'REB%', 'TOV%', 'EFG%', 'TS%', 'PACE', 'PIE'])
        soup = BeautifulSoup(self.driver.page_source,"lxml")
        teamAdvDiv = soup.find('div', {'class': 'nba-stat-table__overflow'})
        teamAdvTrs = ((teamAdvDiv.find('table')).find('tbody')).find_all('tr')
        c = 0
        for tr in teamAdvTrs:
            tds = tr.find_all('td')
            teams_dict = collections.OrderedDict()
            teams_dict['Team'] = tds[1].text
            teams_dict['GP'] = tds[2].text
            teams_dict['W'] = tds[3].text
            teams_dict['L'] = tds[4].text
            teams_dict['Min'] = tds[5].text
            teams_dict['OFFRTG'] = tds[6].text
            teams_dict['DEFRTG'] = tds[7].text
            teams_dict['NETRTG'] = tds[8].text
            teams_dict['AST%'] = tds[9].text
            teams_dict['AST/TO'] = tds[10].text
            teams_dict['AST RATIO'] = tds[11].text
            teams_dict['OREB%'] = tds[12].text
            teams_dict['DREB%'] = tds[13].text
            teams_dict['REB%'] = tds[14].text
            teams_dict['TOV%'] = tds[15].text
            teams_dict['EFG%'] = tds[16].text
            teams_dict['TS%'] = tds[17].text
            teams_dict['PACE'] = tds[18].text
            teams_dict['PIE'] = tds[19].text
            writer.writerow(teams_dict.values())
        csv_file.close()
        



nbaCrawler = NBACrawler("https://stats.nba.com/teams/advanced/?sort=W&dir=-1&Season=2017-18&SeasonType=Playoffs")
nbaCrawler.scrapeTeamAdvStats('nbateamadvancedplayoff2018.csv')