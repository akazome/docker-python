def avg(x,y,z):
    avg_result = (x+y+z)/3
    return avg_result

a = input("３つの数字の平均を算出します。最初の数字を入力してください")
a = int(a)
b = input("2番目の数字を入力してください")
b = int(b)
c = input("3番目の数字を入力してください")
c = int(c)
avg_resulut = avg(a,b,c)
print(avg_resulut)