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


def funcElaborateflight(fromPlace, toPlace, distance, agency, flightType, price, \
                        time, timeMsg):
    '''
    Elaborate a possible flight.
    - fromPlace: from
    - toPlace: to
    - distance: distance
    - agency: agency name
    - flightType: flight type
    - price: flight price
    - time: time in hours
    - timeMsg: time calculated
    '''
    flight = {'from': fromPlace, 'to': toPlace, 'distance': distance,
              'agency': agency, 'flightType': flightType, 'price': price,
              'time': time, 'timeMsg': timeMsg}
    return flight


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
                        weight = flightTypes[typeA]['price']
                        price = funcCalculatePrice(priceA, priceB, weight)
                        flight = funcElaborateflight(fromPlace, toPlace, placeData['distance'], \
                                                     agencyName, typeA, price, placeData['time'], placeData['timeMsg'])
                        flightsPossibilities.append(flight)
                else:
                    typeA = agencyData['types'][0]
                    weight = flightTypes[typeA]['price']
                    price = funcCalculatePrice(priceA, priceB, weight)
                    flight = funcElaborateflight(fromPlace, toPlace, placeData['distance'], agencyName, \
                                                 typeA, price, placeData['time'], placeData['timeMsg'])
                    flightsPossibilities.append(flight)
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