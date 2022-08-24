"""
Web scraping code
"""
from bs4 import BeautifulSoup
import requests
import csv
import json

def projections(): #finding bleacherreports predictions for team records in 2022-2023
    projections = requests.get("https://bleacherreport.com/articles/10042148-overunder-win-predictions-for-every-nfl-team-in-2022").text
    soup = BeautifulSoup(projections, 'lxml')

    #created a csv file to add the data to
    csv_file = open('bleacherreport_projections.csv', 'w', newline = '')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Team', 'Record Prediction'])

    teams = []
    records = []
    for team in soup.find_all('div', class_='organism contentStream slide'):
        #finding each team name and adding it
        if len(team.h1.text.split()) <= 3:
            teams.append(team.h1.text)
    for record in soup.find_all('ol'):
        try:
            wincount = record.find_all('p', class_='')[1].text #if multiple lines in one section, use indexing to grab a specific one
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

def total_spending(): #finding how much each team spent on each position
    money_spent = requests.get('https://overthecap.com/positional-spending').text
    soup = BeautifulSoup(money_spent, 'lxml')

    csv_file = open('team_money_spent.csv', 'w', newline = '')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Team', 'QB', 'RB', 'WR', 'OL', 'Offense', 'DL', 'LB', 'S', 'CB', 'Defense'])

    year = soup.find('div', id='y2022') #finding the specific section for the year
    for team in year.find_all('tr', class_='sortable'):
        Team_data = []
        counter = 0
        linemen = 0
        for money in team.find_all('td'):
            if counter == 4: #using a counter to find the money for certain positons
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

def win_loss(): #finding each teams win percentage in the previous season
    win_loss = requests.get('https://www.teamrankings.com/nfl/trends/win_trends/?sc=is_regular_season').text
    soup = BeautifulSoup(win_loss, 'lxml')

    csv_file = open('team_win_percentage.csv', 'w', newline = '')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Team', 'Win Percentage'])

    parser = soup.find('tbody')
    for team in parser.find_all('tr'):
        team_data = []
        for data in team.find_all('td'):
            if (data.text.replace(' ', '').isalpha()) or ('%' in data.text): #checking for each certain condition within the html code
                team_data.append((data.text).strip('%'))
        csv_writer.writerow(team_data)
    
    csv_file.close()

def strength_of_schedule(): #finding each teams strength of schedule in 2022-2023
    strength_of_schedule = requests.get('https://eatdrinkandsleepfootball.com/schedule/strength-of-schedule.html').text
    soup = BeautifulSoup(strength_of_schedule, 'lxml')

    csv_file = open('strength_of_schedule.csv', 'w', newline = '')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Team', 'Strength of Schedule']) 

    parser = soup.find('div', id='content')
    for team in parser.find_all('tr'):
        team_strength = [team.find_all('td')[1].text, team.find_all('td')[3].text] #find_all returns a list, so indexing is used to find the specific values
        csv_writer.writerow(team_strength)
    
    csv_file.close()

def team_receiving(): #finding the receiving stats of each team
    csv_file = open('team_receiving.csv', 'w', newline = '')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Team', 'Touchdowns', 'Receiving Yards', 'Y/R'])

    #using a football API to get JSON data for team passing stats
    headers = {"X-RapidAPI-Key": "c2c317b721msh130b59a39209c44p1e3a6fjsnc8102dec7b4d",
        "X-RapidAPI-Host": "nfl-team-stats.p.rapidapi.com"}
    response = requests.get("https://nfl-team-stats.p.rapidapi.com/v1/nfl-stats/teams/receiving-stats/offense/2021", headers=headers).text

    #taking the JSON response in string form, and turning it into a python dictionary
    json_data = json.loads(response)
    
    #parsing through the JSON data to turn it into a CSV file
    for team in json_data:
        team_stats = [team['name'], team['touchdowns'], team['yards'], round(team['yards']/team['receives'], 2)]
        csv_writer.writerow(team_stats)

    csv_file.close()

def team_passing(): #finding advanced passing stats of each team
    source = requests.get('https://www.nfl.com/stats/team-stats/offense/passing/2021/reg/all').text
    soup = BeautifulSoup(source, 'lxml')

    csv_file = open('team_passing.csv', 'w', newline = '')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Team', 'Completion Percentage', 'Y/A', 'QBR']) 

    parser = soup.find('tbody')
    turnover = []
    for team in parser.find_all('tr'):
        stats = []
        stats.append(team.find('div', class_='d3-o-club-fullname').text)
        team_stats = team.find_all('td')
        stats.extend([team_stats[3].text, team_stats[4].text, team_stats[8].text])
        turnover.append([team.find('div', class_='d3-o-club-fullname').text, team_stats[7].text, team_stats[-2].text, team_stats[-1].text])
        csv_writer.writerow(stats)

    csv_file.close()
    #return turnover (used for the turnover function)

def team_rushing(): #finding the rushing stats of each team
    source = requests.get('https://www.nfl.com/stats/team-stats/offense/rushing/2021/reg/all').text
    soup = BeautifulSoup(source, 'lxml')

    csv_file = open('team_rushing.csv', 'w', newline = '')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Team', 'Rushing Yards', 'YPC', 'Touchdowns']) 

    parser = soup.find('tbody')
    turnover = []
    for team in parser.find_all('tr'):
        stats = []
        stats.append(team.find('div', class_='d3-o-club-fullname').text)
        team_stats = team.find_all('td')
        stats.extend([team_stats[2].text, team_stats[3].text, team_stats[4].text])
        turnover.append([team.find('div', class_='d3-o-club-fullname').text, team_stats[10].text])
        csv_writer.writerow(stats)

    csv_file.close()
    #return turnover (used for the turnover function)

def turnovers(): #finding each teams turnovers and offensive blunders
    passing = team_passing()
    rushing = team_rushing()

    csv_file = open('turnovers.csv', 'w', newline = '')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Team', 'Interceptions', 'Sacks', 'Sack Yards', 'Fumbles'])

    for p, r in zip(passing, rushing):
        p.extend([r[1]])
        csv_writer.writerow(p)

    csv_file.close()

def age(): #finding the average age of each team, since younger players get better over time
    source = requests.get('https://www.phillyvoice.com/ranking-nfl-teams-age-after-53-man-cutdowns-jets-bears-texans-eagles-2021-edition/').text
    soup = BeautifulSoup(source, 'lxml')

    csv_file = open('average_age.csv', 'w', newline = '')
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Team', 'Average Age'])

    parser = soup.find('tbody')
    for team in parser.find_all('tr'):
        team_age = team.find_all('td')
        if team_age[0].text == 'Team':
            continue
        csv_writer.writerow([team_age[0].text, team_age[1].text[:4]])

    csv_file.close()

def offensiveppg():
    source = requests.get('https://www.teamrankings.com/nfl/stat/points-per-game').text
    soup = BeautifulSoup(source, 'lxml')

    csv_file = open('offensive_ppg.csv', 'w', newline='')
    csv_writer=csv.writer(csv_file)
    csv_writer.writerow(['Team', 'Offensive PPG'])
    
    parser = soup.find('tbody')
    for team in parser.find_all('tr'):
        teamstats = team.find_all('td')
        csv_writer.writerow([teamstats[1].text, teamstats[2].text])

    csv_file.close()

def defensiveppg():
    source = requests.get('https://www.teamrankings.com/nfl/stat/opponent-points-per-game').text
    soup = BeautifulSoup(source, 'lxml')

    csv_file = open('defensive_ppg.csv', 'w', newline='')
    csv_writer=csv.writer(csv_file)
    csv_writer.writerow(['Team', 'Defensive PPG'])

    parser = soup.find('tbody')
    for team in parser.find_all('tr'):
        teamstats = team.find_all('td')
        csv_writer.writerow([teamstats[1].text, teamstats[2].text])

    csv_file.close()
