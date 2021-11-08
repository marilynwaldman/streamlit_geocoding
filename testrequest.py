import pandas as pd
import streamlit
import requests

from census import Census
from us import states

with open('../census_key.txt') as key:
    api_key=key.read().strip()
print(api_key) 

c = Census(api_key)
c.acs5.get(('NAME', 'B25034_010E'),
          {'for': 'state:{}'.format(states.MD.fips)})


# http://127.0.01:5000/ is from the flask api
#response = request.get("http://127.0.01:5000/")
#print(response.json())
#data_table1 = pd.DataFrame(response.json())
#st.write(data_table1)

#response = requests.get("https://example.com", verify=False)
#print(response.status_code)
#print(response)



with open('../census_key.txt') as key:
    api_key=key.read().strip()
print(api_key)    
 

