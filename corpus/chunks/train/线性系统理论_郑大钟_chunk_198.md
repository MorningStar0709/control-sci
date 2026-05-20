$$
\begin{array}{l} \left[ \begin{array}{l} \dot {\boldsymbol {x}} \\ \dot {x} _ {c} \end{array} \right] = \left[ \begin{array}{l l} A & 0 \\ - \boldsymbol {b} _ {c} \boldsymbol {c c} & A _ {c c} \end{array} \right] \left[ \begin{array}{l} \boldsymbol {x} \\ x _ {c c} \end{array} \right] + \left[ \begin{array}{l} \boldsymbol {b} \\ 0 \end{array} \right] u + \left[ \begin{array}{l} \boldsymbol {b} _ {w} \\ 0 \end{array} \right] w + \left[ \begin{array}{l} 0 \\ \boldsymbol {b} _ {c c} \end{array} \right] y _ {0} \\ = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & - 1 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 1 1 & 0 & 0 \\ - 1 & 0 & 0 & 0 & 0 \end{array} \right] \left[ \begin{array}{l} x \\ x _ {c} \end{array} \right] + \left[ \begin{array}{c} 0 \\ 1 \\ 0 \\ - 1 \\ 0 \end{array} \right] u + \left[ \begin{array}{l} 0 \\ 4 \\ 0 \\ 6 \\ - 0 \end{array} \right] w + \left[ \begin{array}{l} 0 \\ 0 \\ 0 \\ 0 \\ - 1 \end{array} \right] y _ {0} \\ \end{array}
$$

由受控系统满足结论1的条件可知，此系统为能控，故可任意配置极点。根据镇定要求，不妨取期望的闭环极点为：

$$\lambda_ {1} ^ {*} = - 1, \lambda_ {2} ^ {*} = - 1, \lambda_ {3, 4} ^ {*} = - 1 \pm j, \lambda_ {5} ^ {*} = - 2$$

从而可定出

$$
\begin{array}{l} \alpha^ {*} (s) = (s + 1) ^ {2} (s + 1 - j) (s + 1 + j) (s + 2) \\ = s ^ {5} + 6 s ^ {4} + 1 5 s ^ {3} + 2 0 s ^ {2} + 1 4 s + 4 \\ \end{array}
$$

进而,取状态反馈控制律为:

$$
u = \left[ - k _ {1} - k _ {2} - k _ {3} - k _ {4} \mid k _ {c} \right] \left[ \begin{array}{l} x \\ x _ {c} \end{array} \right] = [ - k \mid k _ {c} ] \left[ \begin{array}{l} x \\ x _ {c} \end{array} \right]
$$

可得增广系统的闭环矩阵为：

$$
\overline {{A}} = \left[ \begin{array}{c c} A - b k & b k _ {c} \\ - b _ {c} c & A _ {c} \end{array} \right] = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & 0 & 0 \\ - k _ {1} & - k _ {2} & - k _ {3} - 1 & - k _ {4} & k _ {c} \\ 0 & 0 & 0 & 1 & 0 \\ k _ {1} & k _ {2} & 1 1 + k _ {3} & k _ {4} & - k _ {c} \\ - 1 & 0 & 0 & 0 & 0 \end{array} \right]
$$

而其特征多项式为：

$$\alpha (s) = \det (s I - \bar {A}) = s ^ {5} + \left(k _ {2} - k _ {4}\right) s ^ {4} + \left(k _ {1} - k _ {3} - 1 1\right) s ^ {3}\left(k _ {c} - 1 0 k _ {2}\right) s ^ {2} - 1 0 k _ {1} s - 1 0 k _ {c}$$

于是，由使 $\alpha^{*}(s)$ 和 $\alpha(s)$ 的各对应系数相等，即可定出：

$$k _ {c} = - 0. 4, \quad k _ {1} = - 1. 4, \quad k _ {2} = - 2. 0 4k _ {3} = - 2 7. 4, \quad k _ {4} = - 8. 0 4$$

从而，得到

$$\boldsymbol {k} = [ - 1. 4, - 2. 0 4, - 2 7. 4, - 8. 0 4 ]k _ {c} = - 0. 4$$

(4) 定出伺服补偿器和镇定补偿器

对给定受控系统,使其实现无静差跟踪的伺服补偿器和镇定补偿器分别为:

$$\dot {x} _ {c} = [ 0 ] x _ {c} + [ 1 ] e = eu _ {1} = k _ {c} x _ {c} = - 0. 4 x _ {c}$$

和

$$u _ {2} = k x = [ - 1. 4, - 2. 0 4, - 2 7. 4, - 8. 0 4 ] x$$

而控制律

$$u = u _ {1} - u _ {2} = - 0. 4 x _ {c} + [ 1. 4, 2. 0 4, 2 7. 4, 8. 0 4 ] x$$
