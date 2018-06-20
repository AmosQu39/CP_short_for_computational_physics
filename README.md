# balls(离散元框架)
代码托管地址:https://github.com/liuyang0717/balls  
comphy's big homework
>- 离散元框架
>- 锥形堆模拟
>- 分子动力学模拟
>- 框架的后续改进办法

## 离散元框架

>- 项目建立目的
>- 离散元方法基本结构
>- 项目结构

### 项目建立目的

物理学的计算模拟当中,分子动力学模拟是很重要的一部分.分子动力学模拟隶属于离散元方法,是离散元方法当中最为重要的组成部分.作者被linux,python自身的哲学所吸引,对于DRP原则，编程范式,代码规范具有浓厚的兴趣.离散元方法当中有许多分支,从结构上来说并无二致.所以想要写出一个离散元的框架,用以复用.  
这个项目最初是来做多个小球碰撞的,balls成为了它的项目名称,具体的模块名也是依据balls命名.

### 离散元方法基本结构

>- 建立粒子
>- 确定动力学模型
>- 边界作用
>- 更新粒子状态
>- 储存数据
>- 分析处理

### 项目结构

>- 项目规范
>- 项目文件

#### 项目规范
| | 内容 |
| - | - |
| 编程语言 | python3.6 |
| 初始化数据格式 | JSON |
| 数据保存方式 | npy二进制文件 |

#### 项目文件
>- balls  
>	- main.py  
>		- 主函数文件
>	- main_about_picture.py
>		- 生成每帧图片的主函数文件
>	- generate_balls.py  
>		- 生成粒子文件
>	- motion_collision.py  
>		- 粒子运动和边界作用文件
>	- between_collision.py  
>		- 粒子之间相互作用文件
>	- conversion.py  
>		- 数据结构格式转换函数文件
>	- time_axis.py  
>		- 时间轴文件
>	- procession_control.py  
>		- 流程控制文件
>	- data_write.py
>		- 数据保存函数文件
>	- silence_balls.py
>		- 小球休眠文件
>	- tkinter_window.py
>		- tkinter窗口控制文件
>	- draw_picture_gif.py
>		- 绘制每一帧的图片,与GIF动画文件

-----------------------
>	- balls_message,json
>		- 小球初始化数据
>	- boundary_message.json
>		- 边界数据
>	- time_axis_message.json
>		- 时间轴和进程控制数据

## 锥形堆模拟

>- 实际模拟展示
>- 框架复用效果评价

### 实际模拟展示

## 分子动力学模拟

>- 实际模拟展示
>- 框架复用效果评价

## 框架的后续改进办法