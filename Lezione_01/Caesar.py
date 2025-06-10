#Ammetto che non ero sicurissimo di come fare per quanto 
#riguardasse la gestione dei caratteri eccetto
#Una maniera meno efficiente creandomi un alfabeto custom
#Ma a quanto pare su stackoverflow consigliano di usare ord()
#per fare uso dell'alfabeto ASCII

class Caesar:
    def encrypt(s:str, key:int) -> str:
        result = ""
        for i in range(len(s)):
            char = s[i]
            if char == " ":
                result += char
            elif char.isupper() == True:
                result += chr((ord(char) + key-65) % 26 + 65)
            else:
                result += chr((ord(char) + key-97) % 26 + 97)
        return result
    
    def decrypt(s, key) -> str:
        result = ""
        for i in range(len(s)):
            char = s[i]
            if char == " ":
                result += char
            elif char.isupper() == True:
                result += chr((ord(char) - key-65) % 26 + 65)
            else:
                result += chr((ord(char) - key-97) % 26 + 97)
        return result
    

