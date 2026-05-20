# 8.3.3 考虑一个级联系统

$$
\left\{ \begin{array}{l} \dot {x} _ {1} = x _ {2} + \varphi_ {1} (x _ {1}, x _ {2}), \\ \dot {x} _ {2} = x _ {3} + \varphi_ {2} (x _ {1}, x _ {2}, x _ {3}), \\ \vdots \\ \dot {x} _ {n - 1} = x _ {n} + \varphi_ {n - 1} (x), \\ \dot {x} _ {n} = f (x) + g (x) u, \end{array} \right.
$$

这里 $g(x_{0}) \neq 0, \varphi_{1}(x), \varphi_{2}(x), \cdots, \varphi_{n-1}(x)$ 及其一阶导数均在 $x_{0}$ 为零。证明系统在 $x_{0}$ 可线性化。

8.3.4 在原点附近局部线性化下列系统，

$$
\dot {x} = \left[ \begin{array}{c} x _ {2} + x _ {2} ^ {2} \\ x _ {3} - x _ {1} x _ {4} + x _ {4} x _ {5} \\ x _ {2} x _ {4} + x _ {1} x _ {5} - x _ {5} ^ {2} \\ x _ {5} \\ x _ {2} ^ {2} \end{array} \right] + \left[ \begin{array}{c} 0 \\ 0 \\ \cos (x _ {1} - x _ {5}) \\ 0 \\ 0 \end{array} \right] u _ {1} + \left[ \begin{array}{c} 1 \\ 0 \\ 1 \\ 0 \\ 1 \end{array} \right] u _ {2}.
$$
