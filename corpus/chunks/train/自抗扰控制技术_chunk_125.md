![](image/d0e1fb2aae756f61b9635737d2d836b9b6db322e46cac907eb2464edd81e1496.jpg)

<details>
<summary>line</summary>

| x | s≥0 | s≤0 | s≤0 | s≤0 |
| --- | --- | --- | --- | --- |
| -25 | 4.0 | 3.0 | 0.0 | 0.0 |
| -20 | 3.5 | 2.5 | 0.0 | 0.0 |
| -15 | 3.0 | 2.0 | 0.0 | 0.0 |
| -10 | 2.5 | 1.5 | 0.0 | 0.0 |
| -5 | 2.0 | 1.0 | 0.0 | 0.0 |
| 0 | 1.5 | 0.5 | 0.0 | 0.0 |
| 5 | 1.0 | 0.0 | 0.0 | 0.0 |
| 10 | 0.5 | -0.5 | -0.5 | -0.5 |
| 15 | 0.0 | -1.0 | -1.0 | -1.0 |
| 20 | -0.5 | -1.5 | -1.5 | -1.5 |
| 25 | -1.0 | -2.0 | -2.0 | -2.0 |
</details>

图3.5.5

于是四个式子统一地表达成

$$t = s \frac {x _ {2}}{r _ {1}} + a \sqrt {s _ {1} \left(x _ {1} + s \frac {x _ {2} ^ {2}}{2 r _ {1}}\right)} \tag {3.5.33}$$

这个函数的曲面表现和等高线分别如图3.5.6和图3.5.7所示.

![](image/7b21bd00f31509ebdb3e7a98f2fe02a0155303676eac780bd8143d22e36cc01a.jpg)

<details>
<summary>surface_3d</summary>

| x | y |
| --- | --- |
| -5 | 9 |
| -3 | 6 |
| -1 | 4 |
| 1 | 2 |
| 3 | 0 |
</details>

图3.5.6  
![](image/56cd0aa4584ced54211fd812b43e649cf3926cae57c010877521c66dcb07d834.jpg)

<details>
<summary>contour</summary>

| x | y |
| --- | --- |
| -3 | 2 |
| -2 | 1 |
| -1 | 0 |
| 0 | -1 |
| 1 | -2 |
| 2 | -3 |
| 3 | -4 |
</details>

图3.5.7

由于 $t = s \frac{x_{2}}{r_{1}} + a \sqrt{s_{1} \left( x_{1} + s \frac{x_{2}^{2}}{2r_{1}} \right)}$ 是沿系统轨线到达原点的时间，只能是正定函数，而它沿系统轨线的导数 $\frac{\mathrm{d}t(x_{1}, x_{2})}{\mathrm{d}t} = \frac{\partial t(x_{1}, x_{2})}{\partial x_{1}} x_{1} + \frac{\partial t(x_{1}, x_{2})}{\partial x_{2}} x_{2}$ 为常值 -1. 实际上，

$$\frac {\partial t \left(x _ {1} , x _ {2}\right)}{\partial x _ {1}} = \frac {a s _ {1}}{2 \sqrt {s _ {1} \left(x _ {1} + s \frac {x _ {2} ^ {2}}{2 r _ {1}}\right)}},\frac {\partial t \left(x _ {1} , x _ {2}\right)}{\partial x _ {2}} = \frac {s}{r _ {1}} + \frac {x _ {2}}{r _ {1}} \frac {a s _ {1} s}{2 \sqrt {s _ {1} \left(x _ {1} + s \frac {x _ {2} ^ {2}}{2 r _ {1}}\right)}}$$

而闭环系统方程为

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = - r _ {1} \operatorname{sign} \left(x _ {1} + \frac {x _ {2} | x _ {2} |}{2 r}\right) = - r _ {1} s \end{array} \right.
$$

因此计算 $\frac{\mathrm{d}t(x_1,x_2)}{\mathrm{d}t}$ 就得
