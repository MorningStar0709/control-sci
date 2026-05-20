(4) 求解结果为 $N(s)D^{-1}(s) = Q(s) + R(s)D^{-1}(s)$ ，其中 $R(s)D^{-1}(s)$ 为非真 $N(s)D^{-1}(s)$ 的严格真部分。

例 给定非真 $N(s)D^{-1}(s)$ ，其中

$$
N (s) = \left[ (s + 1) ^ {2} (s + 2) - (s + 2) ^ {2} \right]
D (s) = \left[ \begin{array}{c c} (s + 2) (s + 1) & (s + 1) \\ (s + 2) & (s + 1) \end{array} \right]
$$

现先求出 $N(s)D^{-1}(s)$ 的有理分式矩阵表达式 $G(s)$ 为：

$$G (s) = \left[ \frac {s ^ {3} + 4 s ^ {2} + 7 s + 5}{s ^ {2} + s} - \frac {2 s ^ {2} + 6 s + 5}{s} \right]$$

运用多项式除法,可把上式进而表为:

$$
\begin{array}{l} G (s) = \left[ (s + 3) + \frac {4 s + 5}{s ^ {2} + s} - (2 s + 6) - \frac {5}{s} \right] \\ = [ (s + 3) - (2 s + 6) ] + \left[ \frac {4 s + 5}{s ^ {2} + s} - \frac {5}{s} \right] \\ = Q (s) + G _ {s p} (s) \\ \end{array}
$$

由此，即可求出

$$
\begin{array}{l} Q (s) = [ (s + 3) - (2 s + 6) ] \\ R (s) = G _ {i p} (s) D (s) = \left[ \frac {4 s + 5}{s ^ {2} + s} - \frac {5}{s} \right] \left[ \begin{array}{c c} (s + 2) (s + 1) & (s + 1) \\ (s + 2) & (s + 1) \end{array} \right] \\ = [ 4 s + 8 - 1 ] \\ \end{array}
$$

于是，就求得 $N(s)D^{-1}(s)$ 的严格真部分为：

$$
R (s) D ^ {- 1} (s) = [ 4 s + 8 - 1 ] \left[ \begin{array}{c c} (s + 2) (s + 1) & (s + 1) \\ (s + 2) & (s + 1) \end{array} \right] ^ {- 1}
$$

此外，还需指出，如果给定的非真 $N(s)D^{-1}(s)$ 中 $D(s)$ 是列既约的，则还可采用其他的算法来计算 $R(s)D^{-1}(s)$ 和 $Q(s)$ 。

一种特殊情况 下面，我们来讨论 $D(s)=(sI-A)$ 的特殊情况，其中 A 为 p 维常数矩阵。不难看出，这种情况下， $D(s)$ 必为非奇异，且有 $\delta_{ei}D(s)=\delta_{ri}D(s)=1, i=1,2,\cdots,p$ 。并且，相应地有如下的结论。

结论 令 $D(s) = sI - A$ ， $A$ 为 $p \times p$ 常数矩阵。再令 $N(s)$ 为任意 $q \times p$ 的多项式矩阵，且可表为

$$N (s) = N _ {2} s ^ {*} + \dots + N _ {1} s + N _ {0} \tag {7.48}$$

其中， $n = \max(\delta_{e}iN(s), j = 1, \cdots, p)$ ， $N_{i}(j = 1, \cdots, p)$ 为 $q \times p$ 的常数矩阵。定义

$$N _ {r} (A) = N _ {n} A ^ {*} + \dots + N _ {1} A + N _ {0} I \tag {7.49}N _ {l} (A) = A ^ {n} N _ {s} + \dots + A N _ {1} + I N _ {0} \tag {7.50}$$

则存在唯一的多项式矩阵 $Q_{r}(s)$ 和 $Q_{I}(s)$ ，使成立

$$N (s) = Q _ {r} (s) (s I - A) + N _ {r} (A) \tag {7.51}$$

和

$$N (s) = (s I - A) Q _ {l} (s) + N _ {l} (A) \tag {7.52}$$

其中， $N_{r}(A)$ 和 $N_{l}(A)$ 为常阵，且 $Q_{r}(s)$ 和 $Q_{l}(s)$ 分别可求出为：

$$
\begin{array}{l} Q _ {s} (s) = N _ {n} s ^ {n - 1} + \left(N _ {n} A + N _ {n - 1}\right) s ^ {n - 1} + \dots \\ + \left(N _ {n} A ^ {n - 1} + N _ {n - 1} A ^ {n - 2} + \dots + N _ {1}\right) \tag {7.53} \\ \end{array}
$$

和

$$
\begin{array}{l} Q _ {l} (s) = N _ {n} s ^ {n - 1} + \left(A N _ {n} + N _ {n - 1}\right) s ^ {n - 1} + \dots \\ + \left(A ^ {n - 1} N _ {a} + A ^ {n - 2} N _ {n - 1} + \dots + N _ {1}\right) \tag {7.54} \\ \end{array}
$$

证 利用(7.48)、(7.49)和(7.53)可直接检验关系式(7.51)成立,而利用(7.48)、(7.50)和(7.54)则可直接确定关系式(7.52)成立。于是结论得证。
