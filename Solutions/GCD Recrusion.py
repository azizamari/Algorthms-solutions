#Greatest Common Divisor
def gcd(a,b):
    assert int(a)==a and int(b) , 'both numbers have to be integers'
    def gcd_internal(a,b):
        if a%b==0: return b
        return gcd_internal(b,a%b)
    return gcd_internal(max(a,b),min(a,b))
print(gcd(12,24))