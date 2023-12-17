user = input("Input set:")
user = eval(user)
user_power = [[]]

for i in range(len(user)):
    for j in range(len(user_power)):
        user_power.append([*user_power[j], user[i]])

print(user_power)