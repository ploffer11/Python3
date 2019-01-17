stocks = {
    "GOOG" : (1,2,3),
    "MSFT" : (4,5,6),
}

stocks["GOOG"]
#stocks["RIM"]
stocks.get("RIM", "NOTFOUND")

stocks.setdefault("GOOG",(7,8,9))
stocks.setdefault("RIM", (10,11,12))

for key, value in stocks.items():
    print(f"key : {key}, value : {value}")
