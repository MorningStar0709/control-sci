# 7) 脉动函数

考虑下列脉动函数：

$$
f (t) = \left\{ \begin{array}{l l} \frac {A}{t _ {0}}, & 0 <   t <   t _ {0} \\ 0, & t <   0, \quad t _ {0} <   t \end{array} \right.
$$

式中， $A$ 和 $t_0$ 为常数。由于

$$f (t) = \frac {A}{t _ {0}} 1 (t) - \frac {A}{t _ {0}} 1 (t - t _ {0})$$

故脉动函数的拉普拉斯变换

$$F (s) = \mathscr {L} \left[ \frac {A}{t _ {0}} 1 (t) \right] - \mathscr {L} \left[ \frac {A}{t _ {0}} 1 (t - t _ {0}) \right] = \frac {A}{t _ {0} s} (1 - e ^ {- s t _ {0}})$$
