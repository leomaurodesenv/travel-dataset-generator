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
def funcPlaceGenerator(i, j, distInterval, kmPerHour):
    '''
    Generate random place distances, based on predefinitions.
    - i: number of place
    - j: number of place
    - distInterval {min, max} values: distance range
    - kmPerHour: km per hour of the plain
    '''
    if i == j:
        return False, False, False
    distance = round(random.uniform(distInterval['min'], distInterval['max']), 2)
    time = round(distance/kmPerHour, 2)
    hours = int(time)
    minutes = (time*60) % 60
    timeMsg = '%d:%dh' % (hours, minutes)
    return (distance, time, timeMsg)
