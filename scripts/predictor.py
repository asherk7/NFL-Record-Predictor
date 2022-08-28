"""
Uses the model creates to predict a team record using user statistic predictions
"""
import joblib
from scripts.teamdata import predictorinfo

class Predictor:
    def __init__(self, team, defppg, offppg, passtd, passyrd, rushyrd, ypc, rushtd, interception, fumble):
        self.model = joblib.load('Models\\DTR_model.model')
        teamstats = predictorinfo(team)
        self.team=team
        self.schedule = teamstats[0] #schedule for 2022-2023
        self.offense = teamstats[1] #spending for offense
        self.defense = teamstats[2] #spending for defense
        self.completionpct = teamstats[3]
        self.ypa = teamstats[4]
        self.qbr = teamstats[5]
        self.sack = teamstats[6]
        self.sackyrd = teamstats[7]
        self.fg = teamstats[8]
        self.punt = teamstats[9]
        self.kickoff = teamstats[10]
        self.yrdperrec = teamstats[11]
        self.defppg = defppg
        self.offppg = offppg
        self.passtd = passtd
        self.passyrd = passyrd
        self.rushyrd = rushyrd
        self.ypc = ypc
        self.rushtd = rushtd
        self.interception = interception
        self.fumble = fumble

    def winpct_to_record(self, pct):
        win = round(((int(pct)/100)*17))
        loss = round(17-((int(pct)/100)*17))
        record = f'{win}-{loss}-0'
        return record

    def get_prediction(self):
        user_pred = self.model.predict([[self.defppg, self.offppg, self.fg, self.punt, 
                                        self.kickoff, self.schedule, self.offense, self.defense, 
                                        self.completionpct, self.ypa, self.qbr, self.passtd, 
                                        self.passyrd, self.yrdperrec, self.rushyrd, self.ypc, 
                                        self.rushtd, self.interception, self.sack, self.sackyrd, self.fumble]])
        record = self.winpct_to_record(user_pred)
        return record
