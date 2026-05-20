$$A _ {n i} \stackrel {\text { def }} {=} \{x: x \in C, \quad i 2 ^ {- n} \leqslant f (x) < (i + 1) 2 ^ {- n} \}, \quad i = 0, \dots , n 2 ^ {n} - 1, \tag {4.1.1}$$

为可测集. $f(\cdot)$ 在 $C$ 上的Lebesgue积分定义为

$$\int_ {C} f (x) \mathrm{d} x = \lim _ {n \cdot \infty} \left[ \sum_ {i = 0} ^ {n 2 ^ {n} - 1} i 2 ^ {- n} \lambda (A _ {n _ {i}}) + n \lambda (x: f (x) \geqslant n) \right], \tag {4.1.2}$$

这个极限一定存在，但可能无穷.

当 $f(\cdot)$ 不一定是非负时，则定义

$$f ^ {+} (x) \stackrel {\text { def }} {=} \max (f (x), 0), \quad f ^ {-} (x) \stackrel {\text { def }} {=} \max (- f (x), 0).$$

由于 $f(x) = f^{+}(x) - f^{-}(x)$ ，并且 $f^{+}(\cdot)$ 及 $f^{-}(\cdot)$ 都是非负函数，所以 $\int_{C} f^{+}(x) \mathrm{d}x$ 及 $\int_{C} f^{-}(x) \mathrm{d}x$ 都有定义。当这两个积分至少有一个有穷时，则定义 $f(\cdot)$ 在 $C$ 上的

Lebesgue 积分为

$$\int_ {C} f (x) \mathrm{d} x = \int_ {C} f ^ {+} (x) \mathrm{d} x - \int_ {C} f (x) \mathrm{d} x.$$

当 $f(\cdot)$ 几乎处处连续时，则 $f(\cdot)$ 为Riemann可积，其积分值等于它的Lebesgue积分.

由于有理数是可数集, 所以它的 Lebesgue 测度是 0. 因此, 上面提到的 Dirichlet 函数几乎处处等于 1, 它在 [0,1] 上虽然在 Riemann 积分意义下没有积分, 但它的 Lebesgue 积分取值为 1.

我们虽然只对 $\mathbb{R}^1$ 给出了可测集、可测函数及Lebesgue积分这些概念，但它们都可平行地推广到 $\mathbb{R}^n$ 上去.
