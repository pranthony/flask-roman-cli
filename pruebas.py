import unittest
"forma recursiva"

def descomponer(num: int, array: list, callback= lambda digito, indice :digito):
    
    if not num//10:
        array.insert(0,callback(num, len(array)))
    else: 
        array.insert(0,callback(num%10, len(array)))
        descomponer(num//10, array, callback)
        



def romanizar (num:int)->str:
    if not isinstance(num, int):
        raise Exception("No es nùmero")
    if num>4000 or num<0:
        raise Exception("Fuera de limites")
    romans = [
        ["","I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
        ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
        ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
        ["", "M", "MM", "MMM"]
        ]
    array = []
    descomponer(num, array, lambda d, i: romans[i][d] )
    return "".join(array)
    
"forma iterativa"

def romanizar2(num:int)->str:
    if not isinstance(num, int):
        raise Exception("No es nùmero")
    if num>4000 or num<0:
        raise Exception("Fuera de limites")
    val = [1000,900,500,400,100,90,50,40,10,9,5,4,1];
    romans = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"];   
    ans = ""
    i=0
    while num:
        
        while num >= val[i]:
            ans += romans[i]
            num -= val[i]
        i+=1
        
    return ans

class TestRomanizeFunctions(unittest.TestCase):

    def test_romanize1(self):
        self.assertEqual(romanizar(123), 'CXXIII')
    def test_romanize2(self):
        self.assertEqual(romanizar(564), 'DLXIV')
    def test_romanize3(self):
        self.assertEqual(romanizar(2314), 'MMCCCXIV')


if __name__ == '__main__':
    unittest.main()

    
