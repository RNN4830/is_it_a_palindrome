
word = input("Select a word to see if it is the same spelled backwards:").lower()
original =[eachletter for eachletter in word if eachletter.isalpha() and eachletter.strip()]
print ("It's a palindrome!") if original == original[::-1] else print("No palindrome here folks!")

#The long way
# for eachletter in word:
#     if eachletter.isalpha() and eachletter.strip():
#         count+=1
#         original.append(eachletter)
# print(original)
# if original == original[::-1]:
#     print("It's a palindrome!")
# else:
#     print("No palindrome here ya'll!")
