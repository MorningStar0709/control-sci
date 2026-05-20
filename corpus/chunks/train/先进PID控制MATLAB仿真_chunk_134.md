# 【仿真实例】

验证卡尔曼滤波器的滤波性能。对象为二阶传递函数

$$G _ {\mathrm{p}} (s) = \frac {1 3 3}{s ^ {2} + 2 5 s}$$

取采样时间为 1ms，采用 Z 变换将对象离散化，并描述为离散状态方程的形式

$$x (k + 1) = A x (k) + B (u (k) + w (k))y (k) = C x (k)$$

带有测量噪声的被控对象输出为

$$y _ {v} (k) = C x (k) + v (k)$$

式中， $A = \left[ \begin{array}{l}1.0000000,0.0009876\\ 0.0000000,0.9753099 \end{array} \right],\quad B = \left[ \begin{array}{l}0.0000659\\ 0.1313512 \end{array} \right],\quad C = [1,0],\quad D = [0]$
