def matchingStrings(strings,queries):
    # cnt1 = []
    # for j in queries:
    #     if j in strings:
    #         cnt = strings.count(j)
    #     else:
    #         cnt = 0
    #     cnt1.append(cnt)
    cnt1 = [strings.count(j) if j in strings else 0 for j in queries]
    return cnt1

strings = []
queries = []

str1 = int(input("Eneter no.of elements: "))
for ele in range(0,str1):
    str2  = input()
    strings.append(str2)

que1 = int(input("Eneter no.of elements: "))
for ele in range(0,que1):
    que2  = input()
    queries.append(que2)

print(matchingStrings(strings,queries))

