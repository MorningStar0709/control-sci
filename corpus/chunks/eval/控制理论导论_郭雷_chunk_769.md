# Hilbert 空间中守恒系统的镇定

现在我们考虑如下线性控制系统：

$$\frac {\mathrm{d} x (t)}{\mathrm{d} t} = A x (t) + B u (t), \tag {10.3.14}$$

其中 $A$ 是Hilbert空间 $H$ 中的斜自伴算子，即 $A^{*} = -A$ ，而 $B$ 是从另一个Hilbert空间 $U$ (控制空间)到 $H$ 的有界线性算子．这一类系统可以由弹性振动和波方程导出，称为守恒系统．注意系统(10.3.14)的能量是 $E(t) = \frac{1}{2}\| x(t)\|^2$ ，其中 $x(t)$ 是方程(10.3.14)的解．当输入 $\pmb{u}$ 为零时，能量 $E(t)$ 与 $\pmb{t}$ 无关，即能量是守恒的

$$
\begin{array}{l} \frac {\mathrm{d} E (t)}{\mathrm{d} t} = \frac {1}{2} \left[ (A x (t), x (t)) + (x (t), A x (t)) \right] \\ = \frac {1}{2} \left[ (A x (t), x (t)) + (- A x (t), x (t)) \right] = 0. \\ \end{array}
$$

本小节结果参阅文献 [28]. 首先我们证明一个引理.

引理10.3.2 设 $A$ 和 $-A$ 均生成Hilbert空间上的 $C_0$ 半群, 并且 $B \in \mathcal{L}(U, H)$ , $U$ 为另一个Hilbert空间. 如果 $(A, B)$ 和 $(-A, B)$ 都是指数能稳的, 则 $(A, B)$ 在某个有穷区间 $[0, t_f]$ 上是精确能控的.

证明 注意在引理条件下， $A$ 生成一 $C_0$ 群，于是为证 $(A,B)$ 的指数能稳性，根据定理5.2.1，只需证明 $(A,B)$ 在某个区间 $[0,t_f]$ 上是精确零能控的。今 $(A,B)$ 和 $(-A,B)$ 均是指数能稳的，故存在 $K_{1},K_{2}\in \mathcal{L}(H,U)$ 和 $t_f > 0$ 使得

$$\| J \| < 1, \qquad \text {其中} J = T ^ {- A + B K _ {2}} (t _ {f}) T ^ {A + B K _ {1}} (t _ {f}).$$

因此 $(I - J)^{-1} \in \mathcal{L}(H)$ . 对于任意 $x_0 \in H$ , 令

$$
\left\{ \begin{array}{l} v _ {1} (t) = T ^ {A + B K _ {1}} (t) (I - J) ^ {- 1} x _ {0}, \\ v _ {2} (t) = T ^ {A - B K _ {2}} (t) x _ {0}, \\ v _ {3} (t) = T ^ {A - B K _ {2}} (t) (I - J) ^ {- 1} x _ {0}. \end{array} \right.
$$

于是根据 $C_0$ 半群的扰动公式 (5.3.25), 有

$$
\begin{array}{l} x (t) \stackrel {\text { def }} {=} v _ {1} (t) + v _ {2} (t) - v _ {3} (t) \\ = T ^ {A} (t) x _ {0} + \int_ {0} ^ {t} T ^ {A} (t - s) B \left[ K _ {1} v _ {1} (s) - K _ {2} v _ {2} (s) + K _ {2} v _ {3} (s) \right] d s, \\ \end{array}
$$

并且 $x(0) = x_0, x(t_f) = 0$ . 这表明连续控制

$$u (t) = K _ {1} v _ {1} (t) - K _ {2} v _ {2} (t) + K _ {2} v _ {3} (t)$$

把初始状态 $x_0$ 带到 $t_f$ 时刻的零状态。证毕。

推论10.3.3 设 $\Lambda$ 生成 $C_0$ 西群，即 $A^{*} = -A$ ，并设 $B \in \mathcal{L}(U, H)$ 。如果存在对称算子 $K \in \mathcal{L}(U)$ 使得 $T^{A + BKB^*}(t)$ 是指数稳定的，则 $(A, B)$ 在某个区间 $[0, t_f]$ 上是精确能控的，并且（例如）把初始状态 $x_0$ 带到 $t_f$ 时刻零状态的控制可以选为

$$u (t) = K B ^ {*} \left(v _ {1} (t) + v _ {2} (t) - v _ {3} (t)\right),$$

其中

$$
\left\{ \begin{array}{l} v _ {1} (t) = T ^ {A + B K B ^ {*}} (t) (I - J) ^ {- 1} x _ {0}, \\ v _ {2} (t) = T ^ {A - B K B ^ {*}} (t) x _ {0}, \\ v _ {3} (t) = T ^ {A - B K B ^ {*}} (t) (I - J) ^ {- 1} x _ {0}, \end{array} \right.
J = T ^ {- A + B K B ^ {*}} \left(t _ {f}\right) T ^ {A + B K B ^ {*}} \left(t _ {f}\right), \quad \| J \| < 1.
$$

证明 在引理10.3.2的证明中，取 $K_{1} = K_{2} = KB^{*}$ ，则有

$$T ^ {- A + B K B ^ {*}} (t) = \left[ T ^ {A + B K B ^ {*}} (t) \right] ^ {*}$$
