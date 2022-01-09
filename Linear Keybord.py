n = int(input())

for i in range(n):
    alpha=list(input())
    word=list(input())
    sum=0
    for j in range(len(word)-1):
        sum += abs(alpha.index(word[j+1]) - alpha.index(word[j]))
    print(sum)
