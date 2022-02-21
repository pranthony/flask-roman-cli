class Convert:
    def start(self):
        print(self.__str__())
        flag = True
        while flag:
            try:
                number = int(input('Decimal Number: '))
                flag=self.ask('Roman Number: '+self.toRoman(abs(number)))
            except ValueError:
                flag = self.ask('Value Error')
    def ask(self, msj:str):
        while True:
            print(msj)
            op = input('Exit: y/n? ').lower()
            if op == 'y':
                flag = False     
                break
            elif op == 'n':
                flag = True
                break
        return flag
    def toRoman(self, num :int)->str:
        romans = ['I', 'V','X', 'L','C','D','M']
        #array = str(num)
        self.descomponer(num, array:=[])
        roman,n = '',1
        
        for i in array[::-1]:
            digit = ''
            for j in range(1, int(i)+1):
                if(j == 4):
                    digit = romans[n]+romans[n-1]
                    continue 
                if(j == 5):
                    digit = romans[n]
                    continue
                if(j == 9):
                    digit = romans[n-1]+romans[n+1]
                    continue
                if j == 10:
                    digit = romans[n+1]
                    continue
                digit += romans[n-1];
            n+=2
            roman = digit + roman 
        return roman
    def descomponer(self, num, array):
        if not num//10:
            array.insert(0, num)
        else:
            array.insert(0, num%10)
            self.descomponer(num//10, array)
    def __str__(self) -> str:
        return 'Welcome To Roman Convert'

Convert().start()