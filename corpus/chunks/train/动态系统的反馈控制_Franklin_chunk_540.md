# MPZ 法总结

(1) 通过关系式 $z=e^{sT}$ 映射零极点。  
（2）如果分子的阶数比分母的阶数低，则在分子中加入 $(z+1)$ 的幂项，直到分子分母的阶数相等为止。  
(3) 令 $D_{\mathrm{d}}(z)$ 的直流增益或低频增益与 $D_{\mathrm{c}}(s)$ 的相等。

比如：

$$D _ {\mathrm{c}} (s) = K _ {\mathrm{c}} \frac {s + a}{s + b} \tag {8.26}$$

的 MPZ 近似式为

$$D _ {\mathrm{d}} (z) = K _ {\mathrm{d}} \frac {z - \mathrm{e} ^ {- a T}}{z - \mathrm{e} ^ {- b T}} \tag {8.27}$$

运用连续系统和离散系统的终值定理可求得 $D_{\mathrm{c}}(s)$ 与 $D_{\mathrm{d}}(z)$ 的直流增益，再令二者相等即可求出 $K_{\mathrm{d}}$ 。其结果为

$$K _ {\mathrm{c}} \frac {a}{b} = K _ {\mathrm{d}} \frac {1 - \mathrm{e} ^ {- a T}}{1 - \mathrm{e} ^ {- b T}}$$

或

$$K _ {\mathrm{d}} = K _ {\mathrm{c}} \frac {a}{b} \left(\frac {1 - \mathrm{e} ^ {- b T}}{1 - \mathrm{e} ^ {- a T}}\right) \tag {8.28}$$

若 $D_{c}(s)$ 的分母阶数较高，该法的步骤2必须增加 $(z+1)$ 项。举例来说

$$D _ {\mathrm{c}} (s) = K _ {\mathrm{c}} \frac {s + a}{s (s + b)} \Rightarrow D _ {\mathrm{d}} (z) = K _ {\mathrm{d}} \frac {(z + 1) (z - \mathrm{e} ^ {- a T})}{(z - 1) (z - \mathrm{e} ^ {- b T})} \tag {8.29}$$

但因为这些传递函数的直流增益是无穷的，因此有必要用低频增益来代替它。通过删除纯积分项，即去掉极点 $s = 0$ 和 $z = 1$ ，之后可以得到

$$K _ {\mathrm{d}} = K _ {\mathrm{c}} \frac {a}{2 b} \Big (\frac {1 - \mathrm{e} ^ {- b T}}{1 - \mathrm{e} ^ {- a T}} \Big) \tag {8.30}$$

迄今为止，讨论的数字化方法中， $D_{\mathrm{d}}(z)$ 的分子、分母多项式中 $z$ 的幂次都相等。这意味着在 $k$ 时刻的差分方程输出需要 $k$ 时刻输入的采样值。例如，式（8.27）的 $D_{\mathrm{d}}(z)$ 可写为

$$\frac {U (z)}{E (z)} = D _ {\mathrm{d}} (z) = K _ {\mathrm{d}} \frac {1 - \alpha z ^ {- 1}}{1 - \beta z ^ {- 1}} \tag {8.31}$$

其中： $\alpha=e^{-aT}$ ； $\beta=e^{-bT}$ 。通过观察可知由式(8.31)可得到如下的差分方程：

$$u (k) = \beta u (k - 1) + K _ {\mathrm{d}} [ e (k) - \alpha e (k - 1) ] \tag {8.32}$$
