class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):
        storage = {}
        output = []
        for i in range(0,len(s)):
            ss = s[i:i+10]
            if ss in storage:
                storage[ss] += 1
            else:
                storage[ss] = 1
                
        for key in storage:
            if storage[key] > 1:
                output.append(key)
        
        return output
