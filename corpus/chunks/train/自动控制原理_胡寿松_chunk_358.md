<table><tr><td rowspan="2">系统阶数</td><td rowspan="2">闭环传递函数(0)</td><td colspan="5">系数</td><td rowspan="2">超调 量/%</td><td rowspan="2">大调 量/%</td><td rowspan="2">90% 上升时间</td><td rowspan="2">100%上升 时间t_s/s</td><td rowspan="2">调节时 间t_s/s</td></tr><tr><td>a</td><td>β</td><td>γ</td><td>δ</td><td>ε</td></tr><tr><td>2</td><td><img src="image/d0a6df1d0195c4f68a9a432884d2d55d7091d9bb6e27b1e3379f61032201819e.jpg"/></td><td>1.82</td><td></td><td></td><td></td><td></td><td>0.10%</td><td>0.00%</td><td>3.47</td><td>6.59</td><td>4.82</td></tr><tr><td>3</td><td><img src="image/68a874ab2ef0e9ac4c2d3b82019d8da8811b174ebc02959eafdc33b161ffcbc4.jpg"/></td><td>1.90</td><td>2.20</td><td></td><td></td><td></td><td>1.65%</td><td>1.36%</td><td>3.48</td><td>4.32</td><td>4.04</td></tr><tr><td>4</td><td><img src="image/3a4b09d3b73c9ea534787535c0eca7ea3257bc6e0ca0ed9491cd811bacbc3929.jpg"/></td><td>2.20</td><td>3.50</td><td>2.80</td><td></td><td></td><td>0.89%</td><td>0.95%</td><td>4.16</td><td>5.29</td><td>4.81</td></tr><tr><td>5</td><td><img src="image/abe9a0db5cee1c6e1e538ca6fc10a1f40338c768ace0b2a45c3ab60387863e26.jpg"/></td><td>2.70</td><td>4.90</td><td>5.40</td><td>3.40</td><td></td><td>1.29%</td><td>0.37%</td><td>4.84</td><td>5.73</td><td>5.43</td></tr><tr><td>6</td><td><img src="image/1772a788da6eb4dc8b1d2ee975bea61bcf2c6dd3be8d4e9391e3c8a85775428d.jpg"/></td><td>3.15</td><td>6.50</td><td>8.70</td><td>7.55</td><td>4.05</td><td>1.63%</td><td>0.94%</td><td>5.49</td><td>6.31</td><td>6.04</td></tr></table>

注：表中所有时间均为标准化时间。

查表 6-3, 有 $\alpha=1.90, \beta=2.20, \omega_{n}t_{s}=4.04$ 。代入要求值 $t_{s}=2s$ ，可求得 $\omega_{n}=2.02$ 。不难算得

$$K = 6. 1 4, \quad z = 1. 3 4, \quad p = 2. 8 4$$

校正网络及前置滤波器分别为

$$G _ {c} (s) = \frac {s + 1 . 3 4}{s + 2 . 8 4}, \quad G _ {p} (s) = \frac {1 . 3 4}{s + 1 . 3 4}$$

系统的实际性能指标为：

$$\sigma \% = 1.65 \%, \quad t _ {s} = 2 \mathrm{s}$$

上述计算结果表明， $\sigma\%$ 发生在容许的 $\Delta = \pm 2\%$ 误差带内，因此也可以认为系统的 $\sigma\% = 0$ 。

MATLAB 验证: 进行 MATLAB 仿真, 当系统无前置滤波器时, 单位阶跃响应如图 6-28 所示, 测得

$$\sigma \% = 21 \%, \quad t _ {s} = 3.49 \mathrm{s} (\Delta = 2 \%), \quad t _ {p} = 1.44 \mathrm{s}$$

当系统有前置滤波器时,单位阶跃响应如图 6-29 所示,测得

$$\sigma \% = 2 \%, \quad t _ {s} = 2. 4 \mathrm{s} (\Delta = 2 \%)$$
