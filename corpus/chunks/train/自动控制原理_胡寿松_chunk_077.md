# (1) 定义

线性定常系统的传递函数,定义为零初始条件下,系统输出量的拉氏变换与输入量的拉氏变换之比。

设线性定常系统由下述 $n$ 阶线性常微分方程描述：

$$
\begin{array}{l} a _ {0} \frac {\mathrm{d} ^ {n}}{\mathrm{d} t ^ {n}} c (t) + a _ {1} \frac {\mathrm{d} ^ {n - 1}}{\mathrm{d} t ^ {n - 1}} c (t) + \dots + a _ {n - 1} \frac {\mathrm{d}}{\mathrm{d} t} c (t) + a _ {n} c (t) \\ = b _ {0} \frac {\mathrm{d} ^ {m}}{\mathrm{d} t ^ {m}} r (t) + b _ {1} \frac {\mathrm{d} ^ {m - 1}}{\mathrm{d} t ^ {m - 1}} r (t) + \dots + b _ {m - 1} \frac {\mathrm{d}}{\mathrm{d} t} r (t) + b _ {m} r (t) \tag {2-36} \\ \end{array}
$$

式中， $c(t)$ 是系统输出量； $r(t)$ 是系统输入量； $a_{i}(i=1,2,\cdots,n)$ 和 $b_{j}(j=1,2,\cdots,m)$ 是与系统结构和参数有关的常系数。设 $r(t)$ 和 $c(t)$ 及其各阶导数在t=0时的值均为零，即零初始条件，则对上式中各项分别求拉氏变换，并令 $C(s) = \mathcal{L}[c(t)], R(s) = \mathcal{L}[r(t)]$ ，可得 $s$ 的代数方程为

$$\left[ a _ {0} s ^ {n} + a _ {1} s ^ {n - 1} + \dots + a _ {n - 1} s + a _ {n} \right] C (s) = \left[ b _ {0} s ^ {m} + b _ {1} s ^ {m - 1} + \dots + b _ {m - 1} s + b _ {m} \right] R (s)$$

于是，由定义得系统传递函数

$$G (s) = \frac {C (s)}{R (s)} = \frac {b _ {0} s ^ {m} + b _ {1} s ^ {m - 1} + \cdots + b _ {m - 1} s + b _ {m}}{a _ {0} s ^ {n} + a _ {1} s ^ {n - 1} + \cdots + a _ {n - 1} s + a _ {n}} = \frac {M (s)}{N (s)} \tag {2-37}$$

式中 $M(s)=b_{0}s^{m}+b_{1}s^{m-1}+\cdots+b_{m-1}s+b_{m}$

$$N (s) = a _ {0} s ^ {n} + a _ {1} s ^ {n - 1} + \dots + a _ {n - 1} s + a _ {n}$$

例 2-8 试求例 2-1 RLC 无源网络的传递函数 $U_{o}(s)/U_{i}(s)$ 。

解 RLC 网络的微分方程用式(2-1)表示为

$$L C \frac {\mathrm{d} ^ {2} u _ {o} (t)}{\mathrm{d} t ^ {2}} + R C \frac {\mathrm{d} u _ {o} (t)}{\mathrm{d} t} + u _ {o} (t) = u _ {i} (t)$$

在零初始条件下，对上述方程中各项求拉氏变换，并令 $U_{o}(s) = \mathcal{L}[u_{o}(t)], U_{i}(s) = \mathcal{L}[u_{i}(t)]$ ，可得 $s$ 的代数方程为 $(LCs^2 + RCs + 1)U_o(s) = U_i(s)$ ，由传递函数定义，网络传递函数为

$$G (s) = \frac {U _ {o} (s)}{U _ {i} (s)} = \frac {1}{L C s ^ {2} + R C s + 1} \tag {2-38}$$
