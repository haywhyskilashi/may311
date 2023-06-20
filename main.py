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

####################################################################


words = ["adopt", "bake", "beam", "confide", "grill", "plant", "time", "wave", "wish"]

past_tense = []
for each in words:
    lastchar = each[-1]
    if lastchar == "e":
        each = each + 'd'
        print(past_tense.append(each))
    else:
        each = each + 'ed'
        print(past_tense.append(each))


#########################################################################


rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
txt = rainfall_mi.split(",")

num_rainy_months = 0

intlist = list(map(lambda i: float(i), txt))
print(intlist)

for j in intlist:
    if j > 3.0:
        num_rainy_months += 1
print(num_rainy_months)


###################################################################


sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
same_letter_count = 0
txt = sentence.split(" ")
for i in txt:
    if i[0] == i[-1] :
        same_letter_count += 1
print(same_letter_count)


###################################################################


items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama","tumultuous","owing"]
acc_num = 0

for i in items:
    if "w" in i:
        acc_num += 1
print(acc_num)


################################################################


sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
txt = sentence.split(" ")
num_a_or_e = 0


for i in txt:
    if "e" in i:
        num_a_or_e += 1
    elif "a" in i:
        num_a_or_e += 1

print(num_a_or_e)


############################################################################

num_lst = [3, 20, -1, 9, 10]
is_odd = []

for i in num_lst:
    if i % 2 != 0:
        print(i)
        is_odd += [True]
    else:
        # print(i)
        is_odd += [False]

print(is_odd)


#######################################################3

str1 = "I love python"
char = []

for i in str1:
    char.append(i)
print(char)

#########################################

output = ""
for i in range(35):
    output = i * "a"
print(output)
#     output = output + str(i)
# print(output)

#####################################################




colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
initials = []

for color in colors:

    initials.append(color[0])

print(initials)


###########################################################


colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "Purple", "Pink", "Brown", "Teal", "Turquois",
          "Peach", "Beige"]

for position in range(len(colors)):
    color = colors[position]
    print(color)
    if color[0] in ["P", "B", "T"]:
        del colors[position]

print(colors)

#####################################################################



scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
x = scores.split(' ')
a_scores = 0
listofscores = [int(i) for i in x]
for score in listofscores:
    if score >= 90:
        a_scores += 1

print(score)


###############################################################

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so',
             'it', 'and', "The"]

org = "The organization for health, safety, and education"

acro = ""
f1 = org.split(" ")


print(f1)
for i in f1:
    if i not in stopwords:
        acro = acro + i[0].upper()

print(acro)


######################################################################



stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
acro = ""


'. '.join(word[:2].upper() for word in sent.split() if word not in stopwords)
for i in acro:
    if i not in stopwords:
        acro += i[0:2].upper()
        if i != i[:1]:
            acro = acro + "."
print(acro)


################################################################3



stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"

acro = ""
sent_words = sent.split()
# ['The', 'water', 'earth', 'and', 'air', 'are', 'vital']


for word in sent_words:

    if word not in stopwords:
        acro = acro + word[0:2]
        if word != sent_words[-1]:
            acro += ". "
            print(acro)
# #
acro = acro.upper()
print(acro)


#####################################################################3


inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]

for temp in inventory:
    temp = temp.split(',')
    item = temp[0]
    quantity = temp[1]
    amount = temp[2]
    str1 = "The store has {} {}, each for {} USD."
    str1 = str1.format(quantity, item, amount)
    print(str1)








