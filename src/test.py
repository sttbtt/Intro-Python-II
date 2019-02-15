wordFreqDic = {
    "Hello": 56,
    "at" : 23 ,
    "test" : 43,
    "this" : 78
    }
word = 'test'

if word in wordFreqDic:
    print(f"Yes {word} key exists in dict")
else:
    print(f"No {word} key does not exist in dict")


print(list(wordFreqDic))
