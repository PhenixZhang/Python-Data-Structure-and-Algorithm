import turtle
def koch(t,order,size):
	if order ==0:  				# 边界条件
		t.forward(size)
	else:
		koch(t,order-1,size/3)	# 递归调用
		t.left(60)				# 笔转60度
		koch(t,order-1,size/3)	# 递归调用
		t.right(120)			# 笔转120度
		koch(t,order-1,size/3)	# 递归调用
		t.left(60)				# 笔转60度
		koch(t,order-1,size/3)	# 递归调用
if __name__ == '__main__':
	koch(turtle,5,500)
	turtle.mainloop()