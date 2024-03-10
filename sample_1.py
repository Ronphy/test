def main():


    """user_number = input("input number:") #str入力

    print(type(user_number))

    user_number = int(user_number)

    if user_number > 5:
        print("5より大きい")
    else:
        print("違う")"""
    

    N = 10
    for n in range(2, N+1):
        print(n)
        for a in range(2, n//2+1):
            if n % a == 0:
                print(n, '=', a, '*', n//a)
                break

    #list作成方法 2通り
    a = []
    a = list()

    a = [0,1,4,9,16,25,36,49]
    #配列を前から順番に表示
    for x in a:
        print(x)

    wd = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    #配列末尾に要素を追加する
    wd.append('saturday')
    #指定した要素を削除する
    del wd[5]
    #リストを連結して新しいリストを作成する
    d = wd + ['saturdeay', 'sunday']

    #ある要素がリストに含まれるか調べる
    'sun' in d

    #配列作成方法　例
    m = [[i * j for i in range(10)] for j in range(5)]
    print(m)

    
    d = {
    '東京': ['とうきょう', 'Tokyo'],
    '神奈川': ['かながわ', 'Kanagawa'],
    '千葉': ['ちば', 'Chiba'],
    '埼玉': ['さいたま', 'Saitama']
    }
    r = {}
    #表示
    print(d['東京'])
    #ファイルへの書き込み
    with open('prefecture3.txt', 'w') as fo:
        for ja, (yomi, en) in d.items():
            print(ja, yomi, en, file=fo)
    #フィルからの読み込み
    with open('prefecture.txt') as fi:
        for line in fi:
            #print(line.strip('\n'))#「.strip('\n)」改行を取り除く
            #辞書に格納
            values = line.strip('\n').split(' ')
            r[values[0]] = values[1:]
    
    #print(r)#確認用表示


    

if __name__ == "__main__":
    main()