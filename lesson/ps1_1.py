s='azcbobobegghakl'
count_montecristo=0
elon=''
musk=''
for elon in s:
    for musk in 'aeiou':
        if elon==musk:
            count_montecristo+=1
            break
print("Number of vowels: "+str(count_montecristo))