# 5. 线性定常系统的综合设计

# 5.6 解耦控制——串联补偿器解耦

解：由图可求得被控对象部分的传递函数矩阵为: $G_{p}(s)=\left[\begin{array}{ccc}2s+1 & & \\ 1 & & \frac{1}{s+1}\end{array}\right]$ 根据补偿器Gc(s)的求解公式，有：

$$
G _ {c} (s) = G _ {p} ^ {- 1} (s) W (s) \left[ I - W (s) \right] ^ {- 1}
$$

3个矩阵相乘，第1个矩阵外面漏了逆矩阵的符号。最终化简结果是正确的。

$$
= \left[ \begin{array}{c c} \frac {1}{2 s + 1} & 0 \\ 1 & \frac {1}{s + 1} \end{array} \right] \left[ \begin{array}{c c} \frac {1}{s + 1} & 0 \\ 0 & \frac {1}{5 s + 1} \end{array} \right] \left[ \begin{array}{c c} \frac {s}{s + 1} & 0 \\ 0 & \frac {5 s}{5 s + 1} \end{array} \right] = \left[ \begin{array}{c c} \frac {2 s + 1}{s} & 0 \\ - (s + 1) (2 s + 1) & \frac {s + 1}{5 s} \end{array} \right]
$$

基于所求解的补偿器Gc(s),可实现解耦控制系统。

【注解】本例求得的解耦补偿器Gc(s)的传递函数阵的某个元素出现了分子多项式阶次高于分母多项式阶次,这会带来该解耦控制器工程上物理实现的困难,一般工程上只能做到近似实现。