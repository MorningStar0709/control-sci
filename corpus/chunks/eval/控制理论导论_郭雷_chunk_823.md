# 习题 10.6

10.6.1 考察弦振动控制系统

$$
\left\{ \begin{array}{l l} \ddot {y} (, x, t) = y ^ {\prime \prime} (x, t) + u (x, t), & 0 <   x <   1, t > 0, \\ y (0, t) = y (1, t) = 0, \\ y (x, 0) = y _ {0} (x), \quad \dot {y} (x, 0) = y _ {1} (x), \end{array} \right.
$$

性能指标为

$$J (u) = \int_ {0} ^ {\infty} \int_ {0} ^ {1} \left(\frac {1}{4} | y ^ {\prime} (\xi , t _ {1}) | ^ {2} + | u (\xi , t _ {1}) | ^ {2}\right) d \xi d t.$$

试研究该系统的调节问题，找出最优控制和相应的最优性能指标值.
