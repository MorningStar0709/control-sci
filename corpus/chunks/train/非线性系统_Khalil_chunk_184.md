$u^{T}y=0$ 是无源性的极限情况。在这种情况下,我们认为系统是无损耗的。理想变压器就是一个无损耗系统的实例,如图6.3所示。这里 y=Su,其中

$$
u = \left[ \begin{array}{l} v _ {1} \\ i _ {2} \end{array} \right], y = \left[ \begin{array}{l} i _ {1} \\ v _ {2} \end{array} \right], S = \left[ \begin{array}{c c} 0 & - N \\ N & 0 \end{array} \right]
$$

矩阵 S 是斜对称的, 即 $S^{T} + S = 0$ 。因此 $u^{T}y = u^{T}Su = (1/2)u^{T}(S^{T} + S)u = 0$ 。

![](image/efcaeac534bde92800f5149c67005d8a69a11488758ca4b42741cec60b5936c7.jpg)

<details>
<summary>text_image</summary>

N
+ → i₁
v₁
-           i₂ + 
             v₂
             -
</details>

$$v _ {2} = N v _ {1}\boldsymbol {i} _ {1} = - N \boldsymbol {i} _ {2}$$

图 6.3 理想变压器

现在考虑函数 h，对于某个函数 $\varphi(u)$ ，满足 $u^{T}y \geqslant u^{T}\varphi(u)$ 。当对于所有 $u \neq 0, u^{T}\varphi(u) > 0$ 时，h 称为严格输入无源的，因为只有当 u = 0 时，有 $u^{T}y = 0$ ，在这个意义下无源性是严格的。同样，在标量情况下，除原点以外，u - y 曲线与 u 轴不相交。 $u^{T}\varphi(u)$ 一项表示“过量”无源性。另一方面，如果对于某些 u 值， $u^{T}\varphi(u)$ 为负，则函数 h 不一定是无源的。 $u^{T}\varphi(u)$ 一项表示“欠量”无源性。当 h 是标量且 $\varphi(u) = \varepsilon u$ 时，过量和欠量无源性将更明显。在这种情况下，h 属于扇形区域 $[\varepsilon, \infty]$ ，如图 6.4 所示，当 $\varepsilon > 0$ 时为过量无源，当 $\varepsilon < 0$ 时为欠量无源。通过输入前馈运算可消除过量或欠量无源性，如图 6.4(c) 所示。定义新的输出为 $\tilde{y} = y - \varphi(u)$ ，我们有

$$u ^ {\mathrm{T}} \tilde {y} = u ^ {\mathrm{T}} [ y - \varphi (u) ] \geqslant u ^ {\mathrm{T}} \varphi (u) - u ^ {\mathrm{T}} \varphi (u) = 0$$

因此,通过输入前馈,任何满足 $u^{\mathrm{T}}y \geqslant u^{\mathrm{T}}\varphi(u)$ 的函数都能转换为属于扇形区域 $[0,\infty]$ 的函数。这样的函数称为输入前馈无源函数。另一方面,假设对某个函数 $\rho(y)$ ,有 $u^{\mathrm{T}}y \geqslant y^{\mathrm{T}}\rho(y)$ 。如前所述,当对于所有 $y \neq 0$ 有 $y^{\mathrm{T}}\rho(y) > 0$ 时,函数存在过量无源性。而当对于某个 $y$ 值, $y^{\mathrm{T}}\rho(y)$ 为负时,函数存在欠量无源性。图6.5所示为 $\rho(y) = \delta y$ 时标量情况的图形表示。当 $\delta > 0$ 时,存在“过量”无源性,当 $\delta < 0$ 时,存在欠量无源性。过量或欠量无源性都可以通过输出反馈消除,如图6.5(c)所示。定义新的输入为 $\tilde{u} = u - \rho(y)$ ,我们有

$$\tilde {u} ^ {\mathrm{T}} y = [ u - \rho (y) ] ^ {\mathrm{T}} y \geqslant y ^ {\mathrm{T}} \rho (y) - y ^ {\mathrm{T}} \rho (y) = 0$$

因此通过输出反馈,任何满足 $u^{T}y \geqslant y^{T}\rho(y)$ 的函数都能转换为属于扇形区域 $[0, \infty]$ 的函数。这样的函数称为输出反馈无源函数。当对于所有 $y \neq 0$ , 有 $y^{T}\rho(y) > 0$ 时, 函数称为严格输出无源函数, 因为仅当 y = 0 时 $u^{T}y = 0$ 成立, 在此意义下无源性才是严格的。同样, 在标量情况下, u - y 曲线与 y 轴除原点外不相交。为方便, 在下一个定义中对不同无源性的概念进行总结。

![](image/5c8b4d067465a3fab1b23b3be3151de066f715aafdc294c122d4f90a913290e9.jpg)

<details>
<summary>text_image</summary>

y
u
</details>

(a)
