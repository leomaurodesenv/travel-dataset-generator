# travel-dataset-generator

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8fcf18fb09594cbe8a8bdf0f7493b2f5)](https://www.codacy.com/manual/leomaurodesenv/travel-dataset-generator?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=leomaurodesenv/travel-dataset-generator&amp;utm_campaign=Badge_Grade)

---

In this repository, we present the _first_ travel dataset generator of the GitHub.  

This dataset serves as a good base for **Data Mining** learning models, including, but not limited to, supervised learning (_e.g._ , Classification, Regression) and unsupervised learning (_e.g._ , Clustering).  

This generator produces flight and hotel data. Everything is randomly generated, for example, business users, hotels, travel, etc. See the `python/main.py` to understand the parameters.   

---
## Python

Run dataset generator `python/main.py`:
```shell
python main.py
```

Probabilities customization:
```python
#-----------------------------------------------------
#- Companies and Users
#-- Types of gender
defGenders = list(str, str, ...)
#-- Ages of users 
defAgesInterval = {'min': int, 'max': int}
#-- Number of flights by user
defFlightsInterval = {'min': int, 'max': int}
#-- Companies
#--- Number of users by company
defCompanies = {
    'ABC': {'usersCount': int},
    'DEC': {'usersCount': int}, ...
}
#-- Number of Places of a Company
defCompaniesPlacesInterval = {'min': int, 'max': int}

#-----------------------------------------------------
#- Flight Agencies
#-- Types of flight
#--- Weight of price by type
defFlightTypes = {
    'economic': {'price': float},
    'premium': {'price': float}, ...
}
#-- Names of agency
defAgenciesName = [str, str, ...]

#-----------------------------------------------------
#- Places
#-- Names of place
defPlacesName = [str, str, ...]
#-- Distances between cities
defDistancesInterval = {'min': float, 'max': float}
#-- Plain velocity - km/hour
defPlaceTravelKmPerHour = float 

#-----------------------------------------------------
#-- Lodges (Accommodation)
#--- Number of lodges by place
defLodgesInterval = {'min': int, 'max': int}
#--- Prices of lodges
defLodgesPrices   = {'min': float, 'max': float}

#-----------------------------------------------------
#- Travels
#-- Number of days of a travel
defTravelsDays = {'min': int, 'max': int}
#-- Flights prices
defTravelsFlightPrices = {'init': float, 'interval': float}
#-- Probabity of a flight with hotel
defTravelWithLodge = float # ranging [0, 1]
#-- Dates of the travels
defTravelDate = {'init': datetime, 'interval':{'min': int, 'max': int}}
```

---
## Notebook

Step-by-step of the generator:   
-   [Overview: Dataset Generator](jupyter/generator-example.ipynb)

---
## License

This generator is available for researchers and data scientists under the [Creative Commons BY](https://creativecommons.org/licenses/by/4.0/) license. In case of publication and/or public use, as well as any dataset derived from it, one should acknowledge its creators by citing us.  

---
## Also look ~

-   Created by [Argo Solutions](https://github.com/Argo-Solutions/) - <http://useargo.com>
