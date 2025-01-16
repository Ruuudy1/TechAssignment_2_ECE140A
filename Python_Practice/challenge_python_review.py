##
## I AM A CS MAJOR WHO HAS BEEN LEETCODING FOR 5 MONTHS STRAIGHT FOR INTERNSHIPS
## I WILL NOT BE SOLVING THESE THE MOST EFFICIENT WAY
## INSTEAD I WILL SOLVE THESE THE FAST 'INTERVIEW' WAY 
## NO LIST COMPREHENSION && NO LAMBDA FUNCTION
##

from collections import Counter

# Problem 1: Count Unique Characters
def count_unique_characters(s: str) -> int:
    """
    Returns the number of unique characters in the input string.
    """
    return len(set(s))


# Problem 2: Reverse Words
def reverse_words(sentence: str) -> str:
    """
    Reverses the order of words in the input sentence.
    """
    w = sentence.split()
    res = []
    for word in reversed(w):
        res.append(word)
    return ' '.join(res) 


# Problem 3: Flatten a Nested List
def flatten_list(nested_list: list[list[int]]) -> list[int]:
    """
    Flattens a nested list of integers into a single list.
    """
    res = []
    for lst in nested_list:
        for i in lst:
            res.append(i) 
    return res


# Problem 4: Filter Even Numbers
def filter_evens(numbers: list[int]) -> list[int]:
    """
    Filters and returns only the even numbers from the input list.
    """
    res = []
    for num in numbers:
        if num % 2 == 0:
            res.append(num)
    return res


# Problem 5: Find Longest Word
def longest_word(words: list[str]) -> str:
    """
    Finds and returns the longest word in the input list of words.
    """
    res = ""
    for curr in words:
        if len(curr) > len(res):
            res = curr
    return res
        


# Problem 6: Remove Vowels
def remove_vowels(s: str) -> str:
    """
    Removes all vowels from the input string and returns the res.
    """
    arr_vowels = "AaEeIiOoUu"
    res = ""
    
    for i in s:
        if i not in arr_vowels:
            res += i
    return res


# Problem 7: Count Word Frequencies
def count_word_frequencies(sentence: str) -> dict[str, int]:
    """
    Counts the frequency of each word in the input sentence and returns a dictionary.
    """    
    res = {}  
    w = sentence.split() 

    for word in w:
        if word in res:
            res[word] += 1
        else:
            res[word] = 1
    return res



# Problem 8: Palindrome Checker
def is_palindrome(s: str) -> bool:
    """
    Checks if the input string is a palindrome (ignoring case).
    """
    
    res = ""

    for c in s:
        if c.isalnum(): #alphanumerical
            res += c.lower()
    reversed_res = res[::-1]

    return res == reversed_res 


# Problem 9: Merge Dictionaries
def merge_dicts(dict1: dict[str, int], dict2: dict[str, int]) -> dict[str, int]:
    """
    Merges two dictionaries by summing values of common keys.
    """
    res = dict1.copy() 


    for key, val in dict2.items():
        if key in res:  
            res[key] += val
        else:
            res[key] = val
    return res


# Problem 10: Common Elements
def common_elements(list1: list[int], list2: list[int]) -> list[int]:
    """
    Finds and returns elements common to both input lists.
    """
    res = []


    for elem in list1:  
        if elem in list2:  
            res.append(elem) 
    return res

# Problem 11: Replace Substring
def replace_substring(s: str, old: str, new: str) -> str:
    """
    Replaces all occurrences of `old` with `new` in the input string.
    """
    res = ""  
    i = 0
    while i < len(s): 
        if s[i:i+len(old)] == old: 
            res += new  
            i += len(old)  
        else:
            res += s[i] 
            i += 1 
    return res


# Problem 12: Generate Acronym
def generate_acronym(phrase: str) -> str:
    """
    Generates an acronym from the input phrase by using the first letter of each word.
    """

    w = phrase.split() 
    res = ""  
    for word in w:  
        res += word[0].upper()  
    return res


# Problem 13: Validate JSON Keys
def validate_json_keys(data: dict, keys: list[str]) -> bool:
    """
    Checks if all keys in the `keys` list exist in the input dictionary.
    """
    for key in keys:
        if key not in data:
            return False
    return True


# Problem 14: Anagram Checker
def is_anagram(s1: str, s2: str) -> bool:
    """
    Checks if two input strings are anagrams of each other.
    """
    
    s1 = sorted(s1.replace(" ", "").lower()) # clean both strings
    s2 = sorted(s2.replace(" ", "").lower())

    return s1 == s2


# Problem 15: Extract Digits
def extract_digits(s: str) -> list[int]:
    """
    Extracts and returns all digits from the input string as a list.
    """
    res = []

    for i in s: 
        if i.isdigit():
            res.append(int(i))
    return res



# Problem 16: Generate Fibonacci Sequence
def generate_fibonacci(n: int) -> list[int]:
    """
    Generates the first `n` Fibonacci numbers.
    """
    res = [] 
    a, b = 0, 1  
    
    for _ in range(n): 
        res.append(a)  
        a, b = b, a + b 
    
    return res
            
# Problem 17: Group Words by Length
def group_by_length(words: list[str]) -> dict[int, list[str]]:
    """
    Groups words by their lengths and returns a dictionary.
    """
    
    res = {}

    for w in words:
        l = len(w)
        if l in res:
            res[l].append(w)
        else:
            res[l] = [w] # creates separate lists
    
    return res


# Problem 18: Find Key with Maximum Value
def key_with_max_value(d: dict[str, int]) -> str:
    """
    Finds and returns the key with the maximum value in the input dictionary.
    """
    res = None 
    maxval = -9999999999999
    for key, val in d.items():
        if val > maxval:
            maxval = val
            res = key
    return res



# I AM GOING TO HAVE TO IMPORT C0UNTER I DO NOT WANT TO DO THE LONG WAY (aka checking the freq of each manually )


# Problem 19: Most Frequent Element
def most_frequent_element(lst: list[int]) -> int:
    """
    Finds and returns the most frequent element in the input list.
    If there is a tie, the smallest element is returned.
    """

    count = Counter(lst)
    return min(count, key=lambda x: (-count[x], x)) # i need lambda here since it will sort for me in decdnsing order (and then min will be the highest cnt)

    


# Problem 20: Check Sublist
def is_sublist(lst1: list[int], lst2: list[int]) -> bool:
    """
    Checks if `lst1` is a sublist of `lst2`.
    """
    for i in range(len(lst2) - len(lst1) + 1): # subset of both lists aka the differnce
        if lst2[i:i+len(lst1)] == lst1:
            return True
    return False



if __name__ == "__main__":
    # Add test cases or any additional code for testing purposes here
    print("Hello World! Add your test cases here.")


    #  SIMPLEST WAY FOR ME TO DO TEST CASES: COMPARE THE INPUT TO ITS EXPECTED OUTPUT THAT WAY IN PRINTS OUT TRUE OR FALSE IF IT PASSES
    print(count_unique_characters("rudy osuna") == 9)
    print(reverse_words("Rudy Osuna") == "Osuna Rudy")
    print(flatten_list([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5])
    print(filter_evens([1, 2, 3, 4, 5]) == [2, 4])
    print(longest_word(["apple", "banana", "cherry"]) == "banana")
    print(remove_vowels("rudy osuna") == "rdy sn")
    print(count_word_frequencies("rudy rudy osuna") == {'rudy': 2, 'osuna': 1})
    print(is_palindrome("A man a plan a canal Panama") == True)
    print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}) == {'a': 1, 'b': 5, 'c': 4})
    print(common_elements([1, 2, 3], [2, 3, 4]) == [2, 3])
    print(replace_substring("rudy osuna", "osuna", "there") == "rudy there")
    print(generate_acronym("Triton Quantitative Trading") == "TQT")
    print(validate_json_keys({"name": "Alice", "age": 25}, ["name", "age"]) == True)
    print(is_anagram("listen", "silent") == True)
    print(extract_digits("abc123xyz") == [1, 2, 3])
    print(generate_fibonacci(5) == [0, 1, 1, 2, 3])
    print(group_by_length(["apple", "bat", "banana", "cat"]) == {5: ['apple'], 3: ['bat', 'cat'], 6: ['banana']})
    print(key_with_max_value({"a": 1, "b": 2, "c": 3}) == 'c')
    print(most_frequent_element([1, 2, 2, 3, 3, 3]) == 3)
    print(is_sublist([1, 2], [1, 2, 3]) == True)
