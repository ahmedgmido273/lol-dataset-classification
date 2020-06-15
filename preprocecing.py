import numpy as np 
import pandas as pd 

data = pd.read_csv('high_diamond_ranked_10min.csv')

normList = ['blueWardsPlaced', 'blueTotalGold',
    'blueTotalExperience', 
    'blueTotalMinionsKilled', 
    'blueTotalJungleMinionsKilled',
    'blueGoldDiff',
    'blueExperienceDiff',
    'blueCSPerMin',
    'blueGoldPerMin',
    'redWardsPlaced',
    'redWardsDestroyed',
    'redTotalGold',
    'redTotalExperience',
    'redTotalMinionsKilled',
    'redTotalJungleMinionsKilled',
    'redGoldDiff',
    'redExperienceDiff',
    'redCSPerMin',
    'redGoldPerMin'
    ]