# (2) 末端约束时的极小值原理

对于具有目标集约束条件的最优控制问题,需要把极小值原理的原始形式推广到末端受约束时的最优控制问题。

定理10-11 对于如下定常系统、末值型性能指标、末端受约束、控制也受约束的最优控制问题

$$\min _ {\boldsymbol {u} (t) \in \Omega} J (\boldsymbol {u}) = \varphi [ \boldsymbol {x} (t _ {f}) ]$$

s. t. ① $\dot{\pmb{x}}(t) = \pmb{f}(\pmb{x},\pmb{u})$ ， $\pmb{x}(t_0) = \pmb{x}_0$

$$② \psi [ x (t _ {f}) ] = 0$$

式中， $t_f$ 固定或自由； $\psi (\cdot)\in \mathbf{R}^r,r\leqslant n$ ，在 $[t_0,t_f]$ 上连续可微；其余假设同定理10-8。则必存在非零常向量 $\gamma \in \mathbf{R}^r$ 和 $\lambda (t)\in \mathbf{R}^n$ ，使最优解满足如下必要条件：

![](image/02eb6da18b2e915e73a3314eeac88ed884620faee0ffb91074c2a3cdb689d40e.jpg)

<details>
<summary>line</summary>

| t | λ(t) | u*(t) | x*(t) |
| --- | --- | --- | --- |
| 0 | 1.72 | 1 | 5 |
| 0.307 | 1 | 0.5 | 6 |
| 1 | 0 | 0.5 | 12.3 |
</details>

图10-4 例10-8最优解曲线
