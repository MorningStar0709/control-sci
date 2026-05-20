# (2) $A(s) = 0$ 有重根

设 $A(s) = 0$ 有 $r$ 个重根 $s_1$ ，则 $F(s)$ 可写为

$$
\begin{array}{l} F (s) = \frac {B (s)}{\left(s - s _ {1}\right) ^ {r} \left(s - s _ {r + 1}\right) \cdots \left(s - s _ {n}\right)} \\ = \frac {c _ {r}}{\left(s - s _ {1}\right) ^ {r}} + \frac {c _ {r - 1}}{\left(s - s _ {1}\right) ^ {r - 1}} + \dots + \frac {c _ {1}}{s - s _ {1}} + \frac {c _ {r + 1}}{s - s _ {r + 1}} + \dots + \frac {c _ {n}}{s - s _ {n}} \\ \end{array}
$$

式中， $s_{1}$ 为 $F(s)$ 的重极点， $s_{r+1},\cdots,s_{n}$ 为 $F(s)$ 的 n-r 个非重极点； $c_{r},c_{r-1},\cdots,c_{1},c_{r+1},\cdots,c_{n}$ 为待定常数，其中， $c_{r+1},\cdots,c_{n}$ 按式(A-14)或式(A-15)计算，但 $c_{r},c_{r-1},\cdots,c_{1}$ 应按下式计算：

$$
\begin{array}{l} c _ {r} = \lim _ {s \rightarrow s _ {1}} (s - s _ {1}) ^ {r} F (s) \\ c _ {r - 1} = \lim _ {s \rightarrow s _ {1}} \frac {\mathrm{d}}{\mathrm{d} s} \left[ (s - s _ {1}) ^ {r} F (s) \right] \\ c _ {r - j} = \frac {1}{j !} \lim _ {s \rightarrow s _ {1}} \frac {\mathrm{d} ^ {(j)}}{\mathrm{d} s ^ {j}} [ (s - s _ {1}) ^ {r} F (s) ] \tag {A-17} \\ c _ {1} = \frac {1}{(r - 1) !} \lim _ {s \rightarrow s _ {1}} \frac {\mathrm{d} ^ {(r - 1)}}{\mathrm{d} s ^ {r - 1}} [ (s - s _ {1}) ^ {r} F (s) ] \\ \end{array}
$$

因此，原函数 $f(t)$ 为

$$
\begin{array}{l} f (t) = \mathscr {L} ^ {- 1} [ F (s) ] \\ = \mathscr {L} ^ {- 1} \left[ \frac {c _ {r}}{(s - s _ {1}) ^ {r}} + \frac {c _ {r - 1}}{(s - s _ {1}) ^ {r - 1}} + \dots + \frac {c _ {1}}{s - s _ {1}} + \frac {c _ {r + 1}}{s - s _ {r + 1}} + \dots + \frac {c _ {n}}{s - s _ {n}} \right] \\ = \left[ \frac {c _ {r}}{(r - 1) !} t ^ {r - 1} + \frac {c _ {r - 1}}{(r - 2) !} t ^ {r - 2} + \dots + c _ {2} t + c _ {1} \right] \mathrm{e} ^ {s _ {1} t} + \sum_ {i = r + 1} ^ {n} c _ {i} \mathrm{e} ^ {s _ {i} t} \tag {A-18} \\ \end{array}
$$

例A-7 求 $F(s) = \frac{s + 2}{s(s + 1)^2(s + 3)}$ 的原函数 $f(t)$ 。

解 分母 $A(s) = 0$ 有四个根，即二重根 $s_1 = s_2 = -1; s_3 = 0; s_4 = -3$ 。将 $F(s)$ 展为部分分式，则有

$$F (s) = \frac {s + 2}{s (s + 1) ^ {2} (s + 3)} = \frac {c _ {2}}{(s + 1) ^ {2}} + \frac {c _ {1}}{s + 1} + \frac {c _ {3}}{s} + \frac {c _ {4}}{s + 3}$$

按式(A-17)计算得

$$
\begin{array}{l} c _ {2} = \lim _ {s \rightarrow - 1} \left[ (s + 1) ^ {2} \frac {s + 2}{s (s + 1) ^ {2} (s + 3)} \right] = - \frac {1}{2} \\ c _ {1} = \lim _ {s \rightarrow - 1} \frac {\mathrm{d}}{\mathrm{d} s} \left[ (s + 1) ^ {2} \frac {s + 2}{s (s + 1) ^ {2} (s + 3)} \right] = - \frac {3}{4} \\ \end{array}
$$

按式(A-14)计算得

$$
\begin{array}{l} c _ {3} = \lim _ {s \rightarrow 0} \left[ s \frac {s + 2}{s (s + 1) ^ {2} (s + 3)} \right] = \frac {2}{3} \\ c _ {4} = \lim _ {s \rightarrow - 3} [ (s + 3) \frac {s + 2}{s (s + 1) ^ {2} (s + 3)} ] = \frac {1}{1 2} \\ \end{array}
$$

最后由式(A-18)写出原函数为

$$f (t) = \mathscr {L} ^ {- 1} \left[ \frac {s + 2}{s (s + 1) ^ {2} (s + 3)} \right] = \frac {2}{3} - \frac {1}{2} \mathrm{e} ^ {- t} \left(t + \frac {3}{2}\right) + \frac {1}{1 2} \mathrm{e} ^ {- 3 t}$$
