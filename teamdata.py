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
                teamdata.append(row[2])
                teamdata.append(row[1])
                break

    with open('data\\clean\\team_rushing.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == teamname:
                teamdata.append(row[1])
                teamdata.append(row[3])
                break
    
    return teamdata #team name, ppg, defensive ppg, win percentage, strength of schedule, passing stats, rushing stats

def BRprediction(teamname):
    with open('data\\clean\\bleacherreport_projections.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == teamname:
                return f'{row[1]}-{17-float(row[1])}-0'