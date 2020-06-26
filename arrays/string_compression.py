#Implement String compression using the counts of repeated characters. For example, aabccccaaa would become a2b1c4a3. If the compressed string does not become smaller, then return the original string.
input1 = 'aaaabbbbcccccaaaaddd'
input2 = 'asdcdccddffeee'

def string_compression(string):
    if len(string) == 0:
        return string
    compressed_str = ''
    count = 1
    for i in range(len(string)-1):
        if (string[i] == string [i+1]):
            count += 1
        else:
            compressed_str += string[i] + str(count)
            count = 1
    compressed_str += string[i] + str(count)

    if(len(compressed_str) >= len(string)):
        return string
    else:
        return compressed_str

if __name__ == "__main__":
    print('Original test 1 -> ', input1)
    print('Transformed test 1 ->',  string_compression(input1))
    print('Original test 2 ->', input2)
    print('Transformed test 2 ->', string_compression(input2))
