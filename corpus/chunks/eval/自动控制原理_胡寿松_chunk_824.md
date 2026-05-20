$$\boldsymbol {\lambda} \left(t _ {f}\right) = \frac {\partial}{\partial \boldsymbol {x} \left(t _ {f}\right)} \left[ \frac {1}{2} \boldsymbol {x} ^ {\mathrm{T}} \left(t _ {f}\right) \boldsymbol {F x} \left(t _ {f}\right) \right] = \boldsymbol {F x} \left(t _ {f}\right) \tag {10-105}$$

由于在式(10-105)中， $\pmb{\lambda}(t_f)$ 与 $\pmb{x}(t_f)$ 存在线性关系，且正则方程又是线性的，因此可以假设

$$\boldsymbol {\lambda} (t) = \boldsymbol {P} (t) \boldsymbol {x} (t), \quad \forall t \in [ t _ {0}, t _ {f} ] \tag {10-106}$$

式中矩阵 $P(t)$ 待定。对上式求导，得

$$\dot {\boldsymbol {\lambda}} (t) = \dot {\boldsymbol {P}} (t) \boldsymbol {x} (t) + \boldsymbol {P} (t) \dot {\boldsymbol {x}} (t) \tag {10-107}$$

将式 $(10-103)$ 和式 $(10-106)$ 代入式 $(10-107)$ ，有

$$\dot {\boldsymbol {\lambda}} (t) = \left[ \dot {\boldsymbol {P}} (t) + \boldsymbol {P} (t) \boldsymbol {A} (t) - \boldsymbol {P} (t) \boldsymbol {B} (t) \boldsymbol {R} ^ {- 1} (t) \boldsymbol {B} ^ {\mathrm{T}} (t) \boldsymbol {P} (t) \right] \boldsymbol {x} (t) \tag {10-108}$$

将式 $(10-106)$ 代入式 $(10-104)$ ，则又有

$$\dot {\boldsymbol {\lambda}} (t) = - \left[ \boldsymbol {Q} (t) + \boldsymbol {A} ^ {\mathrm{T}} (t) \boldsymbol {P} (t) \right] \boldsymbol {x} (t) \tag {10-109}$$

比较式(10-108)和式(10-109)，立即证得里卡蒂方程(10-99)成立。

在式(10-106)中，令 $t=t_{f}$ ，有

$$\boldsymbol {\lambda} (t _ {f}) = \boldsymbol {P} (t _ {f}) \boldsymbol {x} (t _ {f})$$

上式与横截条件式(10-105)比较,证得里卡蒂方程的边界条件式(10-100)成立。

因 $P(t)$ 可解，将式(10-106)代入式(10-102)，证得 $\pmb{u}^{*}(t)$ 表达式(10-97)。

显然，将式(10-97)代入式(10-96)，得式(10-101)最优闭环系统方程，其解必为最优轨线 $x^{*}(t)$ 。

充分性: 若式(10-97)成立, 可证 $u^{*}(t)$ 必为最优控制。

根据连续动态规划法,可以方便地证明最优控制的充分性及最优性能指标(10-98)成立。其证明过程略。

在上述定理的证明过程中,应用了里卡蒂方程解的有关性质,需要加以说明。
