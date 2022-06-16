from hazm import *
from fa import convert

f = open('input.txt', 'r')

old_text = f.read()



# print(text)
token = sent_tokenize(old_text)



new_token = []
for i in token:
    if len(word_tokenize(i)) <= 50 and len(word_tokenize(i)) >= 10:
        new_token.append(i)
    
text = ''
for i in new_token:
    text = text + i
# print(text)


text = text.replace('ة', 'ه')
text = text.replace('ك', 'ک')
text = text.replace('ي', 'ی')
text = text.replace('آ', 'ا')
text = text.replace('،', ' ')
text = text.replace('.', ' ')
text = text.replace('ژ', '')
# print(text)


normalizer = Normalizer()
norm_text = normalizer.normalize(text)
# print(norm_text)

with open('output_with_filter.txt', 'w') as f :
    f.write(norm_text)
