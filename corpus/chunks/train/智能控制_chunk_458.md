# 9.11.1 系统描述

考虑如下非线性离散系统

$$y (k + 1) = f (\pmb {x} (k)) + u (k) \tag {9.77}$$

式中， $x(k)=[y(k)\quad y(k-1)\quad\cdots\quad y(k-n+1)]^{\mathrm{T}}$ 为状态向量， $u(k)$ 为控制输入， $y(k)$ 为系统输出，假设非线性光滑函数 $f:R^{n}\rightarrow R$ 为未知。

控制任务为 $y(k)$ 跟踪 $y_{\mathrm{d}}(k)$ 。
