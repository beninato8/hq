def countL(text, words):
    words = words.split()
    num = 0
    for word in words:
        num += text.count(word)
    return num

big_text = 'aaa bb aa b c ddd aa bbb aaa ddd ccc ee dd bbb aaa dd aaa bb aaa'
print(countL(big_text.lower().split(), 'aaa'.lower()))
