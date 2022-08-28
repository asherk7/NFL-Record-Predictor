import csv

def team_stats(teamname):
    with open('data\\clean\\offensive_ppg.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == teamname:
                teamdata = row
                break
    
    with open('data\\clean\\defensive_ppg.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == teamname:
                teamdata.append(row[1])
                break

    with open('data\\clean\\team_win_percentage.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == teamname:
                teamdata.append(row[1])
                break

    with open('data\\clean\\strength_of_schedule.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == teamname:
                teamdata.append(row[1])
                break

    with open('data\\clean\\team_receiving.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == teamname:
                teamdata.extend([row[2], row[1]])
                break

    with open('data\\clean\\team_rushing.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == teamname:
                teamdata.extend([row[1], row[3]])
                break

    with open('data\\clean\\special_teams.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == teamname:
                teamdata.append(str(round(float(row[1]), 2)))
                break
    
    return teamdata #team name, ppg, defensive ppg, win percentage, strength of schedule, passing stats, rushing stats

def BRprediction(teamname):
    with open('data\\clean\\bleacherreport_projections.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == teamname:
                return f'{row[1]}-{17-float(row[1])}-0'

def predictorinfo(teamname):
    teamstats = []

    with open('data\\clean\\strength_of_schedule2022.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == teamname:
                teamstats.append(row[1])
                break

    with open('data\\clean\\team_money_spent.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == teamname:
                teamstats.extend([row[5], row[10]])
                break

    with open('data\\clean\\team_passing.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == teamname:
                teamstats.extend([row[1], row[2], row[3]])
                break

    with open('data\\clean\\turnovers.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == teamname:
                teamstats.extend([row[2], row[3]])

    with open('data\\clean\\special_teams.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == teamname:
                teamstats.extend([row[1], row[2], row[3]])

    with open('data\\clean\\team_receiving.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == teamname:
                teamstats.append(row[3])

    return teamstats

def MLstats(teamname):
    ML_stats = [teamname]

    with open('data\\clean\\defensive_ppg.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == teamname:
                ML_stats.append(row[1])

    with open('data\\clean\\offensive_ppg.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == teamname:
                ML_stats.append(row[1])

    with open('data\\clean\\team_receiving.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == teamname:
                ML_stats.extend([row[1], row[2]])

    with open('data\\clean\\team_rushing.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == teamname:
                ML_stats.extend([row[1], row[2], row[3]])

    with open('data\\clean\\turnovers.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == teamname:
                ML_stats.extend([row[1], row[4]])

    return ML_stats
