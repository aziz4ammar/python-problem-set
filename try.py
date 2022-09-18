def saisir():
    global n
    co = False
    while co == False:
        print("donner un entier de 3 chiffres")
        n = int(input())
        co = (len(str(n)) >= 3 and n > 0)

def ex3(n):
    fi = 0
    ch = str(n)
    if len(ch) % 2 == 0:
        for i in range(len(ch)):
            if i % 2 == 1:
                fi += int(ch[i])
            else:
                fi -= int(ch[i])
    else:
        for i in range(len(ch)):
            if i % 2 == 0:
                fi += int(ch[i])
            else:
                fi -= int(ch[i])
    return fi
def fin(n):
    res = True
    if fi % 11 == 0:
        res = True
    else:
        res = False

    return res

saisir()
fi = ex3(n)
res = fin(n)
print(res)
