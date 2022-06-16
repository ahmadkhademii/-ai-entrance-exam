from hazm import *
from fa import convert

f = open('input.txt', 'r')

old_text = f.read()



# print(text)
token = sent_tokenize(old_text)




text_without_filter = ''
for i in old_text:
    text_without_filter = text_without_filter + i
# print(text)




text_without_filter = text_without_filter.replace('ة', 'ه')
text_without_filter = text_without_filter.replace('ك', 'ک')
text_without_filter = text_without_filter.replace('ي', 'ی')
text_without_filter = text_without_filter.replace('آ', 'ا')
text_without_filter = text_without_filter.replace('،', ' ')
text_without_filter = text_without_filter.replace('.', ' ')
text_without_filter = text_without_filter.replace('ژ', '')



normalizer = Normalizer()
norm_text_without_filter = normalizer.normalize(text_without_filter)
# print(norm_text_without_filter)



# convert num to word                               در این قسمت عدد در متن را پیدا کرده و حروف عدد را به جای عدد جایگذاری میکند!
for m in norm_text_without_filter.split():
    if m.isdigit():
        norm_text_without_filter = norm_text_without_filter.replace(m, convert(m))


with open('output_without_filter.txt', 'w') as f:
    f.write(norm_text_without_filter)