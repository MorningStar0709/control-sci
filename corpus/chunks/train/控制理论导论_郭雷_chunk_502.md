$$\Delta_ {\varepsilon , \bar {t}} J _ {1} [ u ] = - \int_ {\bar {t}} ^ {\bar {t} + \varepsilon} \frac {\partial [ H (x ^ {*} (t) , \bar {u} , \psi (t)) - H (x ^ {*} (t) , u ^ {*} (t) , \psi (t)) ]}{\partial x} \Delta_ {\varepsilon , \bar {t}} x (t) d t- \int_ {\bar {t}} ^ {\bar {t} + \varepsilon} [ H (x ^ {*} (t), \bar {u}, \psi (t)) - H (x ^ {*} (t), u ^ {*} (t), \psi (t)) ] d t+ \int_ {t _ {0}} ^ {t _ {f}} o (| \Delta_ {\varepsilon , \bar {t}} x (t) |) d t + o (| \Delta_ {\varepsilon , \bar {t}} x (t _ {f}) |). \tag {7.1.41}$$

命题7.1.1 设 $\phi(t)$ 为定义在区间 $[t_1, t_2]$ 上的连续可微 $n$ 维向量值函数，则

$$\frac {\mathrm{d}}{\mathrm{d} t} | \phi (t) | \leqslant \left| \frac {\mathrm{d}}{\mathrm{d} t} \dot {\phi} (t) \right|, \quad \forall t \in [ t _ {1}, t _ {2} ], \phi (t) \neq 0.$$

下面估计 $\Delta_{\varepsilon, \bar{t}} x(t)$ 和 $\Delta_{\varepsilon, \bar{t}} J_1[u]$ . 将方程 (7.1.39) 右端改写为

$$f (x ^ {*} (t) + \Delta_ {\varepsilon , \bar {t}} x (t), \bar {u}) - f (x ^ {*} (t), u ^ {*} (t))= f (x ^ {*} (t) + \Delta_ {\varepsilon , \bar {t}} x (t), \bar {u}) - f (x ^ {*} (t), \bar {u}) + f (x ^ {*} (t), \bar {u}) - f (x ^ {*} (t), u ^ {*} (t)).$$

利用假设 (7.1.32) 不难得到

$$
\left\{ \begin{array}{l l} | f (x ^ {*} (t), \bar {u}) - f (x ^ {*} (t), u ^ {*} (t)) | \leqslant a, & t \in [ \bar {t}, \bar {t} + \varepsilon ], \\ \big | f (x ^ {*} (t) + \Delta_ {\varepsilon , \bar {t}} x (t), \bar {u}) - f (x ^ {*} (t), \bar {u}) \big | \leqslant b | \Delta_ {\varepsilon , \bar {t}} x (t) |, & t \in [ \bar {t}, \bar {t} + \varepsilon), \\ \big | f (x ^ {*} (t) + \Delta_ {\varepsilon , \bar {t}} x (t), u ^ {*} (t)) - f (x ^ {*} (t), u ^ {*} (t)) \big | \leqslant b | \Delta_ {\varepsilon , \bar {t}} x (t) |, & t \in [ \bar {t} + \varepsilon , t _ {f} ]. \end{array} \right.
$$

由此从微分方程 (7.1.39), (7.1.40) 得到

$$\left| \frac {\mathrm{d}}{\mathrm{d} t} \Delta_ {\varepsilon , \bar {t}} x (t) \right| \leqslant a + b \cdot | \Delta_ {\varepsilon , \bar {t}} x (t) |, \quad t \in [ \bar {t}, \bar {t} + \varepsilon),\left| \frac {\mathrm{d}}{\mathrm{d} t} \Delta_ {\varepsilon , \bar {t}} x (t) \right| \leqslant b \cdot | \Delta_ {\varepsilon , \bar {t}} x (t) |, \quad t \in [ \bar {t} + \varepsilon , t _ {f} ].$$

于是从命题7.1.1可得
