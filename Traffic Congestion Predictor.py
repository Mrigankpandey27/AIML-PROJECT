import pandas as pd
from sklearn.tree import DecisionTreeClassifier

print("Starting my traffic project...")

data = {
    "hour": [8, 9, 17, 18, 22, 6, 14, 16, 20, 7, 12, 19, 10, 15],
    "day": ["weekday", "weekday", "weekday", "weekday", "weekend", "weekday", "weekend", "weekday", "weekend", "weekday", "weekday", "weekday", "weekday", "weekend"],
    "weather": ["clear", "clear", "clear", "rainy", "clear", "foggy", "clear", "rainy", "clear", "foggy", "clear", "rainy", "clear", "clear"],
    "road": ["city", "city", "highway", "city", "highway", "city", "highway", "city", "highway", "city", "city", "highway", "city", "highway"],
    "traffic": ["high", "high", "high", "high", "low", "low", "medium", "high", "medium", "low", "medium", "high", "medium", "medium"]
}

df = pd.DataFrame(data)

df["day"] = df["day"].map({"weekday": 0, "weekend": 1})
df["weather"] = df["weather"].map({"clear": 0, "rainy": 1, "foggy": 2})
df["road"] = df["road"].map({"city": 0, "highway": 1})
df["traffic"] = df["traffic"].map({"low": 0, "medium": 1, "high": 2})

x_train = df[["hour", "day", "weather", "road"]]
y_train = df["traffic"]

my_model = DecisionTreeClassifier()
my_model.fit(x_train, y_train)

print("model is trained now")

while True:
    print("--- Traffic Check ---")
    
    h_val = input("enter hour 0-23: ")
    try:
        h = int(h_val)
    except:
        h = 12
    
    d_val = input("day (weekday/weekend): ")
    if d_val == "weekday":
        d = 0
    else:
        d = 1
        
    w_val = input("weather (clear/rainy/foggy): ")
    if w_val == "clear":
        w = 0
    elif w_val == "rainy":
        w = 1
    else:
        w = 2
        
    r_val = input("road (city/highway): ")
    if r_val == "highway":
        r = 1
    else:
        r = 0

    p = my_model.predict([[h, d, w, r]])
    
    print("result:")
    if p[0] == 0:
        print("traffic is low")
        print("tip: its a good time to go")
    if p[0] == 1:
        print("traffic is medium")
        print("tip: leave early")
    if p[0] == 2:
        print("traffic is high")
        print("tip: wait a bit")
        
    ans = input("again? (y/n): ")
    if ans == "n":
        break

print("program ended")