from pathlib import Path
import json
import plotly.express as px

path = Path("/works/works_python/0523/weed_cultivation.json")
contents = path.read_text()
weed_cultivation=json.loads(contents)


# #데이터 집합에서 지진데이터 읽어내기.
# #규모리스트 []
mags, lons, lats, weed_titles = [], [], [], []
for weed_dict in weed_cultivation:
     mag = weed_dict['plants_count']
     lon = weed_dict['coordinates'] [0] #경도출력
     lat = weed_dict['coordinates'] [1] #위도출력
     weed_title=weed_dict['strain']
     mags.append(mag)
     lons.append(lon)
     lats.append(lat)
     weed_titles.append(weed_title)

title = 'The Weed Cultivation in US'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
                     color=mags, color_continuous_scale='Viridis',
                     labels={'color':'plants_count'},
                     projection='natural earth',
                     hover_name=weed_titles
                     )
fig.show()