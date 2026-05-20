# 1.3.3 离散系统的数字 PID 控制仿真

控制对象为

$$G (s) = \frac {5 2 3 5 0 0}{s ^ {3} + 8 7 . 3 5 s ^ {2} + 1 0 4 7 0 s}$$

采样时间为 1ms，采用 z 变换进行离散化，经过 z 变换后的离散化对象为

$$y (k) = - \mathrm{den} (2) y (k - 1) - \mathrm{den} (3) y (k - 2) - \mathrm{den} (4) y (k - 3)+ \operatorname{num} (2) u (k - 1) + \operatorname{num} (3) u (k - 2) + \operatorname{num} (4) u (k - 3)$$
