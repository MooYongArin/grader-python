file_name = input().strip()
k = int(input())
ruler = ''

for i in range(k//10) : #print text position reference
    ruler += '-'*9 + str(i+1)
if k%10 != 0:
    ruler += '-'*(k%10)
print(ruler)

file = open(file_name) # open file
Text = file.read()
Text = Text.replace('\n','.')
word = []
temp = ''
count = 0
dot_check = False
for ch in Text: # make list of words and dots
    if ch != '.':
        if dot_check:
            word.append(temp)
            dot_check = False
            temp = ch
        else:
            temp += ch
    elif ch == '.':
        if not dot_check:
            word.append(temp)
            dot_check = True
            temp = '.'
        else:
            temp += '.'
word.append(temp)
# print(word)

result = []
for ch in word: # transform into list of tuple (len,word)
    result.append( (ch,len(ch)) )

sentence = ''
Total_len = 0
for n,length in result:
    if Total_len + length <= k: #if line not exceed k value
        sentence += n
        Total_len += length
    else: # exceed k value
        if len(sentence) != 0:
            print(sentence.strip('.'))
        sentence = n
        sentence = sentence.strip('.')
        Total_len = len(sentence)

if len(sentence) > 0: # print last line
    print(sentence.strip('.'))
file.close() # close file