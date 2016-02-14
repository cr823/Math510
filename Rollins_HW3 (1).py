
# coding: utf-8

# In[654]:

#Question 1: Define a procedure histogram() that takes a list of integers and prints a histogram to the screen.

#Using function generate_n_chars from hw2...
def generate_n_char(n,char): 
    '''Generates an integer n and a character, then returns a string of n characters long.'''
    x=''
    for i in range(n): #for the number in n
        x=x+char #x will be returned n number of times
    return x

def histogram(list):
    '''Creates list (parameter) of integers, and based on each value, prints them out in histogram form'''
     
    for x in list: #for each value in the list
        char= generate_n_char(x,'*') #number of characters in each x value from the list is created
        #for example if x=2 was in the list, then two characters would be created. 
        #for every value x on the list, x will be returned n number of times. x will then be replaced by *
        print(char)
    '''for each value in the list a "*" will print out for the value of each item in the list'''    
# histogram([1,4,5])


# In[655]:

#Question 2: The function max() from exercise 1) and the function max_of_three() from exercise 2) will only work
#for two and three numbers, respectively. But suppose we have a much larger number of numbers, or suppose we cannot 
#tell in advance how many they are? Write a function max_in_list() that takes a list of numbers and returns the 
#largest one.

def max_in_list(list):
    '''Function will find the highest value in the list. List of values is the parameter'''
    max = 0 #start value at zero
    for i in list: #for each number in the list
        if i > max: #start iteration of each value in list for loop. 
            max = i #the loop will keep going for each value until it finds the largest i
    return max

# max_in_list([1,200,43,5454,300000,1,90])


# In[656]:

#Question 3: Write a program that maps a list of words into a list of integers representing the lengths of the 
#corresponding words.

def map_list(list):
    '''Function will return the length (i.e. number of letters) for each word in the parameter (list)'''
    ans=[]
    for i in list: #for each word in the list
        count=0 #starting at zero
        for char in i: #this will account for all letters of each word
            count+=1 #this will count the numbers in each word
        ans.append(count) #this will add the count to the answer
    return ans

# map_list(["apple", "carmen", "tired"])


# In[657]:

#Question 4: Write a function find_longest_word() that takes a list of words and returns the length of the longest one.

def find_longest_word(list):
    '''Function will find the longest word on a list and return the number of characters in the word
    Parameter (list) is a list of words.
    Using two functions from HW3 to find 1) map_list to find the length of each word in the list 
    and 2) return the highest value in the list to find the longest word
    '''
    long= max_in_list(map_list(list)) #as explained in docstring
    for i in list: #for each value in the list
        y=max_in_list(map_list(i)) #define y, which finds the longest word out of all the values on the list
        if y > long: long= y #once y is larger than long we know we've found the longest word and make long equal to y
    return long

# find_longest_word(["apple", "happiness", "tired", "mathematics"])


# In[658]:

#Question 5: Write a function filter_long_words() that takes a list of words and an integer n and returns the list of
#words that are longer than n.

def mylen(n):
    """This function will compute the length of a given list or string n"""
    count = 0 #set count to zero
    for i in n: #for each letter/string (i) in n
        count=count+1   #this will count how many strings (i) are in n
    return (count)
    
def filter_long_words(string,number):
    """This function will take a list of words and an integer n, and return the list of words longer than n
    it will use the function mylen(n) from HW2 to count the length of each word
    """
    ans = [] #blank set for answer
    for i in range(mylen(string)): #for each word in the string mylen function counts the number of letters 
        if mylen(string[i]) > number: #if a word in the string is larger than the number n 
            ans.append(string[i]) #it will return these words to the blank set so it can print the answer
    return ans
# filter_long_words(["apple", "happiness", "tired", "mathematics"],8)


# In[659]:

#Question 6: Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go hang a 
#salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate
#no basil", "Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and 
#spacing are usually ignored.

## This doesn't quite work correctly. Should ignore case and punctuation
def is_palindrome_phrase(list):
    """This function will recgonize palindrome phrases 
    Parameter: 'list' is the paramter, which can be any statement (of words) entered below as "list="
    """
    if list==list[::-1]: #this is checking if the list reversed is equal to the list
        return True #if it is equal to list, it will return true
    else:
        return False #if not, it will return false

##list=["was it a rat i saw?"] #enter phrase here
# is_palindrome_phrase(list)


# In[660]:

#Question 7: A pangram is a sentence that contains all the letters of the English alphabet at least once, for example:
#The quick brown fox jumps over the lazy dog. Your task here is to write a function to check a sentence to see if it
#is a pangram or not.

def pangram(sentence):
    """This function will check if the parameter (all) is a panagram sentence and return either true
    or false to let us know if it is a panagram or not.
    The paramater (all) is a list of words"""
    alpha = "abcdefghijklmnopqrstuvwxyz" #alphabet is defined here
    for i in alpha: #for each letter in the alphabet
        if i not in sentence: #if a letter of the alphabet is not in the sentence (parameter)
            return False #the function will return false

    else: return True #if all letters of the alphabet are in the sentence, the function will return true
            
# pangram("The quick brown fox jumps over the lazy dog")


# In[661]:

#Question 8: "99 Bottles of Coke" is a traditional song in the United States and Canada. It is popular to sing on 
#long trips, as it has a very repetitive format which is easy to memorize, and can take a long time to sing. 
#The song's simple lyrics are as follows:
#99 bottles of coke on the wall, 99 bottles of coke.
#Take one down, pass it around, 98 bottles of coke on the wall.
#The same verse is repeated, each time with one fewer bottle. The song is completed when the singer or singers reach
#zero. Your task here is write a Python program capable of generating all the verses of the song.

## Goes one too far and you end up with -1 bottles!
def ninety_nine_bottles():
    """This function will generate all the versus to the song '99 bottles of coke'
    the parameter is blank (i.e. no parameter) as once this function is entered it 
    will automatically generate the entire song"""
    count=9 #start at 99 (the song starts at 99 bottles)
    while count >= 0: #loop will run until count is greater or equal to zero (i.e. it will run from 99-0)
        #this loop will print the blow, which for each iteration has the current count (and count-1 for the
        #second line) 
        print (str(count) + " bottles of coke on the wall, " + str(count) + " bottles of coke.")
        print ("Take one down, pass it around, " + str(count-1) + " bottles of coke on the wall")
        count-=1
        
# ninety_nine_bottles()


# In[662]:

#Question 9: Represent a small bilingual lexicon as a Python dictionary in the following fashion {"merry":"god", 
#"christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"år"} and use it to translate your Christmas cards
#from English into Swedish. That is, write a function translate() that takes a list of English words and returns a 
#list of Swedish words.

## Error in trying to iterate over the dictionary
def translate(words):
    """This function will translate a list of English words to 'Swedish.
    Parameter (words) is a list of English words that will be translated 
    into Swedish based on the below dictionary'"""
    #dictionary for translation
    dic={"merry":"god", "christmas":"jul", "and":"och", "happy":"gott","new":"nytt", "year":"år"} 
    swedish=[] #leave empty
    for i in words: #for each word in the 'words' (the parameter or list of words)
        ## This didn't work for me - Prof G
        #if i in dict: #if there is a word from the dictionary in words parameter
        swedish.append(dic[i]) #then it will be replaced with the dictionary word
    return swedish
    
# translate(["merry", "christmas", "and" ,"happy", "new", "year"])


# In[667]:

#Question 10: Write a function char_freq() that takes a string and builds a frequency listing of the characters 
#contained in it. Represent the frequency listing as a Python dictionary. Try it with something like 
#char_freq("abbabcbdbabdbdbabababcbcbab").

def char_freq(n):
    """Function will count the frequency of each characters in a given string for parameter n.
    Parameter n can be any characters (such as "abcdefg" etc.)"""
    char = {} #leave blank
    
    for i in n: #for each character (i.e. letter) in the parameter n
        keys=char.keys() #this will link each characters in 'char' with 
        
        #for each letter found in keys, when the same character appears the count will increase by 1
        #this means for each character it will keep adding 1 if it is the same character
        if i in keys:
            char[i]+=1
        else:
            char[i]=1 #if there is not more than one charater
    return (char)

# char_freq("aabbababababababa")

# In[668]:

#Question 11: n cryptography, a Caesar cipher is a very simple encryption techniques in which each letter in the plain 
#text is replaced by a letter some fixed number of positions down the alphabet. For example, with a shift of 3, A 
#would be replaced by D, B would become E, and so on. The method is named after Julius Caesar, who used it to 
#communicate with his generals. ROT-13 ("rotate by 13 places") is a widely used example of a Caesar cipher where the 
#shift is 13. In Python, the key for ROT-13 may be represented by means of the following dictionary:
#key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 
#'m':'z', 'n':'a', 'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 
#'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 
#'M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 
#'Z':'M'}
#Your task in this exercise is to implement an encoder/decoder of ROT-13. Once you're done, you will be able to read 
#the following secret message: Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!
#Note that since English has 26 characters, your ROT-13 program will be able to both encode and decode texts written 
#in English.

def ROT13(code):
    """This function will decode ROT-13, named after Julius Caesar, who used it to communicate with his generals.
    Parameter (code): each letter in the plain text is replaced by a letter some fixed number of positions down 
    the alphabet. For example, with a shift of 3, A would be replaced by D, B would become E, and so on."""
    result=""
    key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 
        'm':'z', 'n':'a', 'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 
        'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W',
        'K':'X', 'L':'Y','M':'Z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
        'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
    for i in code: 
        if i in key: 
            result+= key[i] 
    #for each letter in the parameter (code), if the letter is found in the key (i.e. any letter of the alphabet)
    #the letter in code will be replaced with the key (i.e. a would be replaced by n, and so on)
        else: result+=i #if there is something not in key (such as a space or ?) the result will remain the same
    return result
 
# ROT13("Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!")


# In[670]:

#Question 12: Define a simple "spelling correction" function correct() that takes a string and sees to it that
#1) two or more occurrences of the space character is compressed into one, and 
#2) inserts an extra space after a period if the period is directly followed by a letter. 
#E.g. correct("This is very funny and cool.Indeed!") should return "This is very funny and cool. Indeed!"

## Failed to import re in this file, so this initially failed - Prof G
## Added the following line - Prof G
import re
def correct(phrase):
    """This function will takes a phrase from a string to correct simple spelling errors.
     Function will compress multiple space characters into one, and inserts an extra space
     after a period if the period is directly followed by a letter. """
    correct='' #blank set for the 
    
    #this next command will remove extra spaces in the phrase (parameter). 
    #re.sub for '\+' matches a space (or more) with just one space: (' ')
    correct = re.sub('\ +',' ',phrase) 
    
    #this next command will remove an extra space after a period in the phrase (parameter)
    #re.sub for '\.' looks for anywhere there is no space after a period and will add a space: ('. ')
    correct = re.sub('\.','. ',correct)

    ## SHould return the phrase instead of printing it. - Prof G
    return correct

    ##print(correct)
    
# correct("This is very funny and    cool.Indeed!")


# In[671]:

#Question 13: The third person singular verb form in English is distinguished by the suffix -s, which is added to the 
#stem of the infinitive form: run -> runs. A simple set of rules can be given as follows:
#• If the verb ends in y, remove it and add ies
#• If the verb ends in o,ch,s,sh,x or z,add es
#• By default just add s
#Your task in this exercise is to define a function make_3sg_form() which given a verb in infinitive form returns its
#third person singular form. Test your function with words like try, brush, run and fix. Note however that the rules 
#must be regarded as heuristic, in the sense that you must not expect them to work for all cases. 
#Tip: Check out the string method endswith().

## Doesn't work in all cases, see my test cases - Prof G
def make_3sg_form(word):
    """This function will returns a third person singular form verb from the parameter.
    The parameter must be a verb in the infinitive form, i.e. eat, sleep, run, etc."""
    if word.endswith('y'): #checks the last letter of the word for the letter 'y'
        word = word[:-1] + "ies" #will take off the last letter of the word and add 'ies'
    elif word.endswith( ('o' or 'ch'or 's'or'sh' or 'x'or 'z')): 
        #checks the last letter of the word for letters o,ch,s,sh,x or z
        word += 'es' #ads 'es' to the word
    else: #all other words will just have the letter 's' added on to the end of it.
        word += 's'
    ## Should return word instead of printing it - Prof G
    return word
    ##print (word)
    
# make_3sg_form('eat')
# make_3sg_form('sleep')
# make_3sg_form('beauty')
# make_3sg_form('labor')


# In[672]:

#Question 14: In English, the present participle is formed by adding the suffix -ing to the infinite form: go -> going.
#A simple set of heuristic rules can be given as follows:
#• If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
#• If the verb ends in ie, change ie to y and add ing
#• For words consisting of consonant-vowel-consonant, double the final letter before adding ing
#• By default just add ing
#Your task in this exercise is to define a function make_ing_form() which given a verb in infinitive form returns its
#present participle form. Test your function with words such as lie, see, move and hug. However, you must not expect 
#such simple rules to work for all cases.

## Doesn't work in all cases, see my test cases - Prof G
def make_ing_form(word):
    """This function will return a verb (word) into present participle form. 
    The parameter is 'word', the verb there will be changed. """
    vowels= ['a','e','i','o','u'] #here are the vowels 
    
    #if the word ends with 'ie', 
    #delete the last two letters of the word and add "ying"
    if word.endswith('ie'): 
        return word[:-2] + 'ying' 
    
    #if the word ends with 'e'd but not 'ie', 'ee', or not equal to the word 'be', 
    #delete the last letter and add 'ing'
    elif word.endswith('e') and not word.endswith('ie') and not word.endswith('ee') and not word=='be':
        return word[:-1]+'ing'
    
    #if the word (deleting the last 2-3 letters) is not in vowels 
    #and the word (delete the last one to two letters)
    #and the world (delete the last letter of word) is not in word,
    #then delete the last letter and add 'ing'
    elif word[-3:-2] not in vowels and word[-2:-1] in vowels and word[-1:] not in word:
        return word[-1:] + "ing"
    
    else: #if none of the above conditions apply, just add 'ing' to the word
        word += "ing"

    ## Should return word instead of printing it - Prof G
    return word
    ##print (word)


# make_ing_form('be')
# make_ing_form('knee')
# make_ing_form('fly')

##Test Cases
help(histogram)
help(make_ing_form)

print("1 Histogram ", histogram([1,2,3,5,6,7,6,5,4,3,2,1]), '\n')

print("2 Max in List 77 ", max_in_list([1,2,3,77,4,5,6,7]), '\n')

print("3 word to length map 3,5,7,4 ", map_list(['dog', 'snake', 'dolphin', 'cats']), '\n')

print("4 Longest word 7 ", find_longest_word(['dog', 'snake', 'dolphin', 'cats']), '\n')

print("5 filter long words snake, dolphin ", filter_long_words(['dog', 'snake', 'dolphin', 'cats'],4), '\n')

print("6 Palindrome phrase TRUE ", is_palindrome_phrase("Go hang a salami I'm a lasagna hog."), '\n')

print("7 Pangram TRUE ", pangram("The quick brown fox jumps over the lazy dog."), '\n')

print("8 Cokes \n", ninety_nine_bottles())

print("9 Translating to Swedish ['god', 'jul', 'gott'] ", translate(['merry', 'christmas', 'happy']), '\n')

print("10 Char Freq {'a': 7, 'c': 3, 'b': 14, 'e': 2, 'd': 3, 'g': 7, 'f': 3} ", char_freq("agbbabgcbdbabdgbdbabageebabcbgcbffgfabg"), '\n')

print("11 Decoder Caesar cipher? I much prefer Caesar salad!", ROT13("Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"), '\n')

print("12 correct This is very funny and cool. Indeed!", correct("This is very funny and cool.Indeed!"), '\n')

print("13 3ps brushes ", make_3sg_form("brush"), '\n')
print("13 3ps tries ", make_3sg_form("try"), '\n')
print("13 3ps runs ", make_3sg_form("run"), '\n')
print("13 3ps fixes ", make_3sg_form("fix"), '\n')

print("14 ing lying ", make_ing_form("lie"), '\n')
print("14 ing seeing ", make_ing_form("see"), '\n')
print("14 ing moving ", make_ing_form("move"), '\n')
print("14 ing hugging ", make_ing_form("hug"), '\n')

