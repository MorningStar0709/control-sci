$$\Delta Q _ {i} - \Delta Q _ {o} = \frac {\mathrm{d} V}{\mathrm{d} t} = A \frac {\mathrm{d} \Delta h}{\mathrm{d} t} \tag {2-53}$$

式中，V 为液槽液体贮存量； $\Delta Q_{i}$ 由调节阀开度变化 $\Delta u$ 引起，当阀前后压差不变时，有

$$\Delta Q _ {i} = K _ {u} \Delta u \tag {2-54}$$

其中 $K_{u}$ 为阀门流量系数。

流出量与液位高度的关系为 $Q_{0} = A_{0}\sqrt{2gh}$ ，这是一个非线性关系式，可在平衡点 $(h_0,Q_0)$ 附近进行线性化，得到液阻表达式

$$R = \frac {\Delta h}{\Delta Q _ {o}} \tag {2-55}$$

将式(2-54)和式(2-55)代入式(2-53)，可得

$$T \frac {\mathrm{d} \Delta h}{\mathrm{d} t} + \Delta h = K \Delta u \tag {2-56}$$

式中， $T = RA, K = K_{u}R$ 。在零初始条件下，对式(2-56)两端进行拉氏变换，得到单容水槽的传递函数为

$$G (s) = \frac {\Delta H (s)}{\Delta U (s)} = \frac {K}{T s + 1} \tag {2-57}$$

![](image/37793617cfd1b875b017052e27e5d0d91fb9c10f23d012e9238977f27ed844c9.jpg)

<details>
<summary>text_image</summary>

T₁
Qᵢ
电热丝
u
Qₒ
</details>

图 2-19 电加热炉

电加热炉 在工业生产中, 电加热炉是常见的热处理设备, 其示意图如图 2-19 所示。图中, u 为电热丝两端电压, $T_{1}$ 为炉内温度。设电热丝质量为 M, 比热为 C, 传热系数为 H, 传热面积为 A, 未加温前炉内温度为 $T_{0}$ , 加温后的温度为 $T_{1}$ , 单位时间内电热丝产生的热量为 $Q_{i}$ , 则根据热力学知识, 有

$$M C \frac {\mathrm{d} (T _ {1} - T _ {0})}{\mathrm{d} t} + H A (T _ {1} - T _ {0}) = Q _ {i}$$

由于 $Q_{i}$ 与外加电压 $\pmb{u}$ 的平方成比例，故 $Q_{i}$ 与 $\pmb{u}$ 呈非线性关系，可在平衡点 $(Q_0,u_0)$ 附近进行线性化，得 $K_{u} = \Delta Q_{i}/$ $\Delta u$ ，于是可得电加热炉的增量微分方程

$$T \frac {\mathrm{d} \Delta T}{\mathrm{d} t} + \Delta T = K \Delta u \tag {2-58}$$

式中， $\Delta T=T_{1}-T_{0}$ 为温度差；T=MC/HA 为电加热炉时间常数； $K=K_{u}/HA$ 为电加热炉传递系数。

在零初始条件下,对式(2-58)两端进行拉氏变换,可得炉内温度变化量对控制电压变化量之间的电加热炉传递函数

$$G (s) = \frac {\Delta T (s)}{\Delta U (s)} = \frac {K}{T s + 1} \tag {2-59}$$

有纯延迟的单容水槽 在图 2-18 单容水槽中, 若调节阀 1 距贮水槽 2 有一段较长的距离, 则调节阀开度变化所引起的流入量变化 $\Delta Q_{i}$ , 需要经过一段传输时间 $\tau$ 才能对水槽液位产生影响, 其中 $\tau$ 通常称为纯延迟时间。

参照式(2-56)的推导过程,可得有纯延迟单容水槽的微分方程为

$$T \frac {\mathrm{d} \Delta h}{\mathrm{d} t} + \Delta h = K \Delta u (t - \tau) \tag {2-60}$$

在零初始条件下，对式(2-60)两端进行拉氏变换，即得到有纯延迟单容水槽的传递函数

$$G (s) = \frac {\Delta H (s)}{\Delta U (s)} = \frac {K}{T s + 1} \mathrm{e} ^ {- v s} \tag {2-61}$$

该式与单容水槽传递函数[式(2-57)]相比，多了一个延迟因子 $e^{-\alpha}$ 。

双容水槽 图 2-20 是两个串联单容水槽构成的双容水槽。其输入量为调节阀 1 产生的阀门开度变化 $\Delta u$ ，而输出量为第二个水槽的液位增量 $\Delta h_{2}$ 。

![](image/db989a99a727de796dac0ea34180432eea7c622504ae6ec1d9b9c1679a2f8ad7.jpg)

<details>
<summary>text_image</summary>

Q₁+ΔQ₁
h₁₀+Δh₁
Q₁₀+ΔQ₁
h₂₀+Δh₂
Q₂₀+ΔQ₂
</details>

图 2-20 双容水槽

在水流量增量、水槽液位增量及液阻之间，经平衡点线性化后，可以导出如下关系式：
