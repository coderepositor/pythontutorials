"""message = "Learning Python for Data Engineering"
notification = 'Saturdays are working'
print("Title " ,message)
print("Notification of the Week ", notification)
"""
#escape codes
"""
\n = new line feed
\r = carriage return
\t = Tab
\' = literal single
\" = literal double
\\ = Literal backslash
"""
"""
#string Indexing
message = "Learning Python for Data Engineering"
print("The character from the position 6 " , message[5])

#slicing
print("The message from 8th Position", message[9:])
print("The message from 8th Position", message[:9])
print("The message from  9th to 14th Position", message[9:15])
print("The message extracted from end of string 5 characters", message[-5:])
print("The message from  5th position to len-3 position", message[5:-3])
print("The message till len-3 position", message[:-3])
print(message[::-1])

print("length of message ", len(message))


print(message.count("in"))
print(message.upper())
print(message.find("in",29,35))
print(message.split())

"""


name = "IBM"
shares = 100
price = 91.1

trade_msg = f'{name:>10s} {shares:10d} {price:10.2f}'
sharecost = f'Cost = Rs.{shares*price:0.2f}'
print(trade_msg)
print("-" * 60)
print(sharecost)

















