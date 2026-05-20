# 例 9.2 球悬浮器运动的线性化

图 9.1 所示的为一个应用于大型涡轮机械的磁力轴承。磁铁是用反馈控制的方法来激励的，以保证转轴总是处于中心位置且不会触碰磁极，从而几乎不存在摩擦力的影响。图 9.2 所示的为一个可在实验室搭建的磁力轴承简化版，用一块电磁石将金属球悬浮起来。悬浮装置的物理结构如图 9.3 所示。利用牛顿定律式(2.1)，导出球的运动方程为

$$m \ddot {x} = f _ {\mathrm{m}} (x, i) - m g \tag {9.5}$$

![](image/e53b1d9ff7b2875dfeaafb68a6a8a1afa1f627602d2d034b21698b4e0a5656c1.jpg)

<details>
<summary>natural_image</summary>

Close-up of a mechanical component with flanged ends and bolt holes (no visible text or symbols)
</details>

图 9.1 磁力轴承  
(图片来源：magnetic bearings 公司)

![](image/c651e87a9a11013938a99a52749df0082bdcad6f69ed6af0bf8667dbb0527125.jpg)

<details>
<summary>natural_image</summary>

Mechanical testing apparatus with a vertical chamber and base, no visible text or symbols
</details>

图 9.2 用在实验室的磁力浮球装置  
(图片来源：Gene Franklin)

其中：力 $f_{\mathrm{m}}(x, i)$ 是由电磁铁的磁场产生的。理论上，电磁铁产生的磁力与小球到电磁铁的距离平方成反比，但是实验所用悬浮器的准确关系很难用物理机理获得，这是因为磁场非常复杂。不过，这些力可以用仪器来测量。图9.4所示的为直径为 $1\mathrm{cm}$ ，质量为 $8.4\times 10^{-3}\mathrm{kg}$ 的小球的实验曲线。对图中所示电流 $i_2 = 600\mathrm{mA}$ 和位移为 $x_{1}$ 的情况，磁力 $f_{\mathrm{m}}$ 刚好抵消重力， $mg = 82\times 10^{-3}\mathrm{N}$ （球的质量为 $8.4\times 10^{-3}\mathrm{kg}$ ，重力加速度为 $9.8\mathrm{m / s^2}$ ）。因此，点 $(x_1, i_2)$ 代表一个平衡点。使用这个数据，找到此平衡点处运动的线性化方程组。

![](image/bab5978e8798666903d1453b23140ba339a0d3869ca79553ee67b6814325617c.jpg)

<details>
<summary>text_image</summary>

i
x
</details>

图 9.3 浮球装置模型

![](image/796ef536c8f71313687afa8d58b01e00ffdea85260da02fa7772dd498a5318da.jpg)

<details>
<summary>line</summary>

| 距离, x/mm | 作用力f_m (10^-3 N) for i₁=700 mA | 作用力f_m (10^-3 N) for i₂=600 mA | 作用力f_m (10^-3 N) for i₃=500 mA |
| --- | --- | --- | --- |
| 1 | ~90 | ~40 | ~20 |
| 2 | ~110 | ~60 | ~30 |
| x₁ | ~80 | ~80 | ~80 |
| 3 | ~120 | ~100 | ~60 |
| 4 | ~140 | ~120 | ~80 |
| 5 | ~160 | ~140 | ~100 |
| 6 | ~180 | ~160 | ~120 |
</details>

图 9.4 通过实验确定的磁力曲线

解答。首先我们写出力相对于平衡点 $x_{1}$ 和 $i_2$ 的展开形式为

$$f _ {\mathrm{m}} (x _ {1} + \delta x, i _ {2} + \delta i) \approx f _ {\mathrm{m}} (x _ {1}, i _ {2}) + K _ {x} \delta x + K _ {i} \delta i \tag {9.6}$$

找到线性增益如下： $K_{x}$ 是图9.4中曲线 $i=i_{2}$ 上力相对于 x 的斜率，大约为 14N/m。对于固定值 $x=x_{1}$ ， $K_{i}$ 是力随着电流的变化值。我们发现在 $x=x_{1}$ 处，对于 $i=i_{1}=700mA$ ，力大约为 $122\times10^{-3}N$ ，在 $x=x_{1}$ 处，对于 $i=i_{3}=500mA$ ，力大约为 $42\times10^{-3}N$ 。因此
