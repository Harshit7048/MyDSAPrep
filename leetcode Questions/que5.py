print("Question number 14")

liststrs = ['flower',"flow","fler"]

# def checkLCP(n):
#     print(n)
#     first_word = n[0]
#     print(first_word)
#     n = len(liststrs)
#     n2 = len(first_word)
#     checkWord = list(first_word)
#     for i in range(0,n2):
#         print(checkWord[i])
#         checkThis = checkWord[i]
#         for j in range(1,n):
#             newWord = list(liststrs[j])
#             if checkWord == newWord[j]:
#                 print(True)
        

         
            

# checkLCP(liststrs)

def checkLCP(strs):
    result=''
    if len(strs)==0:
        return
    
    base = strs[0]
    for i in range(0,len(base)):
        for word in strs[1:]:
            if i == len(word) or word[i] != base[i]:
                return result
        result += base[i]
    
print(checkLCP(liststrs))