#coding=windows-1251
print("Минимальная сумма инвестиций:")
s=int(input())
print("Средства Майкла:")
m=int(input())
print("Средства Ивана:")
i=int(input())
if (m>s) and (i>s):
    print("2")
elif ((m>s) and (i<s)):  
    print("Mike")
elif ((m<s) and (i>s)):
    print("Ivan")
elif ((m+i)>s):
    print(1)
else:
    print(0)

