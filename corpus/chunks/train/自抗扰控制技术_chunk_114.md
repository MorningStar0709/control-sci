$$
\left\{ \begin{array}{l} d = r h ^ {2}, a _ {0} = h x _ {2}, y = x _ {1} + a _ {0} \\ a _ {1} = \sqrt {d (d + 8 | y |)} \\ a _ {2} = a _ {0} + \operatorname{sign} (y) \left(a _ {1} - d\right) / 2 \\ a = \left\{ \begin{array}{c} a _ {0} + y, | y | \leqslant d \\ a _ {2}, | y | > d \end{array} \right. \\ \text {fhan} = - r \left\{ \begin{array}{l} \frac {a}{d}, | a | \leqslant d \\ \operatorname{sign} (a), | a | > d \end{array} \right. \end{array} \right. \tag {3.3.27}
$$

利用符号函数去掉条件语句并把步长 h 改成独立于步长的另一参

数 $h_{1}$ ，得

$$
\operatorname{fhan} \left(x _ {1}, x _ {2}, r, h _ {1}\right):
\left\{ \begin{array}{l} d = r t _ {1} ^ {2}, a _ {0} = h _ {1} x _ {2}, y = x _ {1} + a _ {0} \\ a _ {1} = \sqrt {d (d + 8 | y |)} \\ a _ {2} = a _ {0} + \operatorname{sign} (y) \left(a _ {1} - d\right) / 2 \\ s _ {y} = (\operatorname{sign} (y + d) - \operatorname{sign} (y - d)) / 2 \\ a = \left(a _ {0} + y - a _ {2}\right) s _ {y} + a _ {2} \\ s _ {a} = (\operatorname{sign} (a + d) - \operatorname{sign} (a - d)) / 2 \\ \text {fhan} = - r \left(\frac {a}{d} - \operatorname{sign} (a)\right) s _ {a} - r \operatorname{sign} (a) \end{array} \right. \tag {3.3.28}
$$

这个反馈函数, 当 $h_{1}=h$ 时成为上述离散系统的最速反馈控制. 应用此函数时, 一般取 $h_{1}>h$ . 在这个函数中有两个参数 $r, h_{1}$ , 可以把它表示成

$$\operatorname{fhan} \left(x _ {1}, x _ {2}, r, h _ {1}\right) = u \left(x _ {1}, x _ {2}\right)$$

参数 r 称为控制量增益, 而把参数 $h_{1}$ 称为快速因子. 这个离散形式的最速反馈控制用于上述例子的仿真结果如图 3.3.6 所示. 在这

![](image/37223e20d0b9d390c85d0454c74513fae6633af407945ebf2435b50a50d936b1.jpg)

<details>
<summary>line</summary>

| x | w |
| --- | --- |
| 0 | 0.8 |
| 5 | -1.0 |
| 10 | 0.8 |
| 15 | -1.0 |
| 20 | 0.8 |
</details>

![](image/8cc75e88f85781fc51b02f0b4f7b600c72d4be74391fb19d20178dd4ba98b238.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 0.0 |
| 5 | 0.8 |
| 10 | 0.0 |
| 15 | 0.8 |
| 20 | 0.0 |
</details>

图3.3.6

里稳态的高频振荡完全被克服了,这就是离散最速反馈函数的优越性. 最速反馈函数和线性饱和函数都具有函数值取 $(-r, +r)$ 中间值的线性区域, 但两个函数确定的这个线性区域的几何形状是完全不同的, 前者的线性区域离原点越远越宽, 但后者却离原点越远越窄. 这种几何差异示于图3.3.7.

![](image/e4d028ecb4c2e573b34ecba6948cae735484932d09982b0034d844dc2e2560d0.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| -2 | 1.8 |
| -1 | 1.0 |
| 0 | 0.0 |
| 1 | -1.0 |
| 2 | -1.5 |
</details>

等高线 $\mathrm{fst}(x_1,x_2,r_0,h_1)$

![](image/98f048db73c4c19247915225f1018d26215c1de0498113fafcc3611bdba49394.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| -2 | 2.0 |
| -1 | 1.0 |
| 0 | 0.0 |
| 1 | -1.0 |
| 2 | -2.0 |
</details>

等高线 $\mathrm{sat}(s_{1},\delta)$   
图 3.3.7
