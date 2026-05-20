# 8.4.2 超前补偿器

使用 PD 控制可以提高系统的响应速度,从物理意义角度考虑,微分项与误差的变化率 $\frac{\mathrm{d}e(t)}{\mathrm{d}t}$ 成正比,因此可以“预测”误差的变化趋势并提前做出反应。需要说明的是,PD 控制具有两个明显的缺陷:第一,PD 控制器需要额外的能量来源,无法通过被动元件实现;第二,PD 控制器会放大高频噪声。以上两点的详细说明参考 9.5 节。

引入超前补偿器(Lead Compensator)可以避免 PD 控制的缺陷,其表达为

$$
C (s) = \frac {s - s _ {\mathrm{zc}}}{s - s _ {\mathrm{pc}}} \tag {8.4.6}
$$

其中， $s_{pc}<s_{zc}<0$ 。超前补偿器的设计思路是同时为系统增加一个极点和一个零点，且零点的位置比极点更加靠近虚轴。针对8.4.1节的例子，新增的这一对极点/零点如图8.4.6所示，只需要保障 $\varphi_{z}-\varphi_{p}=\frac{1}{6}\pi$ ，便可以满足式(8.3.7)中 $\varphi_{z}-\left(\varphi_{p}+\frac{2\pi}{3}+\frac{\pi}{2}\right)=-\pi$ 的条件。加入超前补偿器后的系统框图如图8.4.7(a)所示。

![](image/f2b3e25c686a2da763cfc3bc38e772b83d0ab19454ac3fcc296674f6b71c3c67.jpg)

<details>
<summary>text_image</summary>

-3+2\u221a3j
φp
φz
spc
szc
-3
φ2=1/2π
-1
2/3π
O σ
jω
</details>

图 8.4.6 超前补偿器的设计思路

根据图 8.4.6, 在使用超前补偿器后, 闭环传递函数的根轨迹必然存在着一条分支从新增加的极点 $s_{\mathrm{pc}}$ 指向零点 $s_{\mathrm{zc}}$ , 而另外两条根轨迹将从原开环传递函数极点 $s_{\mathrm{p1}} = -1$ 和 $s_{\mathrm{p2}} = -3$ 出发, 在实轴相会并沿着渐近线指向无穷。其渐近线与实轴的交点为

$$
\sigma_ {a} = \frac {\sum s _ {\mathrm{pn}} - \sum s _ {\mathrm{zm}}}{n - m} = \frac {- 1 - 3 + s _ {\mathrm{pc}} - s _ {\mathrm{zc}}}{3 - 1} = - 2 + \frac {s _ {\mathrm{pc}} - s _ {\mathrm{zc}}}{2} <   - 2 \tag {8.4.7a}
$$

夹角为

$$
\theta = \frac {2 q + 1}{n - m} \pi = \frac {2 q + 1}{3 - 1} \pi , \quad q = 0, 1
$$

$$
\Rightarrow \left\{ \begin{array}{l} \theta_ {1} = \frac {1}{2} \pi \\ \theta_ {2} = \frac {3}{2} \pi = - \frac {1}{2} \pi \end{array} \right. \tag {8.4.7b}
$$

其根轨迹如图 8.4.7(b) 所示。

比较图 8.4.7(b) 和图 8.4.2(a)，可以发现渐近线与实轴的交点在超前补偿器的作用下被“拉向远离虚轴的方向”，因此提高了系统的响应速度。

超前补偿器内容请扫描此二维码观看。
