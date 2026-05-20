作为误差的测度, 当 $\varepsilon$ 为 0.01, 0.05 和 0.1 时, 求出 $E_{0}$ 分别为 0.0112, 0.0589 和 0.1192。这些数据说明当 $\varepsilon \leqslant 0.1$ 时, 误差由 $1.2\varepsilon$ 界定。图 10.1(a) 给出了 $\varepsilon = 0.1$ 时状态向量第一分量的精确轨迹和近似轨迹。由例 10.2 可知 $x_{11}$ 和 $x_{21}$ 满足方程

$$\dot {x} _ {1 1} = x _ {2 1}, \quad x _ {1 1} (0) = 0\dot {x} _ {2 1} = - x _ {1 1} - (1 - \cos^ {2} t) \sin t, x _ {2 1} (0) = 0$$

其解为 $x_{11}(t) = -\frac{9}{32}\sin t - \frac{1}{32}\sin 3t + \frac{3}{8} t\cos t$

$$x _ {2 1} (t) = \frac {3}{3 2} \cos t - \frac {3}{3 2} \cos 3 t - \frac {3}{8} t \sin t$$

由定理10.1可知，二阶逼近 $x_0(t) + \varepsilon x_1(t)$ 为 $O(\varepsilon^2)$ ，当 $\varepsilon$ 足够小时接近精确解。为了比较 $\varepsilon = 0.1$ 时的近似解和精确解，计算出

![](image/bd072c7ab9c93cf7c0fbc9b42126c55204b880e8a32f4e0b355272fe2ff85e7f.jpg)

<details>
<summary>line</summary>

| x | Solid Line | Dashed Line |
| --- | --- | --- |
| 0.0 | 1.0 | 1.0 |
| 0.5 | 0.75 | 0.75 |
| 1.0 | 0.5 | 0.5 |
| 1.5 | 0.25 | 0.25 |
| 2.0 | 0.0 | 0.0 |
| 2.5 | -0.25 | -0.25 |
| 3.0 | -0.5 | -0.5 |
</details>

(a) $x_{1}(t,\varepsilon)$ (实线)和 $x_{10}(t)$ (虚线)

![](image/eec9afaf77ce48fe053a3a3175d6706d54ee7b79395a13ba04e958be7d5c10b1.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0.0 | 0.0000 |
| 0.5 | -0.0050 |
| 1.0 | -0.0250 |
| 1.5 | -0.0500 |
| 2.0 | -0.0750 |
| 2.5 | -0.1000 |
| 3.0 | -0.1200 |
</details>

(b) $x_{1}(t,\varepsilon) - x_{10}(t)$ （实线）和 $x_{1}(t,\varepsilon) - x_{10}(t) - \varepsilon x_{11}(t)$ （虚线）  
图10.1 例10.3在 $\varepsilon = 0.1$ 时的情况

$$E _ {1} = \max _ {0 \leqslant t \leqslant \pi} \| x (t, 0. 1) - x _ {0} (t) - 0. 1 x _ {1} (t) \| _ {2} = 0. 0 0 5 7$$

说明逼近误差几乎降低了一个数量级。图10.1(b)给出了当 $\varepsilon = 0.1$ 时，一阶逼近 $x_0$ 和二阶逼近 $x_0 + \varepsilon x_1$ 的状态向量第一分量的逼近误差。

例10.4 图10.2所示电路含有非线性电阻，其 $I - V$ 特性由 $i = \psi (v)$ 给出。关于电容两端电压的微分方程为

$$C \frac {d v _ {1}}{d t} = \frac {1}{R} (E - v _ {1}) - \psi (v _ {1}) - \frac {1}{R _ {c}} (v _ {1} - v _ {2})C \frac {d v _ {2}}{d t} = \frac {1}{R} (E - v _ {2}) - \psi (v _ {2}) - \frac {1}{R _ {c}} (v _ {2} - v _ {1})$$
