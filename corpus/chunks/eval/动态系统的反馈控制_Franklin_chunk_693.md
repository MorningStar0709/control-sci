(a) 写出描述该反馈系统运行的微分方程。  
(b) 写出关于 $\theta_{0}$ ， $\theta_{i}(s)$ 的综合补偿器的传递函数 $D_{c}(s)$   
(c) 以电动机的电枢电压 $v_{a}$ 作为输入，电位计的电压 $E_{0}$ 作为输出，得到系统的开环频率响应数据如表 10.4 所示。假设电动机是线性的，且有最小相角。可推断出电动机的传递函数为

$$G (s) = \frac {\theta_ {\mathrm{m}} (s)}{V _ {\mathrm{a}} (s)}$$

其中： $\theta_{m}$ 为电动机轴的角位置。

表 10.4 习题 10.17 的频率响应数据

<table><tr><td>频率/(rad/s)</td><td> $\frac{E_o(S)}{V_a(S)}$ </td><td>/dB</td></tr><tr><td>0.1</td><td>60.0</td><td></td></tr><tr><td>0.2</td><td>54.0</td><td></td></tr><tr><td>0.3</td><td>50.0</td><td></td></tr><tr><td>0.5</td><td>46.0</td><td></td></tr><tr><td>0.8</td><td>42.0</td><td></td></tr><tr><td>1.0</td><td>40.0</td><td></td></tr><tr><td>2.0</td><td>34.0</td><td></td></tr><tr><td>3.0</td><td>30.5</td><td></td></tr><tr><td>4.0</td><td>27.0</td><td></td></tr><tr><td>5.0</td><td>23.0</td><td></td></tr><tr><td>7.0</td><td>19.5</td><td></td></tr><tr><td>10.0</td><td>14.0</td><td></td></tr><tr><td>20.0</td><td>2.0</td><td></td></tr><tr><td>40.0</td><td>-10.0</td><td></td></tr><tr><td>60.0</td><td>-20.0</td><td></td></tr><tr><td>65.0</td><td>-21.0</td><td></td></tr><tr><td>80.0</td><td>-24.0</td><td></td></tr><tr><td>100.0</td><td>-30.0</td><td></td></tr><tr><td>200.0</td><td>-48.0</td><td></td></tr><tr><td>300.0</td><td>-59.0</td><td></td></tr><tr><td>500.0</td><td>-72.0</td><td></td></tr></table>

(d) 确定一组适合位置控制系统的性能指标，从而获得最佳性能。设计 $D_{v}(s)$ 以满足这些性能指标。  
(e) 利用 Matlab 进行分析与仿真，对设计进行校验。

10.18 设计并构造一个能使小球位于自由摆杆中心的装置。该装置如图 10.97 所示。将线圈缠绕在永磁铁上作为执行器来移动横轴杆，用太阳能电池测量小球的位置，用一个具有霍尔效应的装置来测量横杆的位置。研究其他可行的执行器和传感器。将只用球位置作为反馈量所获得的控制效果与同时使用球和杆的位置作为多环反馈量所获得的控制效果进行比较。

![](image/4f3f5c118d742cc531a2ed6a46f325f516b425db070c868b2ddafdc34ceb1289.jpg)

<details>
<summary>natural_image</summary>

Experimental setup with labeled components and wiring (no visible text or symbols)
</details>

图 10.97 球平衡器设计例子

10.19 设计并构造如图 9.2 所示的磁悬浮装置。在设计过程中不妨用 LEGO 组件进行设计。  
10.20 使用 Arduino 板及相关软件设计并构造一个 Sun 追踪器。  
10.21 批次控制：考虑如图 10.98 所示的快速热处理(RTP)系统。我们要加热一块半导体晶片，使用卤钨灯精确控制晶片的表面温度。系统的输出温度 T 是关于时间的函数，即 $y = T(t)$ 。系统的参考输入 R 是要求温

度(700℃)时的跃阶。控制输入为灯管的功率。高温计用来测量晶片中心的温度。系统模型为一阶，所用的积分控制器如图10.98所示。通常，传感器无误差(b=0)。
