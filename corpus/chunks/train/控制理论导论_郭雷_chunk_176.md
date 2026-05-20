$$\boldsymbol {x} ^ {\mathrm{T}} \boldsymbol {M} _ {f} (x _ {0}) \boldsymbol {x} = - (x _ {1} - x _ {2}) ^ {2} - (x _ {1} ^ {2} + x _ {2} ^ {2}) - 6 x _ {2 0} ^ {2} x _ {2} ^ {2} \leqslant 0, \quad \forall \boldsymbol {x} \in \mathbb {R} ^ {2}, \tag {2.4.44}$$

并且不等式 (2.4.44) 中仅当 $x = 0$ 时等号成立，因此 $M_{f}(x)$ 是 $\mathbb{R}^2$ 中的负定矩阵。又若记 $W(x) = f(x)^{\mathrm{T}}f(x)$ 。则

$$\lim _ {| x | \rightarrow \infty} W (x) = \lim _ {| x | \rightarrow \infty} \left(x _ {1} ^ {2} + \left(x _ {1} - x _ {2} \left(1 + x _ {2} ^ {2}\right)\right) ^ {2}\right) = + \infty .$$

所以根据 Krasovskii 定理，x = 0 是式 (2.4.43) 的全局渐近稳定的平衡解.

定理 2.4.22(Jacobi 猜想) 设 $f: R^{2} \rightarrow R^{2}$ 连续可微， $f(0) = 0$ 。如果 $\forall x \in R^{2}$ ， $f(x)$ 的 Jacobi 矩阵 $\frac{\partial f(x)}{\partial x}$ 的特征值都有负实部，则微分方程 (2.4.19) 的零解 x = 0 全局渐近稳定。

此 Jacobi 猜想现已成为定理，其证明可见文献 [4].

有关非线性微分方程解的全局稳定性问题，有兴趣的读者可参阅文献[9],[16].
