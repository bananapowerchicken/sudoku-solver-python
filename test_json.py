import requests

url = 'https://sudoku.com/api/level/evil'
res = requests.get(url).json()

print(res)