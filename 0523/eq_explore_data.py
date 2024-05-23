from pathlib import Path
import json
import plotly.express as px

#데이터 경로 알려주고
path = Path("/works/works_python/0523/eq_data.geojson")
#1. 문자열(read_text)로 읽어내고 
contents = path.read_text()
#2. json.loads - json 형식의 문자열을 파이썬이 이해할수있는 딕셔너리 구조로 로드한다.
hawaii_eq_data=json.loads(contents)

#데이터파일의 Path를 설정해주고 위 제이슨파일을 덤프해줘가지고 읽기 쉬운 리데이블 컨텐츠를 하나 만든다.
#path.write_text를 통해서 
path = Path("/works/works_python/0523/readable_eq_data.geojson")
#딕셔너리를 다시 제이슨으로. 
readable_contents=json.dumps(hawaii_eq_data, indent=4) #indent로 중첩된 요소 들여쓰기-가독성 예쁘게 위해서
path.write_text(readable_contents)
##readable_contents는 보통 사람이 읽기 쉬운 형태로 딕셔너리를 표현하기 위해 사용함!
#코딩에서 사용하기 위해서가 아님..호출할때는 readable_contents를 사용할 필요가 없습니다. 
#그냥 딕셔너리로 바꿔놓은 hawaii_eq_data를 써야지


#데이터 집합에서 지진데이터 읽어내기.
hawaii_eq_dicts=hawaii_eq_data['features']
#규모리스트 []
mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in hawaii_eq_dicts:
     mag = eq_dict['properties']['mag'] #properties 안에 mag에 저장되어있음. 
     lon = eq_dict['geometry']['coordinates'] [0] #경도출력
     lat = eq_dict['geometry']['coordinates'] [1] #위도출력
     eq_title=eq_dict['properties']['title']
     mags.append(mag)
     lons.append(lon)
     lats.append(lat)
     eq_titles.append(eq_title)

title = 'Hawaii Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
                     color=mags, color_continuous_scale='Viridis',
                     labels={'color':'Magnitude'},
                     projection='natural earth',
                     hover_name=eq_titles
                     )
fig.show()