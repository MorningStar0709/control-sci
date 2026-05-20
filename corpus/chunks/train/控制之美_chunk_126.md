$$X (s) = \left(\frac {K _ {\mathrm{P}} r - \alpha C}{K _ {\mathrm{P}} + 1 0 \alpha}\right) \frac {1}{s} + \left(x _ {0} - \frac {K _ {\mathrm{P}} r - \alpha C}{K _ {\mathrm{P}} + 1 0 \alpha}\right) \frac {1}{s + \frac {K _ {\mathrm{P}} + 1 0 \alpha}{7 0 0 0}} \tag {7.2.4}$$

对式 $(7.2.4)$ 进行拉普拉斯逆变换,得到

$$
\begin{array}{l} x (t) = \mathcal {L} ^ {- 1} [ X (s) ] = \frac {K _ {\mathrm{P}} r - \alpha C}{K _ {\mathrm{P}} + 1 0 \alpha} \mathrm{e} ^ {0 t} + \left(x _ {0} - \frac {K _ {\mathrm{P}} r - \alpha C}{K _ {\mathrm{P}} + 1 0 \alpha}\right) \mathrm{e} ^ {- \frac {K _ {\mathrm{P}} + 1 0 \alpha}{7 0 0 0} t} \\ = \frac {K _ {\mathrm{P}} r - \alpha C}{K _ {\mathrm{P}} + 1 0 \alpha} + \left(x _ {0} - \frac {K _ {\mathrm{P}} r - \alpha C}{K _ {\mathrm{P}} + 1 0 \alpha}\right) \mathrm{e} ^ {- \frac {K _ {\mathrm{P}} + 1 0 \alpha}{7 0 0 0} t} \tag {7.2.5} \\ \end{array}
$$

在式(7.2.5)中, 输出 $x(t)$ 的稳定性与传递函数的极点 $s_{\mathrm{p} 2} = - \frac{K_{\mathrm{P}} + 10\alpha}{7000}$ 相关。在本例中, $K_{\mathrm{P}} > 0$ , 因此 $s_{\mathrm{p} 2} < 0$ 。说明随着时间的增加, $\mathrm{e}^{-\frac{K_{\mathrm{P}} + 10\alpha}{7000} t}$ 项将趋于 0 。因此, 可以通过式(7.2.5)得到系统输出的终值, 即

$$
\begin{array}{l} x (\infty) = \lim _ {t \rightarrow \infty} x (t) = \lim _ {t \rightarrow \infty} \left(\frac {K _ {\mathrm{P}} r - \alpha C}{K _ {\mathrm{P}} + 1 0 \alpha} + \left(x _ {0} - \frac {K _ {\mathrm{P}} r - \alpha C}{K _ {\mathrm{P}} + 1 0 \alpha}\right) \mathrm{e} ^ {- \frac {K _ {\mathrm{P}} + 1 0 \alpha}{7 0 0 0} t}\right) \\ = \frac {K _ {\mathrm{P}} r - \alpha C}{K _ {\mathrm{P}} + 1 0 \alpha} \tag {7.2.6} \\ \end{array}
$$

图 7.2.3(a) 呈现了在不同 $K_{P}$ 下系统输出 $x(t)$ 随时间的变化(其中, 初始体重 $x_{0}=90kg$ , 目标体重 r=65kg, 其余条件参考表 7.1.1 案例 1)。式 (7.2.6) 和图 7.2.3(a) 说明比例增益 $K_{P}$ 越大, 系统的终值 $x(\infty)$ 越接近于参考值 r。图 7.2.3(b) 显示了不同 $K_{P}$ 下的系统控制量 $u(t)$ 随时间的变化。

![](image/4b889b38ae07afa2493fa9943def79e22660a11727f60837689e72fecc50a402.jpg)

<details>
<summary>line</summary>

| t | Kp=200 | Kp=300 | Kp=400 |
| --- | --- | --- | --- |
| 0 | 90 | 90 | 90 |
| 100 | 58 | 60 | 62 |
| 200 | 55 | 58 | 60 |
</details>

(a) 系统输出 $x(t)$ 随时间的变化

![](image/5d44e11c8664ed0605793cd6391a6d26294ce9255e4148aa6e948f1c51774317.jpg)

<details>
<summary>line</summary>

| t | Kp=200 | Kp=300 | Kp=400 |
| --- | --- | --- | --- |
| 0 | -10000 | -7500 | -5000 |
| 100 | 1950 | 1700 | 1600 |
| 200 | 1950 | 1700 | 1600 |
</details>

(b) 系统控制量 $u(t)=K_{\mathrm{P}}e(t)$ 随时间的变化  
图 7.2.3 不同比例增益情况下系统的输出与控制量随时间的变化

系统误差的终值称为稳态误差(Steady State Error)，根据式(7.2.6)，得到
