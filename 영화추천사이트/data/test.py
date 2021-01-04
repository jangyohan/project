import json
f = open("data.txt", 'r', encoding='utf-8')
# print(list(f)[0])

# print(list(f)[0])
dummy = list(f)[0]

dummy = eval(dummy)


#https://djangoworld.tistory.com/8pip3 install ast

# final_data = dummy[0]
# print(len(final_data))
# print(len(dummy))
# print(dummy[1])



# with open('final.json', 'w', -1, "utf-8") as f:
#   json.dump(dummy, f, ensure_ascii=False)