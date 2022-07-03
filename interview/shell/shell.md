# shell面试大纲：
#### 一、基础
shell结构化命令 <br>
1、if-then，if-then-else，嵌套if语句 <br>
if-then: <br>
if command ; then <br>
command <br>
fi <br>
或 : <br>
if command <br>
then <br>
command <br>
fi <br>

if-then-else: <br>
if command; then <br>
command <br>
else <br>
command <br>
fi <br>
嵌套if语句: <br>
if command; then <br>
command <br>
elif command; then  <br>
more commands <br>
fi <br>

2、test命令（数值比较，字符串比较，文件比较）<br>
3、if-then的高级特性（使用双括号，使用双方括号），case命令 <br>
4、for命令，c语言风格的for命令，while命令，until命令 <br>
5、sed及sed进阶，gawk及gawk进阶 <br>
6、正则表达式
7、系统变量、用户变量、命令替换、重定向输入输出（>,>>,<,<<）、管道、数学运算（expr，[],bc）