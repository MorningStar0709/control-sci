并且， $\lim_{t\to \infty}\pmb {x}(t)e^{\alpha t} = 0$ 的要求等价于 $\lim_{t\to \infty}\bar{x} (t) = 0$ 。

对(5.257)所定义的LQ调节问题,我们可给出如下的几点论断:

(1) 当 $\{A, B\}$ 为能控时， $\{A + \alpha I, B\}$ 也必为能控。

很容易证明这一点。利用能控性的秩判据，显然有

$$\operatorname{rank} [ B, (A + \alpha I) B, \dots , (A + \alpha I) ^ {n - 1} B ]= \operatorname{rank} [ B, A B, \dots , A ^ {n - 1} B ] = n \tag {5.258}$$

从而就证明了这个论断。

(2) 对于调节问题 (5.257), 其相应的最优控制 $\bar{u}^{*}(\cdot)$ 具有如下的唯一形式:

$$\bar {\boldsymbol {u}} ^ {*} (t) = - R ^ {- 1} B P \bar {\boldsymbol {x}} ^ {*} (t) \tag {5.259}$$

而最优性能值为

$$J ^ {*} = \boldsymbol {x} _ {0} ^ {T} P \boldsymbol {x} _ {0} \tag {5.260}$$

其中， $P$ 是下述矩阵黎卡提代数方程的正定对称解阵：

$$P (A + \alpha I) + (A + \alpha I) ^ {T} P + Q - P B R ^ {- 1} B ^ {T} P = 0 \tag {5.261}$$

(3) 对于由 (5.259) 的最优控制所构成的状态反馈闭环调节系统

$$\dot {\bar {x}} ^ {*} = (A + \alpha I - B R ^ {- 1} B ^ {T} P) \bar {x} ^ {*}, \quad \bar {x} ^ {*} (0) = x _ {0} \tag {5.262}$$

其零平衡状态是大范围渐近稳定的,即成立

$$\lim _ {t \rightarrow \infty} \bar {\boldsymbol {x}} ^ {*} (t) = \lim _ {t \rightarrow \infty} \boldsymbol {x} ^ {*} (t) e ^ {\alpha t} = 0 \tag {5.263}$$

于是，在上述讨论的基础上，就可直接得到具有指定衰减度的无限时间定常LQ调节问题的最优解的基本结论。

结论2 对于具有指定衰减度的LQ调节问题（5.255）， $u^{*}(\cdot)$ 为其最优控制的充分必要条件是其具有形式：

$$\boldsymbol {u} ^ {*} (t) = - K ^ {*} \boldsymbol {x} ^ {*} (t), \quad K ^ {*} = R ^ {- 1} B ^ {T} P \tag {5.264}$$

最优轨线 $x^{*}(t)$ 为下述状态方程的解:

$$\dot {\boldsymbol {x}} ^ {*} (t) = A \boldsymbol {x} ^ {*} (t) + B \boldsymbol {u} ^ {*} (t), \quad \boldsymbol {x} ^ {*} (0) = \boldsymbol {x} _ {0} \tag {5.265}$$

而最优性能值则为:

$$J ^ {*} = \boldsymbol {x} _ {0} ^ {T} P \boldsymbol {x} _ {0} \tag {5.266}$$

其中， $P$ 为下述矩阵黎卡提代数方程的正定对称解阵：

$$P (A + \alpha I) + (A + \alpha I) P + Q - P B R ^ {- 1} B ^ {T} P = 0 \tag {5.267}$$

最优调节系统的鲁棒性 考察无限时间的定常 LQ 调节问题,已经导出其最优调节系统为:

$$\dot {\boldsymbol {x}} = (A - B K ^ {*}) \boldsymbol {x}, \quad K ^ {*} = R ^ {- 1} B ^ {T} P, t \geqslant 0 \tag {5.268}$$

其中， $P$ 为正定对称阵且满足方程

$$P A + A ^ {T} P + Q - P B R ^ {- 1} B ^ {T} P = 0 \tag {5.269}$$

并且，闭环系统（5.268）必是大范围渐近稳定的，即其特征值均成立

$$\operatorname{Re} \lambda_ {i} (A - B K ^ {*}) < 0, \quad i = 1, 2, \dots , n \tag {5.270}$$

那么,所谓鲁棒性就是指当受控系统的参数或反馈增益阵的参数发生摄动时,闭环调节系统(5.268)仍能保持渐近稳定的一种属性。显然,如果允许的参数摄动越大,则系统的鲁棒性就越好。下面,我们将从频率域的角度,来讨论和给出最优调节系统的鲁棒性的有关结果。

首先,作为鲁棒性分析的基础,我们要引入最优调节系统的频率条件:

结论1 对于最优调节系统(5.268)，其必满足如下的频率条件

$$
\begin{array}{l} [ I + R ^ {1 / 2} K ^ {*} (- j \omega I - A) ^ {- 1} B R ^ {- 1 / 2} ] ^ {T} [ I + R ^ {1 / 2} K ^ {*} (j \omega I - A) ^ {- 1} B R ^ {- 1 / 2} ] \\ \geqslant I \tag {5.271} \\ \end{array}
$$

如果所研究的为单输入定常LQ调节问题，则上述频率条件还可简化表为
