证明 为了确定起见，不妨设 $\frac{\partial f_1}{\partial x_1} + \frac{\partial f_2}{\partial x_2} > 0, \forall [x_1, x_2]^T \in G.$

设 $\Gamma$ 是微分方程 (2.5.12) 的位于 $G$ 内的封闭轨线， $D$ 是由 $\Gamma$ 围成的区域。这时有

$$\oint_ {\Gamma} \left(f _ {2} \left(x _ {1}, x _ {2}\right) \mathrm{d} x _ {1} + f _ {1} \left(x _ {1}, x _ {2}\right) \mathrm{d} x _ {2}\right) \tag {2.5.22}= \iint_ {D} - \left(\frac {\partial f _ {1}}{\partial x _ {1}} + \frac {\partial f _ {2}}{\partial x _ {2}}\right) \mathrm{d} x _ {1} \mathrm{d} x _ {2}. \tag {2.5.23}$$

关系式 (2.5.23) 中右端积分依假定应为负。另一方面，左端积分为

$$\oint_ {\Gamma} \left(f _ {2} \left(x _ {1}, x _ {2}\right) \mathrm{d} x _ {1} + f _ {1} \left(x _ {1}, x _ {2}\right) \mathrm{d} x _ {2}\right)= \int_ {0} ^ {T} \left(f _ {2} \frac {\mathrm{d} x _ {1}}{\mathrm{d} t} - f _ {1} \frac {\mathrm{d} x _ {2}}{\mathrm{d} t}\right) \mathrm{d} t= \int_ {0} ^ {T} \left(f _ {2} f _ {1} - f _ {1} f _ {2}\right) \mathrm{d} t = 0. \tag {2.5.24}$$

关系式 (2.5.24) 中的 $T$ 表示封闭轨线的周期。得到的矛盾表示，在区域 $G$ 内没有非线性微分方程 (2.5.12) 的封闭轨线。

定理2.5.7 设 $x_{1} - x_{2}$ 平面上原点是非线性微分方程 (2.5.12) 在 $x_{2}$ 轴上的唯一奇点，一切从正 (负) $x_{2}$ 轴出发的轨线绕原点一周后又回到正 (负) 轴。如果这样确定的变换把正 $x_{2}$ 轴上某一不包含原点的闭区间变换到它自己，则必定存在非线性微分方程 (2.5.12) 的封闭轨线。此外，当把 $x_{2}$ 轴改为 $x_{1}$ 轴时，定理的结论仍成立。

证明 由定理假设和初值问题解的唯一性知，由微分方程(2.5.12)的轨线确定的从正 $x_{2}$ 轴到它自身的变换是拓扑变换。显然，如果它有不动点，那么从不动点出发的轨线必定是围绕原点 $x = 0$ 的闭轨线。

根据 Brouwer 不动点定理，把一个闭区间变换到它自身的拓扑变换必定有不动点。因为这个闭区间不包含原点，所以不动点不是原点。
