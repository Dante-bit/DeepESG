str = input("-->")
for i in range(0, int(len(str)/2)): 
        if str[i] != str[len(str)-i-1]:
            print("Palindromo Palindromo")
            break
        else:
            print("nao palindrono")
            break