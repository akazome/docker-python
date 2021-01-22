
def avg(x,y,z):
    avg_result = (x+y+z)/3
    return avg_result

a = input("3つの数の平均を算出、最初の数字を入力してください")
b = input("2つ目の数字を入力してください")
c = input("3つ目の数字を入力してっください")
a = int(a)
b = int(b)
c = int(c)
#d = print(avg(a,b,c))
d = "３つの数字の平均は、{}です".format(avg(a,b,c))
print(d)