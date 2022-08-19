import csv

def team_stats(teamname):
    with open('C:\\Users\\mashe\\Desktop\\NFL-Record-Predictor\\data\\offensive_ppg.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == teamname:
                teamdata = row
                break
    
    with open('C:\\Users\\mashe\\Desktop\\NFL-Record-Predictor\\data\\defensive_ppg.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == teamname:
                teamdata.append(row[1])
                break

    with open('C:\\Users\\mashe\\Desktop\\NFL-Record-Predictor\\data\\team_win_percentage.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == teamname:
                teamdata.append(row[1])
                break

    with open('C:\\Users\\mashe\\Desktop\\NFL-Record-Predictor\\data\\strength_of_schedule.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == teamname:
                teamdata.append(row[1])
                break

    with open('C:\\Users\\mashe\\Desktop\\NFL-Record-Predictor\\data\\team_receiving.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == teamname:
                teamdata.append(row[2])
                teamdata.append(row[1])
                break

    with open('C:\\Users\\mashe\\Desktop\\NFL-Record-Predictor\\data\\team_rushing.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == teamname:
                teamdata.append(row[1])
                teamdata.append(row[3])
                break
    
    return teamdata #team name, ppg, defensive ppg, win percentage, strength of schedule, passing stats, rushing stats
