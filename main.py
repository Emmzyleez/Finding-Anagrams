# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


print("Enter two words and I will output 'True' if they are anagrams and 'False' if they are not")
def find_anagram(word, anagram):

    word1 = word.lower()
    word2 = anagram.lower()
    
    sorted_word1 = sorted(word1)
    sorted_word2 = sorted(word2)


    if (len(sorted_word1) == len(sorted_word2)):

        if (sorted_word1 == sorted_word2):
            return True
        else:
            return False
    else:
        return False
    
active = True
while active:
    word = input("\nEnter a word: ")
    anagram = input("Enter a possible anagram of this word: ")


    if find_anagram (word, anagram):
        print("True")
    else:
        print("False")

    prompt = input("\nDo you want to play again? Enter 'Y' if Yes and 'N' if No: ")

    if prompt == "Y":
        active = True
    else:
        break


    

    


