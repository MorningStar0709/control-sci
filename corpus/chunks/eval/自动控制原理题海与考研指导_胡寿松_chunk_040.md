# 3. 拉普拉斯反变换

求拉普拉斯反变换的简单方法是利用拉普拉斯变换表。如果某个变换式 $F(s)$ 在表中不能找到，那么可以把 $F(s)$ 展成部分分式，写成 $s$ 的简单函数形式，再去查表。

应当指出,这种寻求拉普拉斯反变换的简单方法基于如下事实:对于任何连续的时间函数,它与其拉普拉斯变换之间保持唯一的对应关系。

一般,象函数 $F(s)$ 是复变量 s 的有理代数分式,可以表示如下:

$$F (s) = \frac {B (s)}{A (s)} = \frac {b _ {0} s ^ {m} + b _ {1} s ^ {m - 1} + \cdots + b _ {m - 1} s + b _ {m}}{s ^ {n} + a _ {1} s ^ {n - 1} + \cdots + a _ {n - 1} s + a _ {n}}$$

式中，系数 $a_{1}, a_{2}, \cdots, a_{n}$ 和 $b_{0}, b_{1}, b_{2}, \cdots, b_{m}$ 都是实常数；m 和 n 为正整数，通常 m < n。

为了把 $F(s)$ 展成部分分式, 需要对 $A(s)$ 进行因式分解, 得到

$$F (s) = \frac {B (s)}{A (s)} = \frac {b _ {0} s ^ {m} + b _ {1} s ^ {m - 1} + \cdots + b _ {m - 1} s + b _ {m}}{(s - s _ {1}) (s - s _ {2}) \cdots (s - s _ {n})}$$

式中， $s_{i}(i=1,2,\cdots,n)$ 称为 $F(s)$ 的极点。

1) $F(s)$ 无重极点

$$F (s) = \sum_ {i = 1} ^ {n} \frac {c _ {i}}{s - s _ {i}}$$

式中， $c_{i}$ 为待定常数，称为 $F(s)$ 在极点 $s_i$ 处的留数，可按下式计算：

$$c _ {i} = \lim _ {s \rightarrow s _ {i}} (s - s _ {i}) F (s)$$

于是，可方便求得原函数

$$f (t) = \mathcal {L} ^ {- 1} [ F (s) ] = \sum_ {i = 1} ^ {n} c _ {i} \mathrm{e} ^ {s _ {i} t}$$

上式表明,有理代数分式函数的拉普拉斯反变换,可表示为若干指数项之和。

2) $F(s)$ 有多重极点

设 $A(s) = 0$ 有 $r$ 个重根 $s_1$ ，则 $F(s)$ 可写为

$$
\begin{array}{l} F (s) = \frac {B (s)}{(s - s _ {1}) ^ {r} (s - s _ {r + 1}) \cdots (s - s _ {n})} \\ = \frac {c _ {r}}{(s - s _ {1}) ^ {r}} + \frac {c _ {r - 1}}{(s - s _ {1}) ^ {r - 1}} + \dots + \frac {c _ {1}}{s - s _ {1}} + \frac {c _ {r + 1}}{s - s _ {r + 1}} + \dots + \frac {c _ {n}}{s - s _ {n}} \\ \end{array}
$$

式中，待定常数 $c_{r+1}, \cdots, c_{n}$ 按 $F(s)$ 无重极点时的留数计算

$$c _ {i} = \lim _ {s \rightarrow s _ {i}} (s - s _ {i}) F (s); \quad i = r + 1, r + 2, \dots , n$$

而重极点对应的待定常数 $c_{r}, c_{r-1}, \cdots, c_{1}$ ，则按下式确定：

$$
\begin{array}{l} c _ {r} = \lim _ {s \rightarrow s _ {1}} (s - s _ {1}) ^ {r} F (s) \\ c _ {r - 1} = \lim _ {s \rightarrow s _ {1}} \frac {\mathrm{d}}{\mathrm{d} s} \left[ (s - s _ {1}) ^ {r} F (s) \right] \\ c _ {r - j} = \frac {1}{j !} \lim _ {s \rightarrow s _ {1}} \frac {\mathrm{d} ^ {(j)}}{\mathrm{d} s ^ {j}} [ (s - s _ {1}) ^ {r} F (s) ] \\ \end{array}
$$

•
•
•

$$c _ {1} = \frac {1}{(r - 1) !} \lim _ {s \rightarrow s _ {1}} \frac {\mathrm{d} ^ {(r - 1)}}{\mathrm{d} s ^ {r - 1}} [ (s - s _ {1}) ^ {r} F (s) ]$$

从而，原函数

$$f (t) = \mathscr {L} ^ {- 1} [ F (s) ] = \left[ \frac {c _ {r}}{(r - 1) !} t ^ {r - 1} + \frac {c _ {r - 1}}{(r - 2) !} t ^ {r - 2} + \dots + c _ {2} t + c _ {1} \right] e ^ {s _ {1} t} + \sum_ {i = r + 1} ^ {n} c _ {i} e ^ {s _ {i} t}$$
