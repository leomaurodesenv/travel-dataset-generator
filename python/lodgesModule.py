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

#- Definitions
defName = 'A'
defLodgesPrex = 'Hotel'


#- Functions
def getNextChar(text):
    '''
    Generate order alphabetic.
    - text: input text
    '''
    if len(text) == 0:
        return 'A'
    nextChar = chr(ord(text[-1]) + 1)
    if nextChar <= 'Z':
        text = text[:-1] + nextChar
    else:
        text = getNextChar(text[:-1]) + 'A'
    return text


def funcLodgesGenerator(lodgesInterval, lodgesPrices):
    '''
    Generate random lodges, based on predefinitions.
    - lodgesInterval {min, max} values: number of hotels
    - lodgesPrices {min, max} values: hotel range
    '''
    global defName
    lodges = list()
    n = random.randint(lodgesInterval['min'], lodgesInterval['max'])
    for i in range(n):
        lodgeName = '%s %s' % (defLodgesPrex, defName)
        price = round(random.uniform(lodgesPrices['min'], lodgesPrices['max']), 2)
        lodge = {'code': defName, 'name': lodgeName, 'price': price}
        lodges.append(lodge)
        defName = getNextChar(defName)
    return lodges
