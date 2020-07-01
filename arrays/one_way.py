"""
jde
An edit between two strings is one of the following changes.

Add a character
Delete a character
Change a character
Given two string s1 and s2, find if s1 can be converted to s2 with exactly one edit. Expected time complexity is O(m+n) where m and n are lengths of two strings

"""

def one_way(str1, str2):
    diff = abs(len(str1) -len(str2))
    if diff > 1:
        return False
    elif(diff == 0):
        diff_count = 0
        for i in xrange(len(str1)):
            if str1[i] != str2[i]:
                diff_count += 1
                if diff_count > 1:
                    return False
        return True
    else:
        if len(str1) > len(str2):
            longer, shorter = str1, str2
        else:
            longer, shorter = str2, str1
        shift = 0
        for i in xrange(len(shorter)):
            if shorter[i] != longer[i + shift]:
                if(shift or (shorter[i] != longer[i + 1])):
                    return False
                shift = 1
        return True

    if __name__ == "__main__":
        import sys
        print(one_way(sys.argv[-2], sys.argv[-1]))
