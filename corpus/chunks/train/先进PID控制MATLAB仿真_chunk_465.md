# 10.5.2 一个简单的样条插值实例

三次样条插值（简称 Spline 插值）是通过一系列形值点的一条光滑曲线，数学上通过

求解三弯矩方程组得出曲线函数组的过程。

定义：设 $[a,b]$ 上有插值点， $a=x_{1}<x_{2}<\cdots<x_{n}=b$ ，对应的函数值为 $y_{1},y_{2},\cdots,y_{n}$ 。若函数 $S(x)$ 满足 $S(x_{j})=y_{j}(j=1,2,\cdots,n)$ 上都是不高于三次的多项式，当 $S(x)$ 在 $[a,b]$ 上具有二阶连续导数，则称 $S(x)$ 为三次样条插值函数，如图10-10所示。

要求 $S(x)$ 只需在 $[x_j, x_{j+1}]$ 上确定1个三次多项式，设为

$$S _ {j} (x) = a _ {j} x ^ {3} + b _ {j} x ^ {2} + c _ {j} x + d _ {j} (j = 1, 2, \dots , n - 1)$$

式中， $a_{j}, b_{j}, c_{j}, d_{j}$ 待定，并满足

$$S \left(x _ {j}\right) = y _ {j}, \quad S \left(x _ {j} - 0\right) = S \left(x _ {j} + 0\right),(j = 1, 2, \dots , n - 1)S ^ {\prime} \left(x _ {j} - 0\right) = S ^ {\prime} \left(x _ {j} + 0\right), \quad S ^ {\prime \prime} \left(x _ {j} - 0\right) = S ^ {\prime \prime} \left(x _ {j} + 0\right),(j = 1, 2, \dots , n - 1)$$

![](image/14b649a4787774676ba4dfce98a5d012db8ee6cfb86735c0847cfcc1cbef01f1.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| x₁ | y₁ |
| x₂ | y₂ |
| x₃ | y₃ |
| ... | ... |
| xₙ₋₁ | yₙ₋₁ |
| xₙ | yₙ |
</details>

图 10-10 三次样条插值函数

以一个简单的三次样条插值为例，横坐标取 0 至 10 且间隔为 1 的 11 个插值点，纵坐标取正弦函数，以横坐标间距为 0.25 的点形成插值曲线，利用 MATLAB 提供的插值函数 spline 可实现三次样条插值，仿真结果如图 10-11 所示。

![](image/984d077673c29dc966c60c49c7f6adab23a76f076d3574f2620c2f623978e274.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 0.0 |
| 1 | 0.85 |
| 2 | 0.95 |
| 3 | 0.15 |
| 4 | -0.75 |
| 5 | -0.95 |
| 6 | -0.25 |
| 7 | 0.65 |
| 8 | 1.0 |
| 9 | 0.4 |
| 10 | -0.55 |
</details>

图 10-11 插值效果

【仿真实例】 chap10\_5.m

```matlab
clearall;
closeall
x = 0:10;
y = sin(x);
xx = 0:0.25:10;
yy = spline(x,y,xx);
plot(x,y,'o',xx,yy,'k','linewidth',2); 
```

![](image/26e2b34e982fe7f3df899d4fd7ce15e0240cd0054b955668ccf7d73ba4cb2115.jpg)
