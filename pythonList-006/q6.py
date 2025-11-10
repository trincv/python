import string

frequency = {}
mostFrequent = {}

completeText = input("Escreva um texto ou frase:\n").lower()
caractersToRemove = string.punctuation + string.digits
translateTable = str.maketrans("", "", caractersToRemove)
translatedText = completeText.translate(translateTable)

listOfWords = translatedText.split()

for word in listOfWords:

    if (word in frequency):
        frequency[word] += 1
    else:
        frequency[word] = 1

sortedFrequecy = sorted(frequency.items(), key=lambda item: item[1], reverse=True)

mostFrequent = sortedFrequecy[:5]

print(f"\nQuantidade total de palavras diferentes: {len(frequency)}")
print(f"As palavras mais frequentes são:\n {mostFrequent}")
    