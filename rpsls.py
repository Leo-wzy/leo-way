#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock,������һ����Ϸ�������RPSLS��Ϸ
����:��׿��
����:2020.3.10
"""


import random               #������������������


def name_to_number(name):   #�������ֱ�����ֵĺ���
	"""
	����Ϸ�����Ӧ����ͬ������
	"""
	if name==str('ʯͷ') :  #�趨��ͬ��������������Ӧ�����ֵ�������ʽ
		number=0
		return number
	elif name==str('ʷ����') :
		number=1
		return number
	elif name==str('ֽ' ) :
		number=2
		return number
	elif name==str('����') :
		number=3
		return number
	elif name==str('����') :
		number=4
		return number
	else :	
		number=43           #�������������������ֱ�ɵ�һ���趨����(>4)
		return number
    	


def number_to_name(number):  #�������ֱ�����ֵĺ���
	"""
	������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
	"""
	if number==0 :           #�趨��Ӧ���ֱ����Ӧ���ֵ�������ʽ
		name=str("ʯͷ")
		return name 
	elif number==1 :
		name=str("ʷ����")
		return name
	elif number==2 :
		name=str("ֽ")
		return name
	elif number==3 :
		name=str("����")
		return name
	else :
		name=str("����")
		return name




def rpsls(player_choice):                          #����RPSLS��Ϸ�Ĺ���
	"""
	�û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
	"""
	print("----------")                            #��Ļ���"-------"
	print("����ѡ��Ϊ:",choice_name)                 #��Ļ���������������

	player_choice=choice_name                      #����������ָ�ֵ�����庯����
	choice_number=name_to_number(player_choice)    #����number_to_name����������������ֱ�Ϊ��Ӧ������

	random_number=random.randint(0,5)              #������������������0,1,2,3,4 ����һ��
	random_name=number_to_name(random_number)      #����name_to_number����������������ֱ�Ϊ��Ӧ������

	print("������ѡ��Ϊ:",random_name)               #��Ļ��������������������
	if choice_number - random_number <=2 :         #��������RPSLS��Ϸ�Ĺ���,�������Ӧ���
		if choice_number==random_number :
			print("���ͼ��������һ����")
		elif random_number - choice_number == 2  or  random_number - choice_number == 1 :
			print("����Ӯ��")
		else :
			print("��Ӯ��")
	elif choice_number - random_number ==3 or choice_number - random_number ==4 :
		print("����Ӯ��")
	else :                                         #����������������������
		print("Error: No Correct Name")
	        
  

print("��ӭʹ��RPSLS��Ϸ")    #��Ļ��������
print("----------------")   #���"---------"
print("����������ѡ��:")      #��ʾ�������ѡ�������
choice_name=input()
rpsls(choice_name)          #����RPSLS��Ϸ����








