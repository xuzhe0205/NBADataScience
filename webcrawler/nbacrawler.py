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

class NBACrawler(object):
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='/Users/Oliver/Miscellaneous/chromedriver')
        self.driver.get('http://stats.nba.com/teams/traditional/#!?sort=W_PCT&dir=-1')
        time.sleep(2)
    def scrapeTeamStats(self):

        csv_file = open('nbateamstats.csv', 'wb')
        writer = csv.writer(csv_file)
        writer.writerow(['TEAM', 'GP', 'W', 'L', 'WIN%', 'MIN', 'PTS', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', \
                        'OREB', 'DREB', 'REB', 'AST', 'TOV', 'STL', 'BLK', 'BLKA', 'PF', 'PFD', '+/-'])

        # url='https://stats.nba.com/teams/traditional/?sort=W_PCT&dir=-1'

        # driver.get(url)
        # html = driver.page_source
        # soup = BeautifulSoup(html, "lxml")
        # table = soup.find_all('table', {'id':'team-stats-per_game'})
        # page = requests.get(url)

        # doc = lh.fromstring(page.content)

        # soup = BeautifulSoup(page.text, 'lxml')

        # headrow = soup.findAll('thead', class_='table_outer_container')

        # table_tags = soup.select("table")

        # teamPGtable = soup.find('table', id="team-stats-per_game")
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


nbaCrawler = NBACrawler()
nbaCrawler.scrapeTeamStats()