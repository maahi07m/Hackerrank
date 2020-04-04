import json
import csv
data = '''
{
  "states": [
    {
      "name": "Alabama",
      "abbreviation": "AL"
    },
    {
      "name": "Alaska",
      "abbreviation": "AK"
    },
    {
      "name": "Arizona",
      "abbreviation": "AZ"
    },
    {
      "name": "Arkansas",
      "abbreviation": "AR"
    },
    {
      "name": "California",
      "abbreviation": "CA"
    },
    {
      "name": "Colorado",
      "abbreviation": "CO"
    },
    {
      "name": "Connecticut",
      "abbreviation": "CT"
    },
    {
      "name": "Delaware",
      "abbreviation": "DE"
    },
    {
      "name": "Florida",
      "abbreviation": "FL"
    },
    {
      "name": "Georgia",
      "abbreviation": "GA"
    },
    {
      "name": "Hawaii",
      "abbreviation": "HI"
    }]}'''


json_obj = json.loads(data)


country =json_obj['states']
head = ['name','abbreviation']

#print(country)
    



with open('names.csv','w') as f:
    w = csv.DictWriter(f,fieldnames=head)
    w.writeheader()
    w.writerows(country)
  
    

