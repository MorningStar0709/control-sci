$$
\left\{ \begin{array}{r l} g _ {i} & = \delta_ {(n ^ {i - 1} + 1)}, \\ \mathrm{ad} _ {f} ^ {k} g _ {i} & = \delta_ {n ^ {i - 1} + k + 1}, \end{array} \right. \quad i = 1, \dots , m, \quad k = 1, \dots , n _ {i} - 1. \tag {8.3.5}
$$

记

$$f = \left[ f _ {1} ^ {1}, \dots , f _ {n _ {1}} ^ {1}, \dots , f _ {1} ^ {m}, \dots , f _ {n _ {m}} ^ {m} \right] ^ {\mathrm{T}}.$$

利用式 (8.3.5), 简单计算可得

$$
\frac {\partial f _ {t} ^ {s}}{\partial z _ {j} ^ {i}} = \left\{ \begin{array}{l l} 1, & s = i, \text {且} t = j + 1 ^ {\prime}, \quad s, i = 1, \dots , m; \\ 0, & \text {否则}; \quad t = 1, \dots , n _ {i}; \quad j = 1, \dots , n _ {i} - 1. \end{array} \right.
$$

因此我们可将 $f$ 表示为

$$f = \left[ 0, z _ {1} ^ {1}, \dots , z _ {n _ {1} - 1} ^ {1}, \dots , 0, z _ {1} ^ {m}, \dots , z _ {n _ {m} - 1} ^ {m} \right] ^ {\mathrm{T}} + Y [ z _ {n _ {1}} ^ {1}, \dots , z _ {n _ {m}} ^ {m} ]. \tag {8.3.6}$$

注意向量场 Y 只依赖于 $z_{n_{i}}^{i}, i=1,\cdots,m.$ 计算 $ad_{f}^{n_{i}}g_{i}$ 得

$$\mathrm{ad} _ {f} ^ {n _ {i}} g _ {i} = \left[ \frac {\partial Y _ {1} ^ {1}}{\partial z _ {n _ {i}} ^ {i}}, \dots , \frac {\partial Y _ {n _ {1}} ^ {1}}{\partial z _ {n _ {i}} ^ {i}}, \dots , \frac {\partial Y _ {1} ^ {m}}{\partial z _ {n _ {i}} ^ {i}}, \dots , \frac {\partial Y _ {n _ {m}} ^ {m}}{\partial z _ {n _ {i}} ^ {i}} \right] ^ {\mathrm{T}}.$$

注意到 $ad_{f}^{n_{i}}g_{i}$ 与 $X_{k}^{i}, i=1,\cdots,m, k=1,\cdots,n_{i}$ 可交换。于是有

$$\frac {\partial f _ {t} ^ {s}}{\partial z _ {n _ {i}} ^ {i}} = \text { const. }, \quad \forall s, t, i. \tag {8.3.7}$$

结合式 (8.3.6) 与式 (8.3.7), 得

$$
\left[ \begin{array}{c} \dot {z} ^ {1} \\ \vdots \\ \dot {z} ^ {m} \end{array} \right] = \left[ \begin{array}{c c c} A _ {1} ^ {1} & \dots & A _ {m} ^ {1} \\ & \vdots & \\ A _ {1} ^ {m} & \dots & A _ {m} ^ {m} \end{array} \right] \left[ \begin{array}{c} z ^ {1} \\ \vdots \\ z ^ {m} \end{array} \right] + \left[ \begin{array}{c c c} b _ {1} & \dots & 0 \\ & \vdots & \\ 0 & \dots & b _ {m} \end{array} \right] u, \tag {8.3.8}
$$

这里

$$
A _ {i j} - \left\{ \begin{array}{l l} \left[ \begin{array}{c c c c} 0 & \dots & 0 & c _ {j} ^ {i _ {1}} \\ 0 & \dots & 0 & c _ {j} ^ {i _ {2}} \\ & \vdots & & \\ 0 & \dots & 0 & c _ {j} ^ {i _ {n _ {i}}} \end{array} \right], & i \neq j \\ \left[ \begin{array}{c c c c c} 0 & 0 & \dots & 0 & c _ {i} ^ {i _ {1}} \\ 1 & 0 & \dots & 0 & c _ {i} ^ {i _ {2}} \\ & & \vdots & & \\ 0 & 0 & \dots & 1 & c _ {i} ^ {i _ {n _ {i}}} \end{array} \right], & i = j, \end{array} \right.
$$

且

$$b _ {i} = [ 1, 0, \dots , 0 ] ^ {\mathrm{T}}, \quad i = 1, \dots , m.$$

这正是完全能控线性系统的标准型. (将 $(z_{1}^{i},\cdots,z_{n_{i}}^{i})$ 反序排列并作一线性变换即得Brunovsky标准形.)
