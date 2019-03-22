import random
def anagram():
  letters = []
  anagramList=[]
  anagramObj = input("Enter anagram here:")
  anagramObj=anagramObj.lower()
  shuffleTimes=int(input("How many times to reshuffle?"))
  letters=list(anagramObj)
  while shuffleTimes > 0:
    random.shuffle(letters)
    shuffledWord=''.join(letters)
    shuffledWord=shuffledWord.title()
    anagramList.append(shuffledWord)
    shuffleTimes -=1
  anagramList=set(anagramList)
  anagramList=list(anagramList)
  for i in range(len(anagramList)):
    print(str(i+1) +'. '+anagramList[i])
  print('NOTE: If the number of results is less than the amount of reshuffles requested, it is because duplicate results have been removed.')
anagram()