# 习题

3.1 判断下列系统是否为完全能控:

(i) $\dot{x} = \begin{bmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ -2 & -4 & -3 \end{bmatrix} x + \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ -1 & 1 \end{bmatrix} u$

(ii) $\dot{x} = \begin{bmatrix} 0 & 4 & 3 \\ 0 & 20 & 21 \\ 0 & -25 & -20 \end{bmatrix} x + \begin{bmatrix} -1 \\ 3 \\ 0 \end{bmatrix} u$

(iii) $\dot{\pmb{x}} = \begin{bmatrix} 2 & 0 & 0 & 0 \\ 0 & 3 & 0 & 0 \\ 0 & 0 & 4 & 1 \\ 0 & 0 & 0 & 4 \end{bmatrix} \pmb{x} + \begin{bmatrix} 2 & 0 \\ 4 & 1 \\ 0 & 0 \\ 1 & 0 \end{bmatrix} \pmb{u}$

$$
\text {(iv)} \dot {\boldsymbol {x}} = \left[ \begin{array}{l l l l} 4 & 1 & 0 & 0 \\ 0 & 4 & 0 & 0 \\ 0 & 0 & 4 & 1 \\ 0 & 0 & 0 & 4 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l l} 0 & 0 \\ 1 & 2 \\ 0 & 0 \\ 2 & 1 \end{array} \right] \boldsymbol {u}
$$

3.2 确定使下列系统为完全能控时待定参数的取值范围：

$$
\dot {\boldsymbol {x}} = \left[ \begin{array}{c c c} - 2 & 0 & 0 \\ 0 & - 2 & 0 \\ 0 & 0 & - 2 \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l l} a & 1 \\ 2 & 4 \\ b & 1 \end{array} \right] \boldsymbol {u} \tag {i}

\dot {\boldsymbol {x}} = \left[ \begin{array}{l l} 0 & a \\ b & c \end{array} \right] \boldsymbol {x} + \left[ \begin{array}{l} 1 \\ 0 \end{array} \right] \boldsymbol {u} \tag {ii}
$$

3.3 判断下列系统是否为完全能观测：

$$
\dot {x} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - 2 & - 4 & - 3 \end{array} \right] x, \quad y = [ 1 \quad 4 \quad 2 ] x \tag {i}

\dot {\boldsymbol {x}} = \left[ \begin{array}{r r r} - 2 & 1 & 0 \\ 0 & - 2 & 0 \\ 0 & 0 & - 2 \end{array} \right] \boldsymbol {x}, \quad \boldsymbol {y} = \left[ \begin{array}{l l l} 1 & 0 & 4 \\ 2 & 0 & 8 \end{array} \right] \boldsymbol {x} \tag {ii}

\text {(iii)} \quad \dot {\boldsymbol {x}} = \left[ \begin{array}{l l l} 1 & 3 & 2 \\ 1 & 4 & 6 \\ 2 & 1 & 7 \end{array} \right] \boldsymbol {x}, \quad \boldsymbol {y} = \left[ \begin{array}{l l l} 1 & 0 & 0 \\ 2 & 1 & 0 \end{array} \right] \boldsymbol {x}
$$

3.4 确定使下列系统为完全能观测时待定参数的取值范围：

$$
\dot {x} = \left[ \begin{array}{l l} a & b \\ c & 0 \end{array} \right] x, \quad y = [ 1 \quad 0 ] x \tag {i}

\dot {x} = \left[ \begin{array}{c c c} - 2 & 0 & 0 \\ 1 & - 2 & 0 \\ 0 & 0 & - 2 \end{array} \right] x, y = \left[ \begin{array}{c c c} 1 & a & b \\ 4 & 0 & 4 \end{array} \right] x \tag {ii}
$$

3.5 确定使下列系统同时为完全能控和完全能观测时待定参数的取值范围：
