$$\dot {V} = - \left(\mid x _ {1} \mid^ {\frac {3}{2}} + x _ {2} ^ {2}\right) + 2 \zeta (1 - \mid x _ {1} \mid^ {\frac {1}{2}}) \mid x _ {1} \mid^ {\frac {1}{2}} \mathrm{sign} (x _ {1}) x _ {2} +x _ {1} \frac {w}{k} + x _ {2} \frac {1 + k}{2 k \zeta} \frac {w}{k}\dot {V} = - \left(\left| x _ {1} \right| ^ {\frac {3}{2}} + x _ {2} ^ {2}\right) + x _ {1} \frac {w}{k} + x _ {2} \frac {1 + k}{2 k \zeta} \frac {w}{k} \tag {3.2.28}$$

可以把它整理成

$$\dot {V} = - \left(\mid x _ {1} \mid^ {\frac {3}{4}} \operatorname{sign} \left(x _ {1}\right) - \mid x _ {1} \mid^ {\frac {1}{4}} \frac {w}{2 k}\right) ^ {2} -\left(x _ {2} - \frac {1 + k}{2 k \zeta} \frac {w}{2 k}\right) ^ {2} + \left(\left| x _ {1} \right| ^ {\frac {1}{2}} + \left(\frac {1 + k}{2 k \zeta}\right) ^ {2}\right) \frac {w ^ {2}}{4 k ^ {2}}$$

欲使 $\dot{V} < 0$ 成立，必须

$$\left| x _ {1} \right| ^ {\frac {1}{2}} \left(\left| x _ {1} \right| ^ {\frac {1}{2}} \operatorname{sign} \left(x _ {1}\right) - \frac {w}{2 k}\right) ^ {2} + \left(x _ {2} - \frac {1 + k}{2 k \zeta} \frac {w}{2 k}\right) ^ {2} >\left(\mid x _ {1} \mid^ {\frac {1}{2}} + \left(\frac {1 + k}{2 k \zeta}\right) ^ {2}\right) \frac {w ^ {2}}{4 k ^ {2}}$$

当然如果不等式

$$\left| x _ {1} \right| ^ {\frac {1}{2}} \left(\left| x _ {1} \right| ^ {\frac {1}{2}} \operatorname{sign} \left(x _ {1}\right) - \frac {w}{2 k}\right) ^ {2} > \left(\left| x _ {1} \right| ^ {\frac {1}{2}} + \left(\frac {1 + k}{2 k \zeta}\right) ^ {2}\right) \frac {w ^ {2}}{4 k ^ {2}} \tag {3.2.29}$$

成立,那么不等式 $V < 0$ 必定成立.由此当满足不等式

$$\frac {4 k ^ {2}}{w ^ {2}} \left| x _ {1} \right| > \left(1 + \sqrt {\left(1 + \left(\frac {1 + k}{2 k \zeta}\right) ^ {2} \mid x _ {1} \mid^ {\frac {- 1}{2}}\right)}\right) ^ {2} (3. 2. 3 0)$$

时就有 V < 0. 这就是说, 当点 $(x_{1}, x_{2})$ 处于不等式(3.2.30) 决定的区域时, 经过该点的系统轨线终归要收敛到不等式

$$\left| x _ {1} \right| < \frac {w ^ {2}}{4 k ^ {2}} B, B = \frac {w ^ {2}}{4 k ^ {2}} \left(1 + \sqrt {\left(1 + \left(\frac {1 + k}{2 k \zeta}\right) ^ {2} \mid x _ {1} \mid^ {- \frac {1}{2}}\right)}\right) ^ {2} \tag {3.2.31}$$

决定的区域,因此 $x_{1}$ 的稳态误差小于 $\frac{w^{2}}{4k}B$ ,这个稳态误差是与 $k^{2}$ 成反比.在一般情况下,反馈增益 $k$ 是要取大于可能的扰动范围 $w_{0}$ 的值, $\frac{w_{0}}{k}$ 总是小于1的.因此非线性反馈时的闭环稳态误差(正比于 $\left(\frac{w_{0}}{k}\right)^{2}$ )比起线性反馈时的稳态误差(正比于 $\frac{w_{0}}{k}$ )小得多,可以相差好几个数量级.显然,从抑制扰动的能力来看,合适的非光滑反馈(3.2.25)比起线性反馈(3.2.20)具有更强的扰动抑制能力.

下面给出在闭环系统(3.2.26)中分别取k为5,10,20,而 $2\zeta$ 也分别取成 5,10,20 所作的仿真结果，这个仿真结果示于图 3.2.4.
