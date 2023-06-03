nums = [1,2,3,4,5,6,7,8,9,10]

print("range(5): ")
for i in range(5):
    print(i)

print("range(0,5): ")
for j in range(0,5):
    print(j)

print((list(range(5))))
print(list(range(0,5)))

print(range(5))


####################################################


addition_str = "2+5+10+20"
txt = addition_str.split("+")
res = [int(i) for i in txt]
print(type(res))
sum_val = 0

for i in res:
    sum_val = sum_val + i



print(sum_val)

#############################################


original_str = "The quick brown rhino jumped over the extremely lazy fox"
num_words_list = 0

for i in original_str:
    num_words_list += 1
print(num_words_list)


def convert(string):
    li = list(string.split(" "))
    return li

print(convert(original_str))

res = []

for e in convert(original_str):
    count = 0
    if type(e) == int:
        res.append(1)
    else:
        for sub in e:
            count = count + 1
        res.append(count)

print(str(res))


########################################################

str1 = "Today you are you! That is truer False than true! " \
       "There is no one alive who is you-er than you"

if "False" in str1:
       output = "False, you arent you"
       print(output)

elif "True" in str1:
       output = "True! you are you!"
       print(output)

else:
       output = "Neither true nor false"
       print(output)


###############################################################

words = ["water", "chair", "pen", "basket", "hi", "car"]
num_words = 0
for each in words:
    if len(each) > 3:
        num_words += 1

print(num_words)


