# 向量和矩阵的范数

向量 $x$ 的范数 $\| x\|$ 是一个实值函数，具有下列性质：

- 对于所有 $x \in R^n$ , $\| x \| \geqslant 0$ , 当且仅当 $x = 0$ 时, $\| x \| = 0$ 。  
- 对于所有 $x, y \in R^n$ , $\| x + y \| \leqslant \| x \| + \| y \|$ 。  
- 对于所有 $\alpha \in R, x \in R^n$ , $\| \alpha x \| = |\alpha| \| x \|$ 。

第二个性质就是三角不等式。下面给出的是 $p$ 范数的定义

$$\left\| x \right\| _ {p} = \left(\left| x _ {1} \right| ^ {p} + \dots + \left| x _ {n} \right| ^ {p}\right) ^ {1 / p}, \quad 1 \leqslant p < \infty$$

和

$$\| x \| _ {\infty} = \max _ {i} | x _ {i} |$$

三种最常用的范数是 $\| x\| _1,\| x\|_{\infty}$ 和欧几里得范数

$$\| x \| _ {2} = \left(| x _ {1} | ^ {2} + \dots + | x _ {n} | ^ {2}\right) ^ {1 / 2} = \left(x ^ {\mathrm{T}} x\right) ^ {1 / 2}$$

所有 p 范数在下面的意义上是等价的, 即如果 $\|\cdot\|_{\alpha}$ 和 $\|\cdot\|_{\beta}$ 是两个不同的 p 范数, 那么存在正常数 $c_{1}, c_{2}$ 使得对于所有 $x \in R^{n}$ , 有不等式

$$c _ {1} \| x \| _ {\alpha} \leqslant \| x \| _ {\beta} \leqslant c _ {2} \| x \| _ {\alpha}$$

成立。对于1范数,2范数和 $\infty$ 范数,上面的不等式分别转化为

$$\| x \| _ {2} \leqslant \| x \| _ {1} \leqslant \sqrt {n} \| x \| _ {2}, \quad \| x \| _ {\infty} \leqslant \| x \| _ {2} \leqslant \sqrt {n} \| x \| _ {\infty}, \quad \| x \| _ {\infty} \leqslant \| x \| _ {1} \leqslant n \| x \| _ {\infty}$$

有关 $p$ 范数的一个重要结论是Hölder不等式

$$| x ^ {\mathrm{T}} y | \leqslant \| x \| _ {p} \| y \| _ {q}, \quad \frac {1}{p} + \frac {1}{q} = 1$$

其中 $x \in R^n, y \in R^n$ 。大多数情况下，我们用到的范数性质都是由满足任意范数的三个基本性质推导出来的，在这些情况下，下标 $p$ 可以省略，所表示的范数都可以看成任意 $p$ 范数。

一个 $m \times n$ 实数矩阵 A 定义了一个从 $R^{n}$ 到 $R^{m}$ 的线性映射 y = Ax，其中 A 的 p 范数定义为 $^{①}$

$$\| A \| _ {p} = \sup _ {x \neq 0} \frac {\| A x \| _ {p}}{\| x \| _ {p}} = \max _ {\| x \| _ {p} = 1} \| A x \| _ {p}$$

当 $p = 1,2$ 和 $\infty$ 时，上式分别改写为

$$\| A \| _ {1} = \max _ {j} \sum_ {i = 1} ^ {m} | a _ {i j} |, \quad \| A \| _ {2} = \left[ \lambda_ {\max} (A ^ {\mathrm{T}} A) \right] ^ {1 / 2}, \quad \| A \| _ {\infty} = \max _ {i} \sum_ {j = 1} ^ {n} | a _ {i j} |$$

这里 $\lambda_{\max}(A^{\mathrm{T}}A)$ 表示矩阵 $A^{\mathrm{T}}A$ 的最大特征值, 关于 $m \times n$ 维实矩阵 $A$ 和 $n \times \ell$ 维实矩阵 $B$ 的范数的一些常用性质如下:

$$\frac {1}{\sqrt {n}} \| A \| _ {\infty} \leqslant \| A \| _ {2} \leqslant \sqrt {m} \| A \| _ {\infty}, \quad \frac {1}{\sqrt {m}} \| A \| _ {1} \leqslant \| A \| _ {2} \leqslant \sqrt {n} \| A \| _ {1}\| A \| _ {2} \leqslant \sqrt {\| A \| _ {1} \| A \| _ {\infty}}, \quad \| A B \| _ {p} \leqslant \| A \| _ {p} \| B \| _ {p}$$
