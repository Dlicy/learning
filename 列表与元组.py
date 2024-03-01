#list
nums = ['1','2','3']
o = ['7','8','9']
print(nums)
print(nums[0])
print(nums[-1])
print(len(nums))
nums.append('4')
print("加入元素�?:\n",nums)
nums.pop(2)
print("删除3号位�?:\n",nums)
nums[1] = '6'
print("2号位替换�?6:\n",nums)
nums.append(o)
print("加入列表元素:\n",nums)

#tuple
a = ('1','2',['4','5','6'])
print(a)
print(len(a))
a[2][2] = '7'
a[2].append('8')
print("列表内元素改变后:\n",a)

