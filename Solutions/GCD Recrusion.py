#Greatest Common Divisor
def gcd(a,b):
    def gcd_internal(a,b):
        if a%b==0: return b
        return gcd_internal(b,a%b)
    return gcd_internal(max(a,b),min(a,b))
print(gcd(12,24))