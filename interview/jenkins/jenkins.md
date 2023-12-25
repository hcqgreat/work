# jenkins知识图谱
#### 声明式流水线结构概览及解释
![](png/声明式流失线结构概览.png)
Pipeline  声明式流水线标志符 <br>
agent  指定流水线或阶段在那个节点运行，共7中配置<br>
agent ang <br>
agent none <br>
agent {lable <label>} <br>
agent {docker <image>} <br>
agent {docker <elements>} <br>
agent {dockerfile true} <br>
agent {dockerfile <elements>} <br>

environment 指定流水线或阶段的环境变量，可选指令 <br>
tools 指定哪些工具需要在流水线节点上安装 <br>
options 指定流水线的一些属性和值 <br>
triggers 指定使用什么类型的触发器来启动你的流水线构建 <br>
cron <br>
upstream <br>
githubPush <br>
pollSCM <br>
parameters 为流水线指定项目参数 <br>
booleanParam <br>
choice <br>
file <br>
text <br>
password <br>
run <br>
string <br>
