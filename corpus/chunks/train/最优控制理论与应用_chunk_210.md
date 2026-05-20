# 1. 全向推力火箭问题。

用火箭 P 追击目标 E, 设追击在平面上进行, 则可用下面的方程来描述火箭 P 与目标 E 的运动:

$$\dot {x} _ {\mathrm{P}} = v _ {x \mathrm{P}}\dot {y} _ {\mathrm{P}} = v _ {y \mathrm{P}}\dot {v} _ {x \mathrm{P}} = F \sin u - K v _ {x \mathrm{P}}\dot {v} _ {\gamma \mathrm{P}} = F \cos u - K v _ {\gamma \mathrm{P}}\dot {x} _ {\mathrm{E}} = W \sin v\dot {y} _ {\mathrm{E}} = W \cos v$$

其中， $x_{P}$ 、 $y_{P}$ 为火箭 P 在追击平面中的位置坐标， $x_{E}$ 、 $y_{E}$ 为目标 E 在追击平面中的位置坐标， $v_{xP}$ 、 $v_{yP}$ 为火箭 P 在追击平面中的速度分量，F 为火箭 P 的推力大小，为常数，推力方向与追击平面垂线方向夹角为 u, K 为空气阻力系数，为常数，W 为目标 E 的速度大小，为常数，速度方向与追击平面垂线方向夹角为 v。u、v 分别是 P、E 的控制量，由于推力和速度的方向可任意改变，所以 u, v 均不受限制。

当 $\mathbf{P},\mathbf{E}$ 间的距离不大于 $l$ 时，即 $(x_{\mathrm{P}} - x_{\mathrm{E}})^2 +(y_{\mathrm{P}} - y_{\mathrm{E}})^2\leqslant l^2$ ，就认为实现了捕获，其中 $l$ 为预先指定的常数。求微分对策问题：对于火箭 $\mathbf{P}$ ，选择 $u$ ，使得实现捕获的时间 $T$ 最小；对于目标 $\mathbf{E}$ ，选择 $v$ ，使得实现捕获的

时间 $T$ 最大。
