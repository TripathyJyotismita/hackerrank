
def merge_the_tools(string, k):
    # your code goes here
    num_subsegments = int(len(string) / k)

    for index in range(num_subsegments):
        # Subsegment string
        substring = string[index * k : (index + 1) * k]
    
        # Subsequence string having distinct characters
        s = ""
    
        # If a character is not already in 's', append
        for char in substring:
            if char not in s:
                s += char
        print(s)
   
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
