# 2.2.1 基本原理

可根据带有时滞环节的一阶近似模型的阶跃响应来整定 PID。该模型表示为

$$G (s) = \frac {K}{T s + 1} \mathrm{e} ^ {- \tau s} \tag {2.1}$$

式中，一阶响应的特征参数 K 、 T 和 $\tau$ 可以由图 2-1 所构成的示意图提取出来。

响应曲线法是根据给定对象的瞬态响应特性参数 K 、 T 和 $\tau$ 来确定 PID 控制器的参数，整定公式如表 2-1 所示 $^{[2]}$ 。如果单位阶跃响应曲线为 S 形曲线，则可用此法，否则不能用。

PID 控制算法为

$$u (t) = \frac {1}{\delta} \left(e + \frac {1}{T _ {\mathrm{I}}} \int_ {0} ^ {t} e \mathrm{d} t + T _ {\mathrm{D}} \frac {\mathrm{d} e}{\mathrm{d} t}\right) \tag {2.2}$$

式中， $\delta$ 为比例度； $T_{I}$ 为积分时间； $T_{D}$ 为微分时间。

如果取 $k_{\mathrm{p}} = \frac{1}{\delta}$ ， $k_{\mathrm{i}} = \frac{k_{\mathrm{p}}}{T_{\mathrm{I}}}$ ， $k_{\mathrm{d}} = k_{\mathrm{p}}T_{\mathrm{D}}$ ，则PID控制律表示为

![](image/1d776a69d61818f6ac0f24ecd855a2527a2313eba8bbf4df34891bde3f891857.jpg)

<details>
<summary>text_image</summary>

y
Δr
O
t
y
拐点
Δy
O
τ
T
t
</details>

图 2-1 开环系统对阶跃输入信号的响应曲线示意图

$$u (t) = k _ {\mathrm{p}} e + k _ {\mathrm{i}} \int_ {0} ^ {t} e \mathrm{d} t + k _ {\mathrm{d}} \frac {\mathrm{d} e}{\mathrm{d} t} \tag {2.3}$$

该方法首先要通过实验测定开环系统对阶跃输入信号的响应曲线，具体步骤如下。

（1）首先进行开环控制，断开反馈通道，给被控对象一个阶跃输入信号 $\Delta u$ ；

(2) 记录被控对象的输出特性曲线;

（3）从曲线上求得参数 $u_{\min}$ 、 $u_{\max}$ 、 $y_{\min}$ 、 $y_{\max}$ 、T和 $\tau$ ;

(4) 计算 K 和飞升速度 $\varepsilon$ ;

（5）根据所求的 $\tau$ 和 $\varepsilon$ ，按表 2-1 的经验公式求出不同类型的控制器参数。

K 和 $\varepsilon$ 按下式计算:

$$K = \frac {\frac {\Delta y}{y _ {\max} - y _ {\min}}}{\frac {\Delta u}{u _ {\max} - u _ {\min}}} , \varepsilon = \frac {K}{T} \tag {2.4}$$

表 2-1 响应曲线法整定 PID 参数

<table><tr><td>控制器类型</td><td>比例度 $\delta (\%)$ </td><td>积分时间 $T_{\mathrm {I}}$ </td><td>微分时间 $T_{\mathrm {D}}$ </td></tr><tr><td>P</td><td> $\varepsilon\tau$ </td><td></td><td></td></tr><tr><td>PI</td><td>1.1 $\varepsilon\tau$ </td><td>3.3 $\tau$ </td><td></td></tr><tr><td>PID</td><td>0.85 $\varepsilon\tau$ </td><td>2 $\tau$ </td><td>0.5 $\tau$ </td></tr></table>

式中， $\Delta u$ 为输入信号的阶跃值； $u_{min}$ 和 $u_{max}$ 为输入信号的最大值和最小值； $y_{min}$ 和 $y_{max}$ 为对象输出的最大值和最小值。

![](image/600058fff9b85fe794350ccaa4a46dadd094b623169dea30511a8ec985533019.jpg)
