$$\dot {\tilde {V}} (x) \leqslant - \eta (\omega (x)), \forall x \in R _ {A}, x \neq 0 \tag {C.29}$$

除光滑性外,函数 $\tilde{V}(x)$ 满足定理 4.17 所述的所有条件。为了完成全部证明,我们用下面两个引理,使 $\tilde{V}(x)$ 光滑。这里只引用这两个引理,不做证明。□

引理 C.3 设 D 是 $R^{n}$ 上的开子集，并假设存在局部利普希茨函数 $\Phi: D \to R$ 和 $g: D \to R^{n}$ 以及连续函数 $\psi: D \to R$ ，使 $\Phi(x)$ 沿 $\dot{x} = g(x)$ 轨线的导数对于所有 $x \in D$ 满足 $\Phi(x) \leqslant \psi(x)$ ，那么对于给定的任意连续函数 $\mu: D \to (0, \infty)$ 和 $\nu: D \to (0, \infty)$ ，存在一个光滑函数 $\Psi: D \to R$ ，使得对于所有 $x \in D$ ，有 $|\Phi(x) - \Psi(x)| \leqslant \mu(x)$ 和 $\Psi(x) \leqslant \psi(x) + \nu(x)$ 。

证明: 见文献[118]定理 B.1。

引理 C.4 设 $D \subset R^{n}$ 是包含原点的定义域, 函数 $\Phi: D \to [0, \infty)$ 是正定的局部利普希茨函数, 且 $\Phi(x)$ 在 $x \neq 0$ 时光滑, 则存在一个在 $(0, \infty)$ 上光滑的 $K_{\infty}$ 类函数 $\sigma$ , 使得对于每个 $i = 0, 1, \cdots$ , 当 $r \to 0^{+}$ 时, $\sigma^{(i)}(r) \to 0$ ; 对于所有 r > 0, 有 $\sigma'(r) > 0$ , 且 $\Psi(x) = \sigma(\Phi(x))$ 在 D 上是光滑的。

证明: 见文献[118]引理4.3(定义域限定为D,而不是 $R^{n}$ )。

应用引理 C.3, 其中 $D = R_{A} - \{0\}$ , $\Phi(x) = \tilde{V}(x)$ , $g(x) = \tilde{f}(x)$ , $\psi(x) = -\eta(\omega(x))$ , $\mu(x) = (1/2)\alpha^{-1}(\omega(x))$ , $\nu(x) = (1/2)\eta(\omega(x))$ , 求在 $R_{A} - \{0\}$ 上光滑的函数 $\hat{V}(x)$ , 满足

$$\hat {\alpha} _ {1} (\omega (x)) \leqslant \hat {V} (x) \leqslant \hat {\alpha} _ {2} (\omega (x)), \qquad \dot {\hat {V}} (x) \leqslant - \hat {\alpha} _ {3} (\omega (x))$$

其中 $\hat{\alpha}_1(r) = (1/2)\alpha^{-1}(r)$ 和 $\hat{\alpha}_2(r) = 2r + (1/2)\alpha^{-1}(r)$ 是 $\mathcal{K}_{\infty}$ 类函数， $\hat{\alpha}_3(r) = (1/2)\eta(r)$ 在 $[0, \infty)$ 上是连续正定函数。现在应用引理 C.4，其中 $D = R_A, \Phi = \hat{V}$ ，求一个 $\mathcal{K}_{\infty}$ 类函数 $\sigma$ ，使得 $V(x) = \sigma(\hat{V}(x))$ 在 $R_A$ 上光滑。容易验证 $\alpha_i(r) = \sigma(\hat{\alpha}_i(r)), i = 1, 2$ 是 $\mathcal{K}_{\infty}$ 类函数，

$$\alpha_ {3} (r) = \hat {\alpha} _ {3} (r) \min _ {t \in [ \hat {\alpha} _ {1} (r), \hat {\alpha} _ {2} (r) ]} \sigma^ {\prime} (t)$$

在 $[0, \infty)$ 上是连续正定的，且有

$$\alpha_ {1} (\omega (x)) \leqslant V (x) \leqslant \alpha_ {2} (\omega (x))$$

和

$$\dot {V} (x) = \sigma^ {\prime} (\hat {V} (x)) \dot {\hat {V}} (x) \leqslant - \sigma^ {\prime} (\hat {V} (x)) \hat {\alpha} _ {3} (\omega (x)) \leqslant - \alpha_ {3} (\omega (x))$$

函数 V 满足定理 4.17 中的所有条件。由 $\{V(x) \leqslant c\} \subset \{\omega(x) \leqslant \alpha_{1}^{-1}(c)\}$ 得出，对于任意 c > 0，集合 $\{V(x) \leqslant c\}$ 是 $R_{A}$ 上的紧子集。
