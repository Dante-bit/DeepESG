str = input("-->")
for i in range(0, int(len(str)/2)): 
        if str[i] != str[len(str)-i-1]:
            print("palíndromo")
            break
        else:
            print("Não palíndromo")
            break
