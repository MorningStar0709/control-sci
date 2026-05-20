# 3. 平面拦截问题。

设飞机 $\mathbf{P},\mathbf{E}$ 在一平面上做拦截对策，分别以前向常速度 $v_{\mathrm{P}},v_{\mathrm{E}}$ 做相向飞行。 $\mathbf{P},\mathbf{E}$ 的横向位置记做 $x_{\mathrm{P}},x_{\mathrm{E}}$ ，将由它们的横向速度 $v(t),u(t)$ 分别调节，于是，飞机 $\mathbf{P},\mathbf{E}$ 的运动状态微分方程组为

$$\dot {x} _ {\mathrm{p}} = v\dot {x} _ {\mathrm{E}} = ux _ {\mathrm{P}} \left(t _ {0}\right) = x _ {\mathrm{P}} ^ {0}, x _ {\mathrm{E}} \left(t _ {0}\right) = x _ {\mathrm{E}} ^ {0}$$

记 $x(t) = x_{\mathrm{E}}(t) - x_{\mathrm{P}}(t)$ ，则上述方程组可写成

$$\dot {x} = u - vx \left(t _ {0}\right) = x _ {0} = x _ {\mathrm{E}} ^ {0} - x _ {\mathrm{P}} ^ {0}$$

衡量拦截效果的指标选取为支付

$$J (u, v) = \frac {1}{2} x ^ {2} \left(t _ {\mathrm{f}}\right) + \frac {1}{2} \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} \left(\gamma_ {2} u ^ {2} - \gamma_ {1} v ^ {2}\right) \mathrm{d} t$$

其中， $t_{f}=\frac{L}{v_{E}+v_{P}}$ 是截击时间， $\gamma_{2},\gamma_{1}$ 是飞机P，E控制能量或努力程度的权重， $\gamma_{2}\geqslant0,\gamma_{1}\geqslant0$ 。 $J(u,v)$ 是终端距离与控制能量加权之和，飞机E力图控制 $u(t)$ 使支付 $J(u,v)$ 获得最大值，而飞机P力图控制 $v(t)$ 使支付 $J(u,v)$ 获得最小值。求解该微分对策问题。
