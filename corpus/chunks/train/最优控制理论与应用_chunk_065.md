# 4.3 最短时间控制问题

节省时间意味着提高生产率或先发制人取得军事行动的胜利。所以人们很早就开始了对最短时间控制的研究，这方面的研究结果很多，这里先就简单的重积分系统的最短时间控制展开讨论。

在前面的绪论中列举了火车快速行驶问题。设火车质量 $m = 1$ ，把运动方程写成状态方程形式，令 $x_{1} = x, x_{2} = \dot{x}$ ，可化为下面的最短时间控制问题。

例4-1 重积分系统的最短时间控制

状态方程

$$\dot {x} _ {1} = x _ {2} \tag {4-22}\dot {x} _ {2} = u$$

初始条件为

$$x _ {1} \left(t _ {0}\right) = x _ {1 0} \quad x _ {2} \left(t _ {0}\right) = x _ {2 0} \tag {4-23}$$

终端条件为

$$x _ {1} \left(t _ {\mathrm{f}}\right) = 0 \quad x _ {2} \left(t _ {\mathrm{f}}\right) = 0 \tag {4-24}$$

控制约束为

$$\mid u (t) \mid \leqslant 1 \quad t _ {0} \leqslant t \leqslant t _ {\mathrm{f}} \tag {4-25}$$

求出使性能指标

$$J = \int_ {t _ {0}} ^ {t _ {\mathrm{f}}} \mathrm{d} t = t _ {\mathrm{f}} - t _ {0} \tag {4-26}$$

取极小的最优控制。

解 因为控制作用有限制(属于有界闭集), 故要用极小值原理求解。取哈密顿函数

$$H = F + \boldsymbol {\lambda} ^ {T} \boldsymbol {f} = 1 + \lambda_ {1} (t) x _ {2} (t) + \lambda_ {2} (t) u (t) \tag {4-27}$$

协态方程为

$$\dot {\lambda} _ {1} = - \frac {\partial H}{\partial x _ {1}} = 0 \tag {4-28}\dot {\lambda} _ {2} = - \frac {\partial H}{\partial x _ {2}} = - \lambda_ {1} \tag {4-29}$$

积分上面两个方程可得

$$\lambda_ {1} (t) = c _ {1} \tag {4-30}\lambda_ {2} (t) = c _ {2} - c _ {1} t \tag {4-31}$$

其中， $c_{1}, c_{2}$ 是积分常数。

由 $H$ 的表达式(4-27)可见, 若要选择 $u(t)$ 使 $H$ 取极小, 只要使 $\lambda_2(t) u(t)$ 越负越好, 而 $|u(t)| \leqslant 1$ , 故当 $|u(t)| = 1$ , 且 $u(t)$ 与 $\lambda_2(t)$ 反号时, $H$ 取极小, 即最优控制为

$$
u (t) = - \operatorname{sgn} [ \lambda_ {2} (t) ] = \left\{ \begin{array}{l l} 1 & \text {当} \lambda_ {2} (t) <   0 \\ - 1 & \text {当} \lambda_ {2} (t) > 0 \end{array} \right.
$$

由此可见，最优解 $u(t)$ 取边界值 $+1$ 或 $-1$ ，是开关函数的形式。什么时候发生开关转换，将取决于 $\lambda_2(t)$ 的符号。而由式(4-31)可见， $\lambda_2(t)$ 是 $t$ 的线性函数，它有四种可能的形状（见图4-2）， $u(t)$ 也相应有四种序列：

$$\{+ 1 \}, \{- 1 \}, \{+ 1, - 1 \}, \{- 1, + 1 \}$$

由图4-2可见，当 $\lambda_2(t)$ 为 $t$ 的线性函数时， $u(t)$ 最多改变一次符号。

![](image/e502d46a8b24290a383a1e9ea42631aec4224d5a96d9bd7a494e93be4d8e57cc.jpg)

<details>
<summary>line</summary>

| t | λ₂(t) |
| --- | --- |
| 0 | 0.5 |
| >0 | 1 |
</details>

![](image/f55366f29e054e0bfa6163f24f43152640a808512881ef76460d8982de278c6b.jpg)

<details>
<summary>line</summary>

| t | u(t) | λ₂(t) |
| --- | --- | --- |
| 0 | 1 | -0.5 |
| >0 | 1 | -0.7 |
| <0 | 1 | -0.8 |
</details>

![](image/39bf63476067f237f66091793ab14ec1f37bf2ce185c9bd71b98267e24c0def5.jpg)

<details>
<summary>line</summary>

| t | u(t) | λ₂(t) |
| --- | --- | --- |
| 0 | 1 | 1 |
| c₁ | 0 | -1 |
| c₂ | 0 | -1 |
</details>
