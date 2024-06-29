import pandas as pd

data = {0 : ['역명', '서울역', '대전', '동대구', '부산'], 
        1 : ['서울역', 0, 23700, 43500, 59800], 
        2 : ['대전', 23700, 0, 19700, 36200], 
        3 : ['동대구', 43500, 19700, 0, 17100], 
        4 : ['부산', 59800, 36200, 17100, 0]}
df_index = [0, 1, 2, 3, 4]
df = pd.DataFrame(data, index = df_index)

def getPrice(value1, value2):
    return df[value1][value2]

def getLocation(value1, value2):
    return df[value1][0], df[0][value2]

def main():
    startStation = int(input("출발역 코드 : "))
    stopStation = int(input("도착역 코드 : "))
    
    price = getPrice(startStation, stopStation)
    start, stop = getLocation(startStation, stopStation)
    
    print()
    print(f"출발역 : {start}")
    print(f"도착역 : {stop}")
    print(f"요금 : {price}원")

main()