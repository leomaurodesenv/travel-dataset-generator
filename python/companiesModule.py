#- Import packages
import names
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
def funcUserGenerator(genders, agesInterval, flightsInterval, code):
    '''
    Generate random user, based on predefinitions.
    - genders: list
    - agesInterval {min, max}: user age
    - flightsInterval {min, max}: number of flights
    - code: user ID
    '''
    user = dict()
    user['code'] = code
    user['gender'] = genders[random.randint(0, len(genders)-1)]
    gender = user['gender'] if (user['gender'] != 'none') else False
    user['name'] = names.get_full_name(gender=gender)
    user['age'] = random.randint(agesInterval['min'], agesInterval['max'])
    user['flights'] = random.randint(flightsInterval['min'], flightsInterval['max'])
    return user
