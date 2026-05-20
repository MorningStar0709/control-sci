$$E \int_ {0} ^ {T} \| \xi_ {t} \| ^ {2} \mathrm{d} t < \infty ,$$

则称 $(\xi_t, \mathcal{F}_t) \in \mathcal{M}_T$ 如果

$$P \left(\int_ {0} ^ {T} \| \xi_ {t} \| ^ {2} \mathrm{d} t < \infty\right) = 1,$$

则称 $(\xi_t, \mathcal{F}_t) \in \mathcal{P}_T, T$ 可以有穷或无穷.

设 $\{t_{k}\}$ 是 $[0,T]$ 一个分割， $0=t_{0}<t_{1}<\cdots<t_{n}=T$ ，设 $\xi_{k}$ 为 $F_{t_{k}}$ 可测，那么称

$$\xi_ {t} = \xi_ {0} I _ {[ 0 ]} + \sum_ {k = 0} ^ {n - 1} \xi_ {k} I _ {(t _ {k}, t _ {k + 1} ]}$$

为简单过程.

设 $(w_{t},\mathcal{F}_{t})$ 为Wiener过程．和式(4.3.1)类似地定义随机积分，叫伊滕随机积分，或简称随机积分．首先对简单过程来定义随机积分．对任一 $t\in [0,T]$ 定义

$$\int_ {0} ^ {t} \xi_ {s} \mathrm{d} w _ {t} \stackrel {\text { def }} {=} \sum_ {k = 0} ^ {m} \xi_ {k} (w _ {t _ {k + 1}} - w _ {t _ {k}}) + \xi_ {m + 1} (w _ {t} - w _ {t _ {m + 1}}), \qquad t _ {m + 1} < t \leqslant t _ {m + 2}.$$

对任一 $\xi_t \in \mathcal{M}_T$ , 存在简单过程 $\xi_t^n \in \mathcal{M}_t$ 及不依赖 $\xi_t^n$ 选择的一个随机向量 $\eta$ , 使

$$E \int_ {0} ^ {T} \| \xi_ {t} - \xi_ {t} ^ {n} \| ^ {2} \mathrm{d} t \underset {n \rightarrow \infty} {\longrightarrow} 0,$$

并且

$$\lim _ {n \rightarrow \infty} E \left\| \eta - \int_ {0} ^ {T} \xi_ {t} ^ {n} \mathrm{d} w _ {t} \right\| ^ {2} = 0.$$

那么对 $\xi_t \in \mathcal{M}_T$ 的随机积分的定义为

$$
\begin{array}{l} \int_ {0} ^ {T} \xi_ {t} \mathrm{d} w _ {t} \stackrel {\text { def }} {=} \underset {n \rightarrow \infty} {\text { l.i.m. }} \int_ {0} ^ {T} \xi_ {t} ^ {n} \mathrm{d} w _ {t} \quad (= \eta), \\ \int_ {0} ^ {t} \xi_ {s} \mathrm{d} w _ {s} \stackrel {\text { def }} {=} \int_ {0} ^ {T} I _ {[ 0, t ]} \xi_ {s} \mathrm{d} w _ {s}. \\ \end{array}
$$

进一步，对任一 $\xi_t \in \mathcal{P}_T$ ，存在随机过程列 $\xi_r^n \in \mathcal{M}_T$ ，及不依赖 $\xi_t^n$ 选择的随机变量 $\eta$ ，使

$$\int_ {0} ^ {T} \| \xi_ {t} - \xi_ {t} ^ {n} \| ^ {2} d t \xrightarrow [ n \to \infty ]{P} 0,$$

并且

$$\int_ {0} ^ {T} \xi_ {t} ^ {n} \mathrm{d} w _ {t} \xrightarrow [ n \to \infty ]{P} \eta .$$

这样，对 $\xi_t \in \mathcal{P}_T$ 的随机积分定义为

$$
\begin{array}{l} \int_ {0} ^ {T} \xi_ {t} \mathrm{d} w _ {t} \stackrel {\text { def }} {=} P - \lim _ {n \rightarrow \infty} \int_ {0} ^ {T} \xi_ {t} ^ {n} \mathrm{d} w _ {t} \quad (= \eta), \\ \int_ {0} ^ {t} \xi_ {s} \mathrm{d} w _ {s} \stackrel {\text { def }} {=} \int_ {0} ^ {T} I _ {[ 0, t ]} \xi_ {s} \mathrm{d} w _ {s}. \\ \end{array}
$$

随机积分有如下性质：

i) 设 $a, b$ 为常数， $\xi_s^1, \xi_s^2 \in \mathcal{P}_T$ ，那么

$$\int_ {0} ^ {t} (a \xi_ {s} ^ {1} + b \xi_ {s} ^ {2}) \mathrm{d} w _ {s} = a \int_ {0} ^ {t} \xi_ {s} ^ {1} \mathrm{d} w _ {s} + b \int_ {0} ^ {t} \xi_ {s} ^ {2} \mathrm{d} w _ {s}, \quad \forall t \in [ 0, T ];$$
