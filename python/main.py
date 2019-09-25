# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Travel Dataset Generator
# https://github.com/Argo-Solutions/travel-dataset-generator
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#- Import packages
import pandas as pd
from datetime import datetime as dt

#- Local packages
import companiesModule
import agenciesModule
import placesModule
import lodgesModule
import travelsPosModule
import travelsModule


#-----------------------------------------------------
#- Configurations
#-- Companies and Users
defGenders = ['male', 'female', 'none']
defAgesInterval = {'min': 23, 'max': 50}
defFlightsInterval = {'min': 0, 'max': 3}
defCompanies = {
    'HHD': {'usersCount': 2},
    '4You': {'usersCount': 3},
}

#-- Flight Agencies
defAgencies = dict()
defFlightTypes = {
    'economic': {'price': 1.0},
    'premium': {'price': 1.5},
}
defAgenciesName = ['FlyingDrops', 'Rainbow', 'CloudFy']

#-- Places
defPlacesName = ['Sao Paulo (SP)', 'Rio de Janeiro (RJ)', 'Santa Catarina (SC)']
defPlaces = {name: dict() for name in defPlacesName}
defDistancesInterval = {'min': 200.0, 'max': 850.0}
defPlaceTravelKmPerHour = 400.0

#-- Lodge (Accommodation)
defLodgesInterval = {'min': 1, 'max': 3}
defLodgesPrices   = {'min': 60.0, 'max': 200.0}
defLodges = {name: list() for name in defPlacesName}

#-- Travel
defTravels = list()
defTravelsDays = {'min': 1, 'max': 3}
defTravelsFlightPrices = {'init': 300.0, 'interval': 100.0}
defTravelWithLodge = 0.4
defTravelDate = {'init': dt.now(), 'interval':{'min': 10, 'max': 60}}

#-- Output
defOutputFolder  = '../output'
defOutputUsers   = ['code', 'company', 'name', 'gender', 'age']
defOutputFlights = ['travelCode', 'userCode', 'from', 'to', 'flightType', \
                    'price', 'time', 'distance', 'agency', 'date']
defOutputLodges  = ['travelCode', 'userCode', 'name', 'place', 'days', 'price', 'total', 'date']


#-----------------------------------------------------
#- Functions
def getCompanies(defCompanies):
    userId = 0
    companies = defCompanies.copy()
    for company, data in companies.items():
        users = list()
        for _ in range(data['usersCount']):
            user = companiesModule.funcUserGenerator(defGenders, defAgesInterval, defFlightsInterval, userId)
            users.append(user)
            userId += 1
        companies[company]['users'] = users
    return companies


def getAgencies(defAgencies, defAgenciesName):
    agencies = defAgencies.copy()
    for agency in defAgenciesName:
        agencies[agency] = agenciesModule.funcAgencyGenerator(defFlightTypes)
    return agencies


def getPlaces(defPlaces, defPlacesName, defDistancesInterval, defPlaceTravelKmPerHour):
    places = defPlaces.copy()
    n = len(defPlacesName)
    for i in range(n):
        for j in range(i, n):
            fromPlace = defPlacesName[i]
            toPlace = defPlacesName[j]
            distance, time, msg = placesModule.funcPlaceGenerator(i, j, defDistancesInterval, defPlaceTravelKmPerHour)
            if distance and time:
                place = {'distance': distance, 'time': time, 'timeMsg': msg}
                places[fromPlace][toPlace] = place
                places[toPlace][fromPlace] = place
    return places


def getLodges(defPlacesName, defLodges, defLodgesInterval, defLodgesPrices):
    lodges = defLodges.copy()
    for name in defPlacesName:
        lodge = lodgesModule.funcLodgesGenerator(defLodgesInterval, defLodgesPrices)
        lodges[name] = lodge
    return lodges


def getUsers(companies):
    users = list()
    for companyName, companyData in companies.items():
        for user in companyData['users']:
            user['company'] = companyName
            users.append(user)
    return users


def df2csvOutput(df, columns, path, fileName):
    if len(df) == 0:
        return
    if 'date' in columns:
        df['date'] = df.apply(lambda x: x['date'].strftime("%m/%d/%Y"), axis=1)
    df[columns].to_csv('%s/%s.csv' % (path, fileName), index=False, header=True)



#-----------------------------------------------------
#- Main script
def main():
    #-------------------------------------------------
    #- Companies and users
    companies = getCompanies(defCompanies)

    #- Flight agencies
    agencies = getAgencies(defAgencies, defAgenciesName)

    #- Places to travel
    places = getPlaces(defPlaces, defPlacesName, \
                       defDistancesInterval, defPlaceTravelKmPerHour)

    #- Hotels
    lodges = getLodges(defPlacesName, defLodges, defLodgesInterval, defLodgesPrices)

    #-------------------------------------------------
    #- Simulation
    flightsPossibilities = travelsPosModule.funcFlightsPossibilities(places, agencies, defTravelsFlightPrices, defFlightTypes)
    lodgesPossibilities  = travelsPosModule.funcLodgesPossibilities(lodges, defPlacesName)
    flightsSimulated, lodgesSimulated = \
        travelsModule.funcTravelsSimulated(companies, flightsPossibilities, lodgesPossibilities, \
            defTravelDate, defTravelsDays, defTravelWithLodge, defPlacesName)

    #-------------------------------------------------
    #- Save data
    dfUsers   = pd.DataFrame(getUsers(companies))
    dfFlights = pd.DataFrame(flightsSimulated)
    dfLodges  = pd.DataFrame(lodgesSimulated)

    df2csvOutput(dfUsers, defOutputUsers, defOutputFolder, 'users')
    df2csvOutput(dfFlights, defOutputFlights, defOutputFolder, 'flights')
    df2csvOutput(dfLodges, defOutputLodges, defOutputFolder, 'hotels')


if __name__ == "__main__":
    main()