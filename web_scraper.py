"""https://eatdrinkandsleepfootball.com/schedule/strength-of-schedule.html
https://rapidapi.com/DathanStoneDev/api/nfl-team-stats/
use total spending for offense/defense, spending for 
crucial positions(corner, linebacker, QB, WR), record from the previous season, 
stats from last season(passing, receiving, rushing), schedule difficulty"""

from bs4 import BeautifulSoup
import requests
import csv

def projections():
    projections = requests.get("https://bleacherreport.com/articles/10042148-overunder-win-predictions-for-every-nfl-team-in-2022").text
    soup = BeautifulSoup(projections, 'lxml')

    csv_file = open('projections.csv', 'w', newline = '')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Team', 'Record Prediction'])

    teams = []
    records = []
    for team in soup.find_all('div', class_='organism contentStream slide'):
        if len(team.h1.text.split()) <= 3:
            teams.append(team.h1.text)
    for record in soup.find_all('ol'):
        try:
            wincount = record.find_all('p', class_='')[1].text
            if 'Over/Under' in wincount:
                win = ''
                for letter in wincount:
                    if letter.isdigit() or letter == '.':
                        win += letter
                records.append(win)
        except:
            pass

    for team, record in zip(teams, records):
        csv_writer.writerow([team, record])

    csv_file.close()

def total_spending():
    money_spent = requests.get('https://overthecap.com/positional-spending').text
    soup = BeautifulSoup(money_spent, 'lxml')

    csv_file = open('team_money_spent.csv', 'w', newline = '')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Team', 'QB', 'RB', 'WR', 'OL', 'Offense', 'DL', 'LB', 'S', 'CB', 'Defense'])

    year = soup.find('div', id='y2022')
    for team in year.find_all('tr', class_='sortable'):
        Team_data = []
        counter = 0
        linemen = 0
        for money in team.find_all('td'):
            if counter == 4:
                pass
            elif counter == 7 or counter == 8:
                linemen += int(money.text.strip('$').replace(',', ''))
                if counter == 8:
                    Team_data.append(str(linemen))
            else:
                Team_data.append(money.text.strip('$').replace(',', ''))
            counter += 1

        csv_writer.writerow(Team_data)

    csv_file.close()

def win_loss():
    win_loss = requests.get('https://www.teamrankings.com/nfl/trends/win_trends/?sc=is_regular_season').text
    soup = BeautifulSoup(win_loss, 'lxml')

    csv_file = open('team_win_percentage.csv', 'w', newline = '')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Team', 'Win Percentage'])

    parser = soup.find('tbody')
    for team in parser.find_all('tr'):
        team_data = []
        for data in team.find_all('td'):
            if (data.text.replace(' ', '').isalpha()) or ('%' in data.text):
                team_data.append((data.text).strip('%'))
        csv_writer.writerow(team_data)
    
    csv_file.close()

def strength_of_schedule():
    strength_of_schedule = requests.get('https://eatdrinkandsleepfootball.com/schedule/strength-of-schedule.html').text
    soup = BeautifulSoup(strength_of_schedule, 'lxml')

    #csv_file = open('strength_of_schedule.csv', 'w', newline = '')
    #csv_writer = csv.writer(csv_file)
    #csv_writer.writerow(['Team', 'Strength of Schedule']) 

    parser = soup.find()
