n = input("整数を入力してください:")

# 入力した値を整数にしなければいけない int(n)
# 空のnumbersに[0,1,2,3,4,5]のうち1～6(1,2,3,4,5)を入れる
numbers = list(range(1, int(n)+1))
# numbers[1,2,3,4,5]の合計
total = sum(numbers)
# len()でnumbers[1,2,3,4,5]の長さ(5)を出す
average = total/len(numbers)
print(f"1~{n}までの合計：{total}")
print(f"平均：{average}")



# 板書したコード
total = 0
average = 0
# 入力した値を整数へ
num = int(n)
i = 0
while i <= num:
    total += i
    i += 1
average = total / num
print(f"1~{n}までの合計：{total}")
print(f"平均：{average}")
