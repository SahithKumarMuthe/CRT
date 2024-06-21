'''lst is given  with even odd and float numbers return the even sum,odd sum and float sum sperately'''
list1=[1,2,3,4,5,6.0,7.0,8.0,9,10]
even_sum,odd_sum,float_sum=0,0,0
for num in list1:
    if isinstance(num,int):
        if num%2==0:
            even_sum+=num
        else:
            odd_sum+=num
    elif isinstance(num,float):
        float_sum+=num
print(even_sum,odd_sum,float_sum)
