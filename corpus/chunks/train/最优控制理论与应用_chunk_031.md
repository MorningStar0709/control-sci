$$
\det \left[ \begin{array}{c c c c} f _ {x _ {1} x _ {1}} ^ {\prime \prime} & f _ {x _ {1} x _ {2}} ^ {\prime \prime} & \dots & f _ {x _ {1} x _ {k}} ^ {\prime \prime} \\ f _ {x _ {2} x _ {1}} ^ {\prime \prime} & f _ {x _ {2} x _ {2}} ^ {\prime \prime} & \dots & f _ {x _ {2} x _ {k}} ^ {\prime \prime} \\ & \dots \dots & & \\ f _ {x _ {k} x _ {1}} ^ {\prime \prime} & f _ {x _ {k} x _ {2}} ^ {\prime \prime} & \dots & f _ {x _ {k} x _ {k}} ^ {\prime \prime} \end{array} \right] _ {X = X ^ {*}} > 0 \quad k = 1, 2, \dots , n \tag {2-12}
$$

则 $f''_{X}$ 就是正定的。det $\pmb{A}$ 表示 $\pmb{A}$ 阵的行列式的值。

例2-2 求下面的多元函数的极值点

$$f \left(x _ {1}, x _ {2}, x _ {3}\right) = 2 x _ {1} ^ {2} + 5 x _ {2} ^ {2} + x _ {3} ^ {2} + 2 x _ {2} x _ {3} + 2 x _ {3} x _ {1} - 6 x _ {2} + 3$$

解

$$f _ {x _ {1}} ^ {\prime} = \frac {\partial f}{\partial x _ {1}} = 4 x _ {1} + 2 x _ {3} = 0f _ {x _ {2}} ^ {\prime} = \frac {\partial f}{\partial x _ {2}} = 1 0 x _ {2} + 2 x _ {3} - 6 = 0f _ {x _ {3}} ^ {\prime} = \frac {\partial f}{\partial x _ {3}} = 2 x _ {1} + 2 x _ {2} + 2 x _ {3} = 0$$

由上面三个方程,求得可能的极值点为

$$\boldsymbol {X} ^ {*} = \left[ x _ {1} ^ {*}, x _ {2} ^ {*}, x _ {3} ^ {*} \right] ^ {\mathrm{T}} = [ 1, 1, - 2 ] ^ {\mathrm{T}}$$

二阶导数阵为

$$
f _ {x ^ {*}} ^ {\prime \prime} = \left[ \begin{array}{c c c} 4 & 0 & 2 \\ 0 & 1 0 & 2 \\ 2 & 2 & 2 \end{array} \right]
$$

用西尔维斯特判据来检验,有

$$
4 > 0 \quad \det \left[ \begin{array}{l l} 4 & 0 \\ 0 & 1 0 \end{array} \right] = 4 0 > 0 \quad \det \left[ \begin{array}{l l l} 4 & 0 & 2 \\ 0 & 1 0 & 2 \\ 2 & 2 & 2 \end{array} \right] = 2 4 > 0
$$

故 $f''_{X}$ 为正定，在 $X^{*}=[1,1,-2]^{T}$ 处， $f(X^{*})$ 为极小。
