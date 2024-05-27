import csv
from datetime import datetime
from pathlib import Path
import plotly.express as px


path = Path('/works/works_python/0527/world_fires_1_day.csv')

with open(path, newline = '') as csvfile:
     reader = csv.DictReader(csvfile)
     #예쁘게 대응시켜서 '':'','':'',로 딕셔너리화 할게요*** 이부분 중요 그래야 그래프화 할수있다
     dates, lats, lons, brights = [], [], [], []

     for row in reader:
          print(row)
          date = datetime.strptime(row['acq_date'], '%Y-%m-%d')
          dates.append(date)

          try:
               lat = float(row['latitude'])
               lon = float(row['longitude'])
               brightness = float(row['brightness'])
          except ValueError:
               print(f"missing data for {date}")
          else:
               lats.append(lat)
               lons.append(lon)
               brights.append(brightness)


title = "World Fires 1 day"
fig = px.scatter_geo(lat=lats, lon=lons, size=brights, title=title, 
                     color=brights, color_continuous_scale='Viridis',
                     labels={'color':'brightness'}, hover_name=dates)

fig.show()