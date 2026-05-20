$$
\boldsymbol {S} _ {c} = \left[ \begin{array}{l l l} \boldsymbol {b} & \boldsymbol {A b} & \boldsymbol {A} ^ {2} \boldsymbol {b} \end{array} \right] = \left[ \begin{array}{l l l} 1 & 0 & 0 \\ 0 & 1 & - 6 \\ 0 & 0 & 1 \end{array} \right]
\operatorname{rank} \mathbf {S} _ {c} = 3 = n
$$

系统可控，满足极点可配置条件。系统的特征多项式为

$$
\det (s \boldsymbol {I} - \boldsymbol {A}) = \det \left[ \begin{array}{c c c} s & 0 & 0 \\ - 1 & s + 6 & 0 \\ 0 & - 1 & s + 1 2 \end{array} \right] = s ^ {3} + 1 8 s ^ {2} + 7 2 s
$$

希望特征多项式为

$$
\begin{array}{l} a _ {0} ^ {*} (s) = (s - \lambda_ {1}) (s - \lambda_ {2}) (s - \lambda_ {3}) = (s + 2) (s + 1 - j) (s + 1 + j) \\ = s ^ {3} + 4 s ^ {2} + 6 s + 4 \\ \end{array}
$$

于是可求得

$$\bar {\boldsymbol {k}} = \left[ a _ {0} ^ {*} - a _ {0} \quad a _ {1} ^ {*} - a _ {1} \quad a _ {2} ^ {*} - a _ {2} \right] = \left[ 4 - 6 6 - 1 4 \right]$$

变换矩阵为

$$
\boldsymbol {P} ^ {- 1} = \left[ \begin{array}{l l l} \boldsymbol {A} ^ {2} \boldsymbol {b} & \boldsymbol {A b} & \boldsymbol {b} \end{array} \right] \left[ \begin{array}{l l l} 1 & 0 & 0 \\ a _ {2} & 1 & 0 \\ a _ {1} & a _ {2} & 1 \end{array} \right] = \left[ \begin{array}{l l l} 0 & 0 & 1 \\ - 6 & 1 & 0 \\ 1 & 0 & 0 \end{array} \right] \left[ \begin{array}{l l l} 1 & 0 & 0 \\ 1 8 & 1 & 0 \\ 7 2 & 1 8 & 1 \end{array} \right] = \left[ \begin{array}{l l l} 7 2 & 1 8 & 1 \\ 1 2 & 1 & 0 \\ 1 & 0 & 0 \end{array} \right]

\boldsymbol {P} = \left[ \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 1 & - 1 2 \\ 1 & - 1 8 & 1 4 4 \end{array} \right]

\pmb {k} = \bar {\pmb {k}} \pmb {P} = \left[ \begin{array}{l l l} 4 & - 6 6 & - 1 4 \end{array} \right] \left[ \begin{array}{c c c} 0 & 0 & 1 \\ 0 & 1 & - 1 2 \\ 1 & - 1 8 & 1 4 4 \end{array} \right] = \left[ \begin{array}{l l l} - 1 4 & 1 8 6 & - 1 2 2 0 \end{array} \right]
$$

或令

$$
a _ {0} ^ {*} (s) = \det (s I - A + b k)
\begin{array}{l} = \left[ \begin{array}{c c c} s + k _ {1} & k _ {2} & k _ {3} \\ - 1 & s + 6 & 0 \\ 0 & - 1 & s + 1 2 \end{array} \right] \\ = s ^ {3} + \left(k _ {1} + 1 8\right) s ^ {2} + \left(1 8 k _ {1} + k _ {2} + 7 2\right) s + \left(7 2 k _ {1} + 1 2 k _ {2} + k _ {3}\right) \\ \end{array}
$$

于是有

$$k _ {1} + 1 8 = 41 8 k _ {1} + k _ {2} + 7 2 = 67 2 k _ {1} + 1 2 k _ {2} + k _ {3} = 4$$

可求得

$$
k _ {1} = - 1 4, \quad k _ {2} = 1 8 6, \quad k _ {3} = - 1 2 2 0
\boldsymbol {k} = \left[ \begin{array}{l l l} k _ {1} & k _ {2} & k _ {3} \end{array} \right] = \left[ \begin{array}{l l l} - 1 4 & 1 8 6 & - 1 2 2 0 \end{array} \right]
$$
