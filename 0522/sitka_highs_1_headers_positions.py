from pathlib import Path
import csv


path = Path('/works/works_python/0522/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)

#enumerate를 사용해서 0 STATION, 1 NAME, 2 DATE 이런 식으로 인덱스와 각 요소를 동시에 붙여서 반환할수잇음 