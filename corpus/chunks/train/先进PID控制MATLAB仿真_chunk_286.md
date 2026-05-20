$$
\frac {1}{\varepsilon} = R = \left\{ \begin{array}{l l} \mu \frac {1 - \mathrm{e} ^ {- \lambda_ {1} t}}{1 + \mathrm{e} ^ {- \lambda_ {2} t}}, & 0 \leqslant t \leqslant t _ {\max} \\ \mu , t > t _ {\max} \end{array} \right. \tag {5.45}
$$

式中， $\mu$ 、 $\lambda_{1}$ 和 $\lambda_{2}$ 为正实数。

例如，取 $\lambda_{1}=\lambda_{2}=50,\quad\mu=100$ ，运行程序 chap5\_7sim.mdl，R 和 $\varepsilon$ 的变化如图 5-18 所示。

（2）如果实测信号含有噪声，对于非常小的 $\varepsilon$ ，将会产生很大的观测误差。为了防止这种现象，文献 $^{[9]}$ 提出了切换增益 $\varepsilon$ 的设计方法。  
（3） $\alpha_{i}(i=1,2,3)$ 的设计。按 $\overline{A}$ 为Hurwitz进行极点配置，例如，对于 $\lambda^{3}+\alpha_{1}\lambda^{2}+\alpha_{2}\lambda+\alpha_{3}=0$ ，可选择 $(\lambda+1)(\lambda+2)(\lambda+3)=0$ ，则 $\lambda^{3}+6\lambda^{2}+11\lambda+6=0$ ，从而 $\alpha_{1}=6$ ， $\alpha_{2}=11$ ， $\alpha_{3}=6$ 。

![](image/ad16936cce301fd5d5c08a6e1884a85a5d0e302823f0e95372405001bb95adf7.jpg)

<details>
<summary>line</summary>

| time(s) | R change | Epsilon change |
| --- | --- | --- |
| 0.0 | 100 | 0.01 |
| 0.5 | 100 | 0.01 |
| 1.0 | 100 | 0.01 |
| 1.5 | 100 | 0.01 |
| 2.0 | 100 | 0.01 |
| 2.5 | 100 | 0.01 |
| 3.0 | 100 | 0.01 |
| 3.5 | 100 | 0.01 |
| 4.0 | 100 | 0.01 |
| 4.5 | 100 | 0.01 |
| 5.0 | 100 | 0.01 |
</details>

图 5-18 R 和 $\varepsilon$ 的变化

![](image/def6f70e90920eda8cdf446a453d63ce549d8e1237a19266a7a7376b13050381.jpg)
