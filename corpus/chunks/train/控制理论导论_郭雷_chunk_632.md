等式 (8.4.51), 式 (8.4.52) 保证了式 (8.4.50) 有形式为式 (8.4.53) 的平行分解.

下面我们考虑级联解耦. 设 $u$ 的分割及 $F_{i}$ 的定义如前. 令 $J_{i}$ 为包含 $\{F_{s} \mid s \leqslant i\}$ 的 $\mathcal{F}$ 的最小理想, 即

$$J _ {i} = \left\{F _ {s} \mid s \leqslant i \right\} _ {I}, \quad i = 1, \dots , k.$$

注意，这里 $J_{k} = \mathcal{F}_{0}$

根据推广的 Frobenius 定理，利用证明定理 8.4.6 的相同的方法可证明以下结果.

定理 8.4.7 系统 (8.4.42) 在 $x_{0}$ 的级联解耦可解，当且仅当存在 u 的一个分割，使得嵌套的理想 $J_{1}, \cdots, J_{k}$ 在 $x_{0}$ 非奇异.

解决无反馈平行式级联分解问题的关键是找到理想 $I_{i}, I_{i}$ 可由以下算法得到：

$$
\left\{ \begin{array}{l} E _ {0} ^ {i} = F _ {i} \\ E _ {s + 1} ^ {i} = E _ {s} ^ {i} + \operatorname{span} \left\{\mathrm{ad} _ {f} E _ {s} ^ {i} \mid f \in F \right\}, \quad s \geqslant 0. \end{array} \right. \tag {8.4.54}
$$

显见若存在 $k^{*}$ 使得 $E_{k^{*}}^{i} = E_{k^{*} + 1}^{i}$ ，则 $I_{i} = E_{k^{*}}^{i}$ .

例8.4.3 考虑下列系统在 $z_0 = 0$ 的平行解耦：

$$
\left[ \begin{array}{c} \dot {z} _ {1} \\ \dot {z} _ {2} \\ \dot {z} _ {3} \\ \dot {z} _ {4} \end{array} \right] = \left[ \begin{array}{c} \sin (z _ {2} + z _ {4} + u _ {2}) \\ \frac {1}{2} u _ {1} u _ {2} \mathrm{e} ^ {z _ {1}} + \frac {1}{2} (z _ {3} + 1 - \mathrm{e} ^ {z _ {1}}) \\ \mathrm{e} ^ {z _ {1}} \sin (z _ {2} + z _ {4} + u _ {2}) + u _ {3} (z _ {2} - z _ {4} + 1) \\ \frac {1}{2} u _ {1} u _ {2} \mathrm{e} ^ {z _ {1}} - \frac {1}{2} (z _ {3} + 1 - \mathrm{e} ^ {z _ {1}}) \end{array} \right].
$$

先算 $I_{i}, i = 1,2,3$ . 我们有

$$
F _ {1} = \left\{\left. \left[ \begin{array}{c} 0 \\ \frac {1}{2} (u _ {1} ^ {\prime} - u _ {1}) u _ {2} \mathrm{e} ^ {z _ {1}} \\ 0 \\ \frac {1}{2} (u _ {1} ^ {\prime} - u _ {1}) u _ {2} \mathrm{e} ^ {z _ {1}} \end{array} \right] \right| u _ {1} ^ {\prime}, u _ {1}, u _ {2} = \text {const} \right\}
$$

于是

$$
\begin{array}{l} E _ {0} ^ {1} = \operatorname{span} \left\{\left[ 0, 1, 0, 1 \right] ^ {\mathrm{T}} \right\} \\ E _ {1} ^ {1} = \operatorname{span} \left\{\left[ 0, 1, 0, 1 \right] ^ {\mathrm{T}} \right\} + \operatorname{span} \left\{\operatorname{ad} _ {f} e _ {0} ^ {1} \right\} \\ = \operatorname{span} \left\{\left[ 0, 1, 0, 1 \right] ^ {\mathbf {T}}, \left[ 1, 0, e ^ {z _ {1}}, 0 \right] ^ {\mathbf {T}} \right\}. \\ \end{array}
$$

因为

$$\operatorname{ad} _ {f} ([ 1, 0, \mathrm{e} ^ {z _ {1}}, 0 ] ^ {\mathrm{T}}) = \frac {1}{2} [ u _ {1} u _ {2} \mathrm{e} ^ {z _ {1}}, 0, u _ {1} u _ {2} \mathrm{e} ^ {z _ {1}}, 0 ] ^ {\mathrm{T}} \in E _ {1} ^ {1},$$

故

$$E _ {2} ^ {1} = E _ {1} ^ {1} = I _ {1}.$$

类似地，可算 $I_{2}$ 和 $I_{3}$

由于 $F_{2} \in I_{1}$ , 故

$$I _ {2} \subset I _ {1}.$$

由此可算得 $I_{3}$
