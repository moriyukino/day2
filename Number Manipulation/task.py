bmi = 84 / 1.65 ** 2

print(bmi)

print(int(bmi))

#roud関数
print(round(bmi))
#round関数で小数点第2位までを表示
print(round(bmi,2))

####################
#f-string

score = 0
height = 1.8
is_winning = True

print(f"Your score is = {score},Your height is {height},You are winning is {is_winning}")