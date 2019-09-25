#- Import packages
import random
import pandas as pd
from datetime import datetime as dt
from datetime import timedelta as td

'''
@module: Travel Dataset Generator
@authors: Leonardo Mauro <leomaurodesenv>
@link: https://github.com/Argo-Solutions/travel-dataset-generator GitHub
@license:  Creative Commons BY License
@copyright: 2019 Argo Solutions
@access: public
'''

#- Definitions
travelCode = 0


#- Functions
def df2Dict(df):
    '''
    Convert dataframe into dict
    '''
    procDict = dict()
    tmp = df.to_dict('split')
    data = tmp['data'][0]
    for (i, column) in enumerate(tmp['columns']):
        procDict[column] = data[i]
    return procDict


def funcTravelsSimulated(companies, flightsPossibilities, lodgesPossibilities, travelDate, travelsDays, travelWithLodge, placesName):
    '''
    Elaborate random travels with flights and lodges, based on possibilities.
    - flightsPossibilities: possible flights
    - lodgesPossibilities: possible hotels
    '''
    global travelCode
    dfFlightsPos = pd.DataFrame(flightsPossibilities)
    dfLodgesPos = pd.DataFrame(lodgesPossibilities)
    flightsSimulated, lodgesSimulated = list(), list()
    for (_companyName, companyData) in companies.items():
        for user in companyData['users']:
            date = travelDate['init']
            for _ in range(user['flights']):
                # random - days, places, hotel?
                daysFlight = random.randint(travelsDays['min'], travelsDays['max'])
                daysNextTravel = random.randint(travelDate['interval']['min'], travelDate['interval']['min'])
                fromPlace, toPlace = random.sample(placesName, 2)
                chanceTravelWithLodge = (random.randrange(100) < travelWithLodge*100)
                # travels
                fromConditions = (dfFlightsPos['from']==fromPlace) & (dfFlightsPos['to']==toPlace)
                tmpFlightFrom  = df2Dict(dfFlightsPos[fromConditions].sample(n=1))
                toConditions = (dfFlightsPos['from']==toPlace) & (dfFlightsPos['to']==fromPlace) & \
                               (dfFlightsPos['agency']==tmpFlightFrom['agency']) & \
                               (dfFlightsPos['flightType']==tmpFlightFrom['flightType'])
                tmpFlightTo  = df2Dict(dfFlightsPos[toConditions])
                tmpFlightFrom['userCode'] = tmpFlightTo['userCode'] = user['code']
                tmpFlightFrom['travelCode'] = tmpFlightTo['travelCode'] = travelCode
                tmpFlightFrom['date'] = date
                tmpFlightTo['date']   = date + td(days=daysFlight)
                # lodge
                if chanceTravelWithLodge:
                    lodgeConditions = (dfLodgesPos['place']==toPlace)
                    tmpLodge = df2Dict(dfLodgesPos[lodgeConditions])
                    tmpLodge['userCode'] = user['code']
                    tmpLodge['date'] = date
                    tmpLodge['days'] = daysFlight
                    tmpLodge['total'] = round(tmpLodge['price'] * daysFlight, 2)
                    tmpLodge['travelCode'] = travelCode
                    lodgesSimulated.append(tmpLodge)
                # save and update data
                flightsSimulated.append(tmpFlightFrom)
                flightsSimulated.append(tmpFlightTo)
                travelCode += 1
                date = dt.now() + td(days=daysNextTravel)
    return flightsSimulated, lodgesSimulated
