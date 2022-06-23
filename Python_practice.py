counties = ["Arapahoe","Denver","Jefferson"]

if counties[1] == 'Denver':
    print(counties[1])

#-----------------------

if "elpaso" in counties:
    print("el Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

#---------------
if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

#---------------------------

for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[i])

    counties_tuple = ("Arapahoe","Denver","Jefferson").

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)
