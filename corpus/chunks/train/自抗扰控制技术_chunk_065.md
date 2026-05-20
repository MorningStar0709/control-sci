例2 线性系统 $y = w(s) = \frac{r^4}{(s + r)^4} v$ 的状态变量实现为

$$
\begin{array}{l} f = - r \left(r \left(r \left(r \left(x _ {1} - v\right) + 4 x _ {2}\right) + 6 x _ {3}\right) + 4 x _ {4}\right) \\ \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = x _ {3} \\ \dot {x} _ {3} = x _ {4} \\ \dot {x} _ {4} = f \end{array} \tag {2.3.26}
$$

离散化成

$$
\left\{ \begin{array}{l} f = - r \left(r \left(r \left(r \left(x _ {1} - v\right) + 4 x _ {2}\right) + 6 x _ {3}\right) + 4 x _ {4}\right) \\ x _ {1} = x _ {1} + h x _ {2} \\ x _ {2} = x _ {2} + h x _ {3} \\ x _ {3} = x _ {3} + h x _ {4} \\ x _ {4} = x _ {4} + h f \end{array} \right. \tag {2.3.27}
$$

参数 r 适当大时就有 $x_{1}(t) \rightarrow v(t)$ , $x_{2}(t) \rightarrow \frac{\mathrm{d}v}{\mathrm{d}t}$ , $x_{3}(t) \rightarrow \frac{\mathrm{d}^{2}v}{\mathrm{d}t^{2}}$ , $f(t) \rightarrow \frac{\mathrm{d}^{3}v}{\mathrm{d}t^{2}}$ . 采样步长取 h = 0.01, 输入函数取 $v(t) = \sin(t)$ , 参数取 r = 30 时的仿真结果如图 2.3.8 所示, 各阶导数逼近的很好. 这说明, 在一些情况下, 高阶线性跟踪微分器也具有很好的微分功能.

![](image/bd06f89393e78cc6cc6375e27e8c09dc249b4bb5bf0a9ed83a89329e53421d96.jpg)

<details>
<summary>line</summary>

| t | f(t) | x(t) |
| --- | --- | --- |
| 1 | -0.5 | 0.5 |
| 2 | 0.5 | -0.5 |
| 3 | 0.0 | 0.0 |
| 4 | -0.5 | 0.5 |
| 5 | -0.5 | -0.5 |
| 6 | 0.0 | 0.0 |
| 7 | 0.5 | -0.5 |
| 8 | 0.0 | 0.5 |
| 9 | -0.5 | -0.5 |
| 10 | -0.5 | 0.0 |
</details>

图2.3.8
