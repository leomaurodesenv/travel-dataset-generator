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
def funcAgencyGenerator(flightTypes):
    '''
    Generate random agency services, based on predefinitions.
    - flightTypes: types of flight
    '''
    agency = dict()
    types = list(flightTypes.copy().keys())
    random.shuffle(types)
    typesMany = random.randint(1, len(types))
    agency['types'] = [types[i] for i in range(typesMany)]
    return agency
