# Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
# Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.


# Example 1:



# Input: a = 2, b = 6, c = 5
# Output: 3
# Explanation: After flips a = 1 , b = 4 , c = 5 such that (a OR b == c)


#sol1
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a or b or c:
            bita = a&1
            bitb = b&1
            bitc = c&1
            if bitc == 0:
                flips+=(bita+bitb)
            else:
                if bita == 0 and bitb == 0:
                    flips+=1
            a>>= 1
            b>>= 1
            c>>= 1
        return flips
#solution_2
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        a = bin(a).replace("0b","")
        b = bin(b).replace("0b","")
        c = bin(c).replace("0b","")
        mx = max(len(a),len(b),len(c))
        a = ('0'*abs(len(a) - mx) + a)
        b = ('0'*abs(len(b) - mx) + b)
        c = ('0'*abs(len(c) - mx) + c)
        res = 0
        for i in range(len(a)-1,-1,-1):
            d = 0
            na = int(a[i])
            nb = int(b[i])
            
            if int(a[i])|int(b[i]) != int(c[i]):
                if (na^1)|nb == int(c[i]):
                    d+=1
                if na|(nb^1) == int(c[i]) and d==0:
                    d+=1
                if (na^1)|(nb^1) == int(c[i]) and d==0:
                    d+=2
            res += d
        return res