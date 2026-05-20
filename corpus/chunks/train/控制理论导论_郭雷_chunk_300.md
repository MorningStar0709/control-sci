推论 4.2.1 若 $\{X_{j}\}, j=1,2,\cdots$ ，为相互独立同分布 (iid)，则当 $E|X_{1}|^{1+\delta}<\infty$ 时，弱大数定理的条件成立；当 $E|X_{1}|^{2+\delta}<\infty$ 时，则中心极限定理的条件成立.

定理 4.2.4 所阐述的中心极限定理要求 $2 + \delta$ -阶矩 $E|X_{j}|^{2+\delta} < \infty$ ，其实只要求 $EX_{j}^{2} < \infty$ ，也可以得到中心极限定理。我们可以证明下面的定理：

定理 4.2.3 设 $\{X_{j}\}, j = 1, 2, \cdots$ ，为相互独立的随机变量， $\sigma_{j}^{2} = E(X_{j} - EX_{j})^{2}$ ， $s_{n} = \left(\sum_{j=1}^{n} \sigma_{j}^{2}\right)^{\frac{1}{2}}$ ，则

$$P \left\{s _ {n} ^ {- 1} \sum_ {j = 1} ^ {n} (X _ {j} - E X _ {j}) < x \right\} \to \frac {1}{\sqrt {2 \pi}} \int_ {- \infty} ^ {x} \mathrm{e} ^ {- \frac {- t ^ {2}}{2}} \mathrm{d} t \text {及} \max _ {1 \leqslant j \leqslant s} \frac {\sigma_ {s}}{s _ {n}} \underset {n \to \infty} {\longrightarrow} 0$$

的充分必要条件是成立 Lindeberg 条件：对任意 $\epsilon > 0$

$$\frac {1}{s _ {n} ^ {2}} \sum_ {j = 1} ^ {n} \int_ {| x | \geqslant \epsilon s _ {n}} x ^ {2} \mathrm{d} F _ {j} (x) \underset {n \rightarrow \infty} {\longrightarrow} 0,$$

这里 $F_{j}(\cdot)$ 表示 $X_{j}$ 的分布函数.
