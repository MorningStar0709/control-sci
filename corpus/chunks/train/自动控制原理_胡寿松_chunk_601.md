$$
\begin{array}{l} y ^ {(n)} + a _ {n - 1} y ^ {(n - 1)} + a _ {n - 2} y ^ {(n - 2)} + \dots + a _ {1} \dot {y} + a _ {0} y \\ = b _ {n} u ^ {(n)} + b _ {n - 1} u ^ {(n - 1)} + \dots + b _ {1} \dot {u} + b _ {0} u \tag {9-8} \\ \end{array}
$$

一般输入导数项的次数小于或等于系统的阶数 $n$ 。首先研究 $b_{n} \neq 0$ 时的情况。为了避免在状态方程中出现输入导数项，可按如下规则选择一组状态变量，设

$$
\left. \begin{array}{l} x _ {1} = y - h _ {0} u \\ x _ {i} = \dot {x} _ {i - 1} - h _ {i - 1} u; \quad i = 2, 3, \dots , n \end{array} \right\} \tag {9-9}
$$

其展开式为

$$
\left. \begin{array}{l} x _ {1} = y - h _ {0} u \\ x _ {2} = \dot {x} _ {1} - h _ {1} u = \dot {y} - h _ {0} \dot {u} - h _ {1} u \\ x _ {3} = \dot {x} _ {2} - h _ {2} u = \ddot {y} - h _ {0} \ddot {u} - h _ {1} \dot {u} - h _ {2} u \\ \vdots \\ x _ {n - 1} = \dot {x} _ {n - 2} - h _ {n - 2} u = y ^ {(n - 2)} - h _ {0} u ^ {(n - 2)} - h _ {1} \dot {u} ^ {(n - 3)} - \dots - h _ {n - 2} u \\ x _ {n} = \dot {x} _ {n - 1} - h _ {n - 1} u = y ^ {(n - 1)} - h _ {0} u ^ {(n - 1)} - h _ {1} u ^ {(n - 2)} - \dots - h _ {n - 1} u \end{array} \right\} \tag {9-10}
$$

式中， $h_{0}, h_{1}, h_{2}, \cdots, h_{n-1}$ 是 n 个待定常数。由式(9-10)的第一个方程可得输出方程

$$y = x _ {1} + h _ {0} u$$

其余可得 $n - 1$ 个状态方程

$$
\begin{array}{l} \dot {x} _ {1} = x _ {2} + h _ {1} u \\ \dot {x} _ {2} = x _ {3} + h _ {2} u \\ \begin{array}{c} \bullet \\ \vdots \\ \bullet \end{array} \\ \dot {x} _ {n - 1} = x _ {n} + h _ {n - 1} u \\ \end{array}
$$

对 $x_{n}$ 求导数并考虑式(9-8)，有

$$
\begin{array}{l} \dot {x} _ {n} = y ^ {(n)} - h _ {0} u ^ {(n)} - h _ {1} u ^ {(n - 1)} - \dots - h _ {n - 1} \dot {u} = (- a _ {n - 1} y ^ {(n - 1)} - a _ {n - 2} y ^ {(n - 2)} \\ - \dots - a _ {1} \dot {y} - a _ {0} y + b _ {0} u ^ {(n)} + \dots + b _ {1} \dot {u} + b _ {0} u) - h _ {0} u ^ {(n)} - h _ {1} u ^ {(n - 1)} \\ - \dots - h _ {n - 1} \dot {u} \\ \end{array}
$$

由式(9-10)将 $y^{(n-1)},\cdots,\dot{y},y$ 均以 $x_{i}$ 及 u 的各阶导数表示，经整理可得

$$\dot {x} _ {n} = - a _ {0} x _ {1} - a _ {1} x _ {2} - \dots - a _ {n - 2} x _ {n - 1} - a _ {n - 1} x _ {n} + (b _ {n} - h _ {0}) u ^ {(n)}+ \left(b _ {n - 1} - h _ {1} - a _ {n - 1} h _ {0}\right) u ^ {(n - 1)} + \left(b _ {n - 2} - h _ {2} - a _ {n - 1} h _ {1} - a _ {n - 2} h _ {0}\right) u ^ {(n - 2)}+ \dots + \left(b _ {1} - h _ {n - 1} - a _ {n - 1} h _ {n - 2} - a _ {n - 2} h _ {n - 3} - \dots - a _ {1} h _ {0}\right) \dot {u}+ \left(b _ {0} - a _ {n - 1} h _ {n - 1} - a _ {n - 2} h _ {n - 2} - \dots - a _ {1} h _ {1} - a _ {0} h _ {0}\right) u$$

令上式中 u 的各阶导数项的系数为零, 可确定各 h 值

$$h _ {0} = b _ {n}h _ {1} = b _ {n - 1} - a _ {n - 1} h _ {0}h _ {2} = b _ {n - 2} - a _ {n - 1} h _ {1} - a _ {n - 2} h _ {0}$$

•
•
•

$$h _ {n - 1} = b _ {1} - a _ {n - 1} h _ {n - 2} - a _ {n - 2} h _ {n - 3} - \dots - a _ {1} h _ {0}$$

记 $h_{n}=b_{0}-a_{n-1}h_{n-1}-a_{n-2}h_{n-2}-\cdots-a_{1}h_{1}-a_{0}h_{0}$ ，故

$$\dot {x} _ {n} = - a _ {0} x _ {1} - a _ {1} x _ {2} - \dots - a _ {n - 2} x _ {n - 1} - a _ {n - 1} x _ {n} + h _ {n} u$$
