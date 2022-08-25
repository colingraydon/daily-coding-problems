# Soundex is an algorithm used to categorize phonetically, such that two names that sound alike but are spelled differently have the same representation.

# Soundex maps every name to a string consisting of one letter and three numbers, like M460.

# One version of the algorithm is as follows:

# Remove consecutive consonants with the same sound (for example, change ck -> c).
# Keep the first letter. The remaining steps only apply to the rest of the string.
# Remove all vowels, including y, w, and h.
# Replace all consonants with the following digits:
# b, f, p, v → 1
# c, g, j, k, q, s, x, z → 2
# d, t → 3
# l → 4
# m, n → 5
# r → 6
# If you don't have three numbers yet, append zeros until you do. Keep the first three numbers.
# Using this scheme, Jackson and Jaxen both map to J250.


#this is drastically over simplified and there are many consonant combinations and edge cases which are not addressed here
#I just wanted to show a basic implementation where more consonant checks can be added easily
#A basic examination of consonant clusters showed that typically, only words with up to 3 consonants in a row can have identitical pronuncations, ie jackson/jaxen
#Therefore, 2 passes through a string should suffice for this simple implementation
#I am uncertain, based on the prompt, if consecutive repeat consonants shoudl be repeated - my interpretation is that they should
class Soundex:

    def map(s):

        first = s[0]
        #changing the similar sounding consonants
        s = Soundex.consonant_check(s)
        s = Soundex.consonant_check(s)
        #removes duplicate consonants
        i = 0
        while (i < len(s) - 1):
            if s[i] == s[i+1]:
                s = s[:i] + s[i+1:]
        #remove vowels
        i = 0
        vowels = ["a", "e", "i", "o", "u", "w", "y", "h"]
        temp_str = s
        while (i < len(s)):
            if s[i] in vowels:
                temp_str = s[:i] = s[i+1:]
        s = temp_str
        #map to new string
        consonant_dict = {"b": 1, "f": 1, "p": 1, "v": 1, "c": 2, "g": 2, "j": 2, "k":2, "q": 2, "s": 2, "x":2, "z": 2, "d": 3, "t": 3, "l":4, "m": 5, "n": 5, "r": 6}
        for i in s:
            s[i] = consonant_dict[i]
        output = first + s
        #change length of output
        l = len(output)
        if (l < 4):
            while (l < 4):
                s = s + "0"
        if (l > 4):
            s = s[:4]

        return s


    #more consonant combinations can be added in this dict
    #must run this before removing vowels because gh sounds like f but g and f map to different values
    def consonant_check(s):
        #more consonant combinations can be added
        d = {"ck" : "c", "gh" : "f", "cx" : "x", "kx" : "x"}
        i = 0
        for i in range(len(s) - 2):
            temp = s[i] + s[i+1]
            if temp in d:
                s = s[:i] + d[temp] + s[i+2:]