$$y (0) = h \left(x _ {0}\right), \quad \dot {y} (t) = \sum_ {i = 0} ^ {m} L _ {g _ {i}} h.$$

设

$$y ^ {(k)} (t) = \sum_ {i _ {h}, \dots , i _ {1}} \langle h \rangle ,$$

那么由式 (8.5.23) 可知

$$y ^ {(k + 1)} (t) = \sum_ {i _ {k + 1}, i _ {k}, \dots , i _ {1}} \langle h \rangle .$$

因此

$$y ^ {k} (0) = \sum_ {i _ {k}, \dots , i _ {1} = 0} ^ {m} L _ {g _ {j}} \dots L _ {g _ {i _ {1}}} h (x _ {0}).$$

利用 $y$ 的解析性可知，存在 $T_0 > 0$ ，使得

$$h \left(x _ {0}\right) + \sum_ {k = 1} ^ {\infty} \sum_ {i _ {k}, \dots , i _ {1} = 0} ^ {m} \frac {1}{k !} \left| L _ {g _ {i _ {k}}} \dots L _ {g _ {i _ {1}}} h \left(x _ {0}\right) \right| T _ {0} ^ {k} < \infty . \tag {8.5.29}$$

由 $u_{1},\cdots,u_{m}$ 的连续性可知，对任一给定 $T_{1}>0,$ 存在 N>0, 使得

$$\left| u _ {i} (t) \right| < N, \quad i = 1, \dots , m; 0 \leqslant t \leqslant T _ {1}.$$

不妨设 $N \geqslant 1$ ，于是有

$$\left| \int_ {0} ^ {t} \mathrm{d} \xi_ {i} \right| = \left| \int_ {0} ^ {t} u _ {i} (\tau) \mathrm{d} \tau \right| \leqslant \int_ {0} ^ {t} | u _ {i} (\tau) | \mathrm{d} \tau \leqslant N t.$$

设

$$\left| \int_ {0} ^ {t} \mathrm{d} \xi_ {i _ {k}} \dots \mathrm{d} \xi_ {i _ {1}} \right| \leqslant \frac {1}{k !} N ^ {k} t ^ {k}, \tag {8.5.30}$$

那么

$$\left| \int_ {0} ^ {t} \mathrm{d} \xi_ {i _ {k + 1}} \mathrm{d} \xi_ {i _ {k}} \dots \mathrm{d} \xi_ {i _ {1}} \right| \leqslant \int_ {0} ^ {t} N \frac {1}{k !} N ^ {k} \tau^ {k} \mathrm{d} \tau = \frac {1}{(k + 1) !} N ^ {k + 1} t ^ {k + 1},$$

这证明了式 (8.5.30) 的正确性. 取 $T = \min \left(\frac{T_0}{N}, T_1\right) > 0$ , 则当 $0 \leqslant t \leqslant T$ 时

$$
\begin{array}{l} | z (t) | \leqslant | h \left(x _ {0}\right) | + \sum_ {k = 0} ^ {\infty} \sum_ {i _ {k}, \dots , i _ {0} = 0} ^ {m} \left| L _ {g _ {i _ {k}}} \dots L _ {g _ {i _ {0}}} h \left(x _ {0}\right) \right| \frac {1}{(k + 1) !} \cdot N ^ {k + 1} \cdot \left(\frac {T _ {0}}{N}\right) ^ {k + 1} \\ = | h (x _ {0}) | + \sum_ {k = 1} ^ {\infty} \sum_ {i _ {k}, \dots , i _ {1} = 0} ^ {m} \left| L _ {g _ {i _ {k}}} \dots L _ {g _ {i _ {1}}} h (x _ {0}) \right| \cdot \frac {T _ {0} ^ {k}}{k !} <   \infty . \\ \end{array}
$$

所以 $z(t)$ 在 $[0, T]$ 上一致绝对连续，从而 $z(t)$ 为 $[0, T]$ 上的解析函数.

现在我们证明存在 $T_{s} > 0$ ，使 $z^{(s)}(t)$ 在 $t \in [0, T_{s}]$ 中一致绝对收敛。利用式 (8.5.26)，因为 $p$ 有限，所以只要对 $p$ 个级数分别证明其一致绝对收敛即可。对每个 $p, u_{i_t^p}^{(q_t^p)}$ 在 $0$ 的某个邻域 $[0, T]$ 上一致有界，即存在 $N_0 > 0$ ，使得

$$\left| u _ {i _ {t} ^ {p}} ^ {(q _ {t} ^ {p})} \right| < N _ {0}, \quad t = 1, \dots , s _ {p}; t \in [ 0, T ].$$

因此
