# Given a dictionary of words and a string made up of those words (no spaces), 
# return the original sentence in a list. If there is more than one possible reconstruction, 
# return any of them. If there is no possible reconstruction, then return null.

# For example, given the set of words 'quick', 'brown', 'the', 'fox', 
# and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', 
# and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

class Solution:

    new_list = []
    def strtolist (self, str, words):
        new_word = ""
        for char in str:
            new_word = new_word + char
            if new_word in words:
                Solution.new_list.append(new_word)
                length = len(new_word)
                str_list = list(str)
                del str_list[:length]
                new_str = "".join(str_list)
                return self.strtolist(new_str, words)
            else:
                continue
        print(Solution.new_list)          



obj = Solution()
obj.strtolist(str = "thequickbrownfox", words = ['quick', 'brown', 'the', 'fox'])