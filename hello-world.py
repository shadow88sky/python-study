﻿#第一步，输出hello-world
#注释说明，单行注释采用#
#python没有块级注释，所以现在推荐的多行注释也是采用的#
print "Hello World!"


#print函数
#用print加上字符串，就可以在屏幕上输出指定的文字.
#print语句也可以跟上多个字符串，用逗号“,”隔开，就可以连成一串输出：
print('qwe','fdasf')

#print也可以打印整数
print(10+20)

#标示符,python中由字母、数字、下划线组成，但不能以数字开头
#python严格区分大小写
#以下划线开头的标识符是有特殊意义的。以单下划线开头（_foo）的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用"from xxx import *"而导入；
#以双下划线开头的（__foo）代表类的私有成员；以双下划线开头和结尾的（__foo__）代表python里特殊方法专用的标识，如__init__（）代表类的构造函数。
#学习Python与其他语言最大的区别就是，Python的代码块不使用大括号（{}）来控制类，函数以及其他逻辑判断。python最具特色的就是用缩进来写模块。
#缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行。如下所示：
if True:
	print ("True")
else:
	print ("False")

#Python语句中一般以新行作为语句的结束符。但是我们可以使用斜杠（\）将一行的语句分为多行显示，如下所示：
total = 2 + \
        3 + \
        4

#语句中包含[], {} 或 () 括号就不需要使用多行连接符。如下实例：
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']

#Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：
import sys; x = 'foo'; sys.stdout.write(x + '\n')

#缩进相同的一组语句构成一个代码块，我们称之代码组。像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
#我们将首行及后面的代码组称为一个子句(clause)。如下实例：
if 'expression' : 
   1 
elif 'expression' :  
   2  
else :  
   3 