#- Import packages
import random

'''
@module: Travel Dataset Generator
@authors: Leonardo Mauro <leomaurodesenv>
@link: https://github.com/Argo-Solutions/travel-dataset-generator GitHub
@license:  Creative Commons BY License
@copyright: 2019 Argo Solutions
@access: public
'''

#- Functions
def funcCalculatePrice(priceMin, priceMax, weight):
    '''
    Calculate a random price for a travel.
    - priceMin: min price
    - priceMax: max price
    - weight: weight the price range
    '''
    priceMin = priceMin * weight
    priceMax = priceMax * weight
    price = round(random.uniform(priceMin, priceMax), 2)
    return price


def funcElaborateflight(arr, fromPlace, toPlace, distance, agency, flightTypes, flightType, \
                        priceA, priceB, time, timeMsg):
    '''
    Elaborate a possible flight.
    - fromPlace: from
    - toPlace: to
    - distance: distance
    - agency: agency name
    - flightType: flight type
    - priceA: min price interval
    - priceB: max price interval
    - time: time in hours
    - timeMsg: time calculated
    '''
    weight = flightTypes[flightType]['price']
    price = funcCalculatePrice(priceA, priceB, weight)
    flight = {'from': fromPlace, 'to': toPlace, 'distance': distance,
              'agency': agency, 'flightType': flightType, 'price': price,
              'time': time, 'timeMsg': timeMsg}
    arr.append(flight)


def funcFlightsPossibilities(places, agencies, flightPrices, flightTypes):
    '''
    Elaborate a list of possible flights.
    - places: places data
    - flightPrices: flight prices
    - flightTypes: flight types
    - agencies: agencies data
    '''
    flightsPossibilities = list()
    for fromPlace, toPlaces in places.items():
        toPlacesSorted = sorted(toPlaces.items(), key=lambda x:x[1]['distance'], reverse=False)
        priceA, priceB = flightPrices['init'], \
                         flightPrices['init'] + flightPrices['interval']
        for (toPlace, placeData) in toPlacesSorted:
            for (agencyName, agencyData) in agencies.items():
                if len(agencyData['types']) > 1: # has more than 1 element
                    for typeA in agencyData['types']:
                        funcElaborateflight(flightsPossibilities, fromPlace, toPlace, placeData['distance'], \
                                            agencyName, flightTypes, typeA, priceA, priceB, \
                                            placeData['time'], placeData['timeMsg'])
                else:
                    typeA = agencyData['types'][0]
                    funcElaborateflight(flightsPossibilities, fromPlace, toPlace, placeData['distance'], agencyName, flightTypes, \
                                        typeA, priceA, priceB, placeData['time'], placeData['timeMsg'])
            # Update prices for bigger distances
            priceA, priceB = priceB, priceB + flightPrices['interval']
    return flightsPossibilities


def funcLodgesPossibilities(lodges, placesName):
    '''
    Elaborate a list of possible hotels.
    - placesName: places names
    - lodges: lodges data
    '''
    lodgesPossibilities = list()
    for place in placesName:
        for lodge in lodges[place]:
            lodge = lodge.copy()
            lodge['place'] = place
            lodgesPossibilities.append(lodge)
    return lodgesPossibilities
