

class UyghurSyllabification:

    # vowel character
    UYGHUR_VOWELS = ["a", "e", "i", "é", "o", "u", "ö", "ü"]
    # consonants character
    UYGHUR_CONSONANTS = ["b", "p", "t", "c", "ç", "x", "d", "r", "z", "j", "s", "ş", "f", "ğ", "q", "k", "g", "ñ", "l", "m", "v", "y", "h", "n"]
    # hemze
    SPECIAL = ["'", "-", ".", "?", ","]

    def __init__(self):
        self.syl_pos = []

    def reset(self):
        self.syl_pos = []

    def numberOfSyllabification(self, source):
        count = 0
        for i, _ in enumerate(source):
            if (isVolwels(source[i:i + 1])):
                count += 1
        return count

    # Turn the given string to ternary format, which are vowels, constant and hemze
    def getFormatString(self, source):
        target = ""
        for i, l in enumerate(source):
            sub = source[i : i + 1]
            key = sub

            # # jude the double char character
            # if ((sub is "z" or sub is "c" or sub is "s" or sub is "g") and (i < len(source)-1)):
            #     next = source[i+1:i+2]
            #     if (next is "h"):
            #         key = sub + next
            #         i += 1

            # elif((sub is "n") and (i < len(source)-1)):
            #     next = source[i+1:i+2]
            #     if (next is "g"):
            #         key = sub + next
            #         i += 1

            # match keys
            if (self.isVolwels(key)):
                target += "V"
            elif(self.isConsonants(key)):
                target += "C"
            elif(key in self.SPECIAL):
                target += "'"
            else:
                raise  ValueError('Unexpected letter in the word')

        return target

    def find_last_2th_vowel(self, source):
        return source.rfind('V', 0, source.rfind('V'))


    def syllabication(self, source):
        matchRule = self.setMatchRule()
        formatString = self.getFormatString(source)
        begin = 0
        end = 1
        self.syllab(source, formatString, matchRule)

        return self.show_syllabs(source)



    def show_syllabs(self, source, mark="/"):
        # for i in range(len(self.syl_pos), 0, -1):
        #     print(self.syl_pos[i-1])
        indices = [0] + self.syl_pos[::-1]
        parts = [source[i:j] for i, j in zip(indices, indices[1:] + [None])]
        self.reset()
        return '/'.join(parts)



    # def syllab(self, source, formatString, matchRule):
    #     if self.find_last_2th_vowel(formatString) is not -1:
    #         format_current = formatString[self.find_last_2th_vowel(formatString):]
    #     else:
    #         return
    #     format_rest = formatString[:self.find_last_2th_vowel(formatString)]
    #
    #     relative_split_pos =  format_current.find("'")
    #     if relative_split_pos is  -1:
    #         relative_split_pos = matchRule[format_current]
    #     format_rest += format_current[:relative_split_pos]
    #     self.syl_pos.append(len(format_rest))
    #     # print(format_rest)
    #     # print(source[:len(format_rest)])
    #     return self.syllab(source, format_rest,  matchRule)

    def syllab(self, source, formatString, matchRule):
        # print(formatString)
        if self.find_last_2th_vowel(formatString) is not -1:
            format_current = formatString[self.find_last_2th_vowel(formatString):]
        else:
            return
        format_rest = formatString[:self.find_last_2th_vowel(formatString)]

        relative_split_pos = format_current.find("'")
        if relative_split_pos is -1:
            relative_split_pos = matchRule[format_current]
        else:
            if len(self.syl_pos) is not 0:
                self.syl_pos.append(len(format_rest) + relative_split_pos + 1)

        format_rest += format_current[:relative_split_pos]
        self.syl_pos.append(len(format_rest))
        # print(format_rest)
        # print(source[:len(format_rest)])
        return self.syllab(source, format_rest, matchRule)

    def setMatchRule(self):

        # default match rule rule for Uyghur language
        matchRule = {}
        matchRule["VCCV"] = 2
        matchRule["VCCVCC"] = 2
        matchRule["VCVCC"] = 2
        matchRule["VCCVC"] = 2
        matchRule["CVCCV"] = 3
        matchRule["CVCCVC"] = 3
        matchRule["CCVCCVC"] = 4
        matchRule["VCV"] = 1
        matchRule["CVCV"] = 2
        matchRule["VCVC"] = 1
        matchRule["CVCVC"] = 2
        matchRule["CVCVCC"] = 2
        matchRule["CCVCV"] = 3
        matchRule["VCCCV"] = 3
        matchRule["CVCCCV"] = 3
        matchRule["VCCCCV"] = 3
        matchRule["CVVCCV"] = 4
        matchRule["VV"] = 1

        return matchRule

    def setVowelCharacterSet(self, vowels):
        if(vowels is not null):
            VOWELS = vowels
        else:
            VOWELS = UYGHUR_VOWELS

    def setConsonantCharacterSet(self, consonants):
        if(consonants is not null):
            CONSONANTS = consonants
        else:
            CONSONANTS = UYGHUR_CONSONANTS


    def isVolwels(self, achar):
        if achar in self.UYGHUR_VOWELS:
            return True
        else:
            return False

    def isConsonants(self, achar):
        if achar in self.UYGHUR_CONSONANTS:
            return True
        else:
            return False