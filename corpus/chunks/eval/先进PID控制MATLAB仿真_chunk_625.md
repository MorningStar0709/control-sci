# 16.2.3 主程序的实现

采用 LQR 控制算法实现倒立摆和小车的控制，主程序 dlb.m 包括以下几个部分。

（1）模型参数创建：采用 mc\_CreateFcn()、mc\_Callback() 实现小车质量的创建，同理可实现摆杆长度和质量的创建。  
（2）LQR 参数创建：采用 qi\_CreateFcn() 和 qi\_Callback() 实现 $q_{i}$ ，i = 1, 2, 3, 4。采用 r\_CreateFcn() 和 r\_Callback() 实现 R。  
（3）采用 LQR 计算 K：由 lqrok\_Callback() 实现。  
（4）K 的创建：采用 ki\_CreateFcn() 和 ki\_Callback() 实现 $K_{i}$ ，i = 1, 2, 3, 4。  
（5）摆杆角度和小车位置初始值设定：实现小车水平位置创建与回调、小车水平拖动条的创建与回调，摆杆角度创建与回调、摆杆角度拖动条的创建与回调。  
（6）干扰的输入：共有冲击、阶跃和正弦三种干扰可以选择。  
（7）仿真时间和步长的设定：Tedit\_CreateFcn()和Step\_CreateFcn()。  
(8) 仿真启动的设定。

（9）重置按钮：reset\_Callback()，实现倒立摆模型参数和 LQR 参数的重置。  
(10) 退出: exit\_Callback()。

![](image/bf9f8b677b2b796a1be4c94e0d7a7ec14b9d888ff3229b5d0cdd29430bcae313.jpg)
