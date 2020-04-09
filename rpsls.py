#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock,即设置一个游戏编码完成RPSLS游戏
作者:王卓雅
日期:2020.3.10
"""


import random               #计算机产生随机的数字


def name_to_number(name):   #定义名字变成数字的函数
	"""
	将游戏对象对应到不同的整数
	"""
	if name==str('石头') :  #设定不同的名字输入变成相应的数字的条件公式
		number=0
		return number
	elif name==str('史波克') :
		number=1
		return number
	elif name==str('纸' ) :
		number=2
		return number
	elif name==str('蜥蜴') :
		number=3
		return number
	elif name==str('剪刀') :
		number=4
		return number
	else :	
		number=43           #不满足输入条件的名字变成的一个设定数字(>4)
		return number
    	


def number_to_name(number):  #定义数字变成名字的函数
	"""
	将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
	"""
	if number==0 :           #设定相应数字变成相应名字的条件公式
		name=str("石头")
		return name 
	elif number==1 :
		name=str("史波克")
		return name
	elif number==2 :
		name=str("纸")
		return name
	elif number==3 :
		name=str("蜥蜴")
		return name
	else :
		name=str("剪刀")
		return name




def rpsls(player_choice):                          #定义RPSLS游戏的规则
	"""
	用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果
	"""
	print("----------")                            #屏幕输出"-------"
	print("您的选择为:",choice_name)                 #屏幕输出玩家输入的名字

	player_choice=choice_name                      #将输入的名字赋值到定义函数中
	choice_number=name_to_number(player_choice)    #调用number_to_name函数，将输入的名字变为相应的数字

	random_number=random.randint(0,5)              #计算机产生随机的数字0,1,2,3,4 其中一个
	random_name=number_to_name(random_number)      #调用name_to_number函数，将输入的名字变为相应的数字

	print("机器的选则为:",random_name)               #屏幕输出计算机随机输出的名字
	if choice_number - random_number <=2 :         #定义满足RPSLS游戏的规则,与最后相应结果
		if choice_number==random_number :
			print("您和计算机出的一样呢")
		elif random_number - choice_number == 2  or  random_number - choice_number == 1 :
			print("机器赢了")
		else :
			print("您赢了")
	elif choice_number - random_number ==3 or choice_number - random_number ==4 :
		print("机器赢了")
	else :                                         #不满足题设条件的输出结果
		print("Error: No Correct Name")
	        
  

print("欢迎使用RPSLS游戏")    #屏幕输出该语句
print("----------------")   #输出"---------"
print("请输入您的选择:")      #提示玩家输入选择的名字
choice_name=input()
rpsls(choice_name)          #运用RPSLS游戏规则








