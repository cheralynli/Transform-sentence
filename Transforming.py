def transform(original_sentence):
    word=[]
    words=[]
    spaces=[]
    newsentence=[]
    wordcount=0
    lettercount=0
    # Creating a list of words with alternating case letters
    for i in range(len(original_sentence)):
        char= original_sentence[i]
        char_before= original_sentence[i-1] if i > 0 else ""

        if i>0 and char != " " and char_before != " ":
            word[wordcount-1]= word[wordcount-1]+ char.lower() if lettercount%2 else word[wordcount-1]+ char.upper()
            lettercount+=1

        elif char.isalpha():
            word.append(char) if lettercount%2 else word.append(char.upper())
            wordcount += 1
            lettercount+=1

        elif i>0 and char == " " and char_before == " ":
            word[wordcount-1]= word[wordcount-1] +char

        elif char == " ":
            word.append(char)
            wordcount += 1
    # Reversing the words while keeping spaces in their original positions
    for w in word:
        if w.isalpha():
            words.append(w)
        else:
            spaces.append(w)
    words=words[::-1]
    # Merge the words and spaces back into one list
    for i in range(len(word)):
        newsentence.append(words[i] if i < len(words) else "")
        newsentence.append(spaces[i] if i < len(spaces) else "")
    # Form the sentence into a string
    word= ''.join(newsentence)
    return word

original_sentence = input()
print(transform(original_sentence))