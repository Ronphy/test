#Σ(n,k=0)nCkの計算

def main_3():
    #nCkの計算関数 正確にはnCkをそれぞれk=0~6まで計算してそれらを配列にして返している
    def list_combination(n):
        v = 1
        C = []
        for k in range(n+1):
            C.append(v)
            v *= (n-k)
            v //= (k+1)
        return C

    #実際の計算
    n = 6

    s = 0
    for v in list_combination(n): #list_combination(n)はn=6のとき配列C = [1,6,15,20,15,6,1]と考えることができる
        print(v)
        s += v





if __name__ == "__main__":
    main_3()