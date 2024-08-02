lucky_draws = set()
print(type(lucky_draws), lucky_draws)
lucky_draws_o = {14,18,35,37,67,55,40,18,37}
lucky_draws_s = {11,18,35,36,66,55,43}
#lucky_draws_s.add(4)
#lucky_draws_o.discard(37)
print("online draws", lucky_draws_o)
print("shop draws",lucky_draws_s)
"""
print(len(lucky_draws_o))
for draw in lucky_draws_o:
    print(draw)
"""
print("set union", lucky_draws_o | lucky_draws_s)
print("set intersection", lucky_draws_o & lucky_draws_s)
print("set difference online - shopping ", lucky_draws_o - lucky_draws_s)
print("set difference shopping - online ", lucky_draws_s - lucky_draws_o)
print(lucky_draws_o.intersection(lucky_draws_s))
set_1 = {1,3,5}
set_2 = {3,5,1}
print(set_1 == set_2)



