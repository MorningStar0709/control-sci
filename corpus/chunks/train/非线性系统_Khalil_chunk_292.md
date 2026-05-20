$$
\dot {x} _ {1 0} + \varepsilon \dot {x} _ {1 1} + \varepsilon^ {2} \dot {x} _ {1 2} + \varepsilon^ {3} \dot {R} _ {x _ {1}} = x _ {2 0} + \varepsilon x _ {2 1} + \varepsilon^ {2} x _ {2 2} + \varepsilon^ {3} R _ {x _ {2}}
\begin{array}{l} \dot {x} _ {2 0} + \varepsilon \dot {x} _ {2 1} + \varepsilon^ {2} \dot {x} _ {2 2} + \varepsilon^ {3} \dot {R} _ {x _ {2}} = - x _ {1 0} - \varepsilon x _ {1 1} - \varepsilon^ {2} x _ {1 2} - \varepsilon^ {3} R _ {x _ {1}} \\ + \varepsilon [ 1 - (x _ {1 0} + \varepsilon x _ {1 1} + \varepsilon^ {2} x _ {1 2} + \varepsilon^ {3} R _ {x _ {1}}) ^ {2} ] \\ \times \left(x _ {2 0} + \varepsilon x _ {2 1} + \varepsilon^ {2} x _ {2 2} + \varepsilon^ {3} R _ {x _ {2}}\right) \\ \end{array}
$$

匹配 $\varepsilon^0$ 的系数，可得 $\dot{x}_{10} = x_{20},\quad x_{10}(0) = \eta_{10}$

$$\dot {x} _ {2 0} = - x _ {1 0}, \quad x _ {2 0} (0) = \eta_ {2 0}$$

它是当 $\varepsilon=0$ 时的非扰动问题。匹配 $\varepsilon$ 的系数，得

$$\dot {x} _ {1 1} = x _ {2 1}, \quad x _ {1 1} (0) = \eta_ {1 1}\dot {x} _ {2 1} = - x _ {1 1} + \left(1 - x _ {1 0} ^ {2}\right) x _ {2 0}, \quad x _ {2 1} (0) = \eta_ {2 1}$$

匹配 $\varepsilon^2$ 的系数，有

$$\dot {x} _ {1 2} = x _ {2 2}, \quad x _ {1 2} (0) = \eta_ {1 2}\dot {x} _ {2 2} = - x _ {1 2} + \left(1 - x _ {1 0} ^ {2}\right) x _ {2 1} - 2 x _ {1 0} x _ {1 1} x _ {2 0}, \quad x _ {2 2} (0) = \eta_ {2 2}$$

后两组方程即为 k=1,2 时方程(10.8)的形式。

计算出 $x_{0}, x_{1}, \cdots, x_{N-1}$ ，现在的任务就是证明 $\sum_{k=0}^{N-1} x_{k}(t) \varepsilon^{k}$ 确实是 $x(t, \varepsilon)$ 的一个 $O(\varepsilon^{N})$ 逼近。考虑逼近误差

$$e = x - \sum_ {k = 0} ^ {N - 1} x _ {k} (t) \varepsilon^ {k} \tag {10.9}$$

上式两边对 t 进行微分,并将式(10.1)、式(10.7)和式(10.8)的 x 和 $x_{k}$ 的导数代入,可证明 e 满足方程

$$\dot {e} = A (t) e + \rho_ {1} (t, e, \varepsilon) + \rho_ {2} (t, \varepsilon), \quad e \left(t _ {0}\right) = \varepsilon^ {N} R _ {\eta} (\varepsilon) \tag {10.10}$$

其中 $\rho_{1}(t,e,\varepsilon)=f(t,e+\sum_{k=0}^{N-1}x_{k}(t)\varepsilon^{k},\varepsilon)-f(t,\sum_{k=0}^{N-1}x_{k}(t)\varepsilon^{k},\varepsilon)-A(t)e$

$$\rho_ {2} (t, \varepsilon) = f (t, \sum_ {k = 0} ^ {N - 1} x _ {k} (t) \varepsilon^ {k}, \varepsilon) - f (t, x _ {0} (t), 0) - \sum_ {k = 1} ^ {N - 1} [ A (t) x _ {k} (t) + g _ {k} (\cdot) ] \varepsilon^ {k}$$
