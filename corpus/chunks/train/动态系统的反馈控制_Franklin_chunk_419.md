# 7.4.2 从状态方程求解动态响应

研究了系统状态变量方程的结构后，现在我们转向从状态描述求解动态响应，以及找到状态描述与前面第6章讨论过的频率响应、零点和极点之间的关系。由式(7.18a)和式(7.18b)给出的一般状态方程开始，考虑频域问题。对下式进行拉普拉斯变换：

$$\dot {x} = A x + B u \tag {7.41}$$

得到

$$s \boldsymbol {X} (s) - \boldsymbol {x} (0) = \boldsymbol {A X} (s) + \boldsymbol {B U} (s) \tag {7.42}$$

这是一个代数方程。如果我们选择包含 $X(s)$ 的项移到式(7.42)的左边，同时注意到在矩阵乘法中相乘矩阵的前后次序很重要，整理上式得到

$$(s \boldsymbol {I} - \boldsymbol {A}) \boldsymbol {X} (s) = \boldsymbol {B} U (s) + \boldsymbol {x} (0)$$

如果在方程两边左乘矩阵 $(sI - A)$ 的逆，则有

$$\boldsymbol {X} (s) = (s \boldsymbol {I} - \boldsymbol {A}) ^ {- 1} \boldsymbol {B} U (s) + (s \boldsymbol {I} - \boldsymbol {A}) ^ {- 1} \boldsymbol {x} (0) \tag {7.43}$$

系统的输出为

$$
\begin{array}{l} Y (s) = \mathbf {C X} (s) + D U (s) \\ = \boldsymbol {C} (s \boldsymbol {I} - \boldsymbol {A}) ^ {- 1} \boldsymbol {B} U (s) + \boldsymbol {C} (s \boldsymbol {I} - \boldsymbol {A}) ^ {- 1} \boldsymbol {x} (0) + D U (s) \tag {7.44} \\ \end{array}
$$

该方程给出的是系统对初始条件和外部强迫输入的输出响应。整理有关 $U(s)$ 的项，并且假设零初始条件，由此得到系统的传递函数为

$$G (s) = \frac {Y (s)}{U (s)} = \boldsymbol {C} (s \boldsymbol {I} - \boldsymbol {A}) ^ {- 1} \boldsymbol {B} + D \tag {7.45}$$
