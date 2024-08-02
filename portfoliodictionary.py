my_stocks = {}
my_stocks= {"TCS":2700, "Infosys": 3000, "IDBI" : 140, "NTPC":221, "TCS":900}
#print(type(my_stocks))
my_stocks["SBI"] = 1700
print("Price of Infosys is-", my_stocks["Infosys"])
print(my_stocks)
print(len(my_stocks))
#my_stocks.clear()
#print(len(my_stocks))
"""print("keys" , my_stocks.keys())
print("values" , my_stocks.values())
"""
"""
for stock in my_stocks:
    print(stock, "has price:",my_stocks[stock])


for stock in my_stocks.items():
    print(stock)
    print(stock[0])
"""
#print(my_stocks.items())
for key,value in my_stocks.items():
    print(key,"->",value);

print(my_stocks.pop("Infosys"))
print(my_stocks.popitem())
my_stocks["IDFC"] = 90
for key,value in my_stocks.items():
    print(key,"->",value);

print("*" * 60)
del my_stocks["TCS"];

for key,value in my_stocks.items():
    print(key,"->",value);
print("*" * 60)
swapped = {}
for key,value in my_stocks.items():
    swapped[value] = key
print(swapped)
















