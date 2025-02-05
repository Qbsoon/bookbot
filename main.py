def count(text):
    i=0
    for j in text.split():
        i+=1
    return i

def diction(text):
    d = dict()
    for ch in text:
        ch = ch.lower()
        if ch in d.keys():
            d.update({ch: d.get(ch)+1})
        else:
            d.update({ch: 1})
    return d

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print(f'--- Begin report of books/frankenstein.txt ---\n{count(file_contents)} words found in the document\n')
    di = diction(file_contents)
    for i,j in di.items():
        if not i.isalpha(): continue
        print(f'The \'{i}\' character was found {j} times')
    print('--- End report ---')
