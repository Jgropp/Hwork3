from nltk.book import *
from nltk import bigrams
#print(text1)

print(text2)
print("\n\n")

print("Length of ",text1,"is",len(text1))

print("Length of ",text2,"is",len(text2))

print("Unique tokens in",text1," are: ",len(set(text1)))

print("Unique tokens in",text2,"are: ",len(set(text2)))
print("\n\nList of unique words")
print(sorted(set(text2))[:15])
print(sorted(set(text2),reverse=True)[:15])
print("\n\nFrequency Distribution")
#Frequency Distribution
fdist1 = FreqDist(text1)

print(fdist1)

print(fdist1.most_common(25))

print("\n\nWords with more characters")

#How about "long" words
long_words = [w for w in text1 if len(w)>15]

print(long_words)

print("\n\nBigrams")

print(list(bigrams(text4))[:20]) #text8 would get me in trouble

print("\n\nCollocations")

print(text4.collocations())