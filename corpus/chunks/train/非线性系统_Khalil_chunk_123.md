$$\alpha_ {1} (\| x \|) \leqslant V (x) \leqslant \alpha_ {2} (\| x \|)$$

如果 $D = R^{n}$ 且 $V(x)$ 是径向无界的，则存在 $K_{\infty}$ 类函数 $\alpha_{1}$ 和 $\alpha_{2}$ ，使得上式对于任意 $x \in R^{n}$ 都成立。

证明: 见附录 C.4。

对于二次正定函数 $V(x)=x^{T}Px$ ，引理4.3是根据下述不等式得出的：

$$\lambda_ {\min} (P) \| x \| _ {2} ^ {2} \leqslant x ^ {\mathrm{T}} P x \leqslant \lambda_ {\max} (P) \| x \| _ {2} ^ {2}$$

引理4.4 考虑标量自治可微方程 $\dot{y} = -\alpha (y), y(t_0) = y_0$

其中 $\alpha$ 是定义在 $[0, a)$ 上的局部利普希茨 $\mathcal{K}$ 类函数。对于所有 $0 \leqslant y_0 < a$ ，当 $t \geqslant t_0$ 时方程有唯一解 $y(t)$ ，且 $y(t) = \sigma(y_0, t - t_0)$

其中， $\sigma$ 是定义在 $[0, a) \times [0, \infty)$ 上的 $\mathcal{KL}$ 类函数。

证明: 见附录 C.5。

通过几个可找出标量方程闭式解的特例, 可验证该引理的正确性。例如, 如果 $\dot{y} = -ky$ , k > 0, 那么解为

$$y (t) = y _ {0} \exp [ - k (t - t _ {0}) ] \Rightarrow \sigma (r, s) = r \exp (- k s)$$

另一个例子是,如果 $\dot{y} = -ky^{2}, k > 0$ ,那么解为

$$y (t) = \frac {y _ {0}}{k y _ {0} (t - t _ {0}) + 1} \Rightarrow \sigma (r, s) = \frac {r}{k r s + 1}$$

为了理解如何把K类函数和KL类函数引入李雅普诺夫分析,先看一下在定理4.1的证明中K类函数和KL类函数的应用。在证明中,希望选择 $\beta$ 和 $\delta$ ,满足 $B_{\delta}\subset\Omega_{\beta}\subset B_{r}$ 。利用正定函数 $V(x)$ 满足 $\alpha_{1}(\|x\|)\leqslant V(x)\leqslant\alpha_{2}(\|x\|)$

可选择 $\beta \leqslant \alpha_{1}(r)$ 和 $\delta \leqslant \alpha_{2}^{-1}(\beta)$ 。这是因为

$$V (x) \leqslant \beta \Rightarrow \alpha_ {1} (\| x \|) \leqslant \alpha_ {1} (r) \Leftrightarrow \| x \| \leqslant r$$

和 $\| x\| \leqslant \delta \Rightarrow V(x)\leqslant \alpha_{2}(\delta)\leqslant \beta$

在这个证明中,还希望说明当 $\dot{V}(x)$ 负定时,随着 t 趋于无穷,解 $x(t)$ 趋于零。由引理 4.3 可知,存在 K 类函数 $\alpha_{3}$ ,满足 $\dot{V}(x) \leqslant -\alpha_{3}(\|x\|)$ 。因此,V 满足微分不等式

$$\dot {V} \leqslant - \alpha_ {3} (\alpha_ {2} ^ {- 1} (V))$$

比较引理(引理3.4)说明 $V(x(t))$ 以标量微分方程

$$\dot {y} = - \alpha_ {3} (\alpha_ {2} ^ {- 1} (y)), y (0) = V (x (0))$$

的解为界。引理4.2表明 $\alpha_{3} \circ \alpha_{2}^{-1}$ 是 $\mathcal{K}$ 类函数，引理4.4表明标量方程的解为 $y(t) = \beta(y(0), t)$ ，其中 $\beta$ 为 $\mathcal{KL}$ 类函数。因此 $V(x(t))$ 满足不等式 $V(x(t)) \leqslant \beta(V(x(0)), t)$ 则说明了当 $t$ 趋于无穷时 $V(x(t))$ 趋于零。实际上，无须证明定理4.1即可给出 $\|x(t)\|$ 的估计值，该估计值在证明中未给出。不等式 $V(x(t)) \leqslant V(x(0))$ 是指

$$\alpha_ {1} (\| x (t) \|) \leqslant V (x (t)) \leqslant V (x (0)) \leqslant \alpha_ {2} (\| x (0) \|)$$

因此,有 $\parallel x(t)\parallel\leqslant\alpha_{1}^{-1}\left(\alpha_{2}\left(\parallel x(0)\parallel\right)\right)$ ，其中 $\alpha_{1}^{-1}\circ\alpha_{2}$ 是 K 类函数。同样，不等式 $V(x(t))\leqslant\beta(V(x(0)),t)$ 表示

$$\alpha_ {1} (\| x (t) \|) \leqslant V (x (t)) \leqslant \beta (V (x (0)), t) \leqslant \beta (\alpha_ {2} (\| x (0) \|), t)$$

因此，有 $\| x(t)\| \leqslant \alpha_1^{-1}(\beta (\alpha_2(\| x(0)\|),t))$ ，其中 $\alpha_{1}^{-1}(\beta (\alpha_{2}(r),t))$ 是 $\mathcal{KL}$ 类函数。
