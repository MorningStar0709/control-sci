例4.3.3 设 $\{\xi_k\}$ 是正态宽平稳过程，那么它一定是狭义平稳过程。这是因为联合正态分布只取决于一、二阶矩，而宽平稳性决定了二阶矩经时间推移后不变，所以它必定是狭义平稳。

狭义平稳过程的分布不随推移变化, 这就使人想到 (可以证明), 有些集合是 “推不动” 的, 这些集合叫不变集, 不变集构成一个子 $\sigma$ -代数, 记作 $C$ .

对狭义平稳过程 $\{\xi_k\}$ , 当 $E\xi_1$ 存在时,

$$\frac {1}{n} \sum_ {k = 1} ^ {n} \xi_ {k} \underset {n \rightarrow \infty} {\longrightarrow} E (\xi_ {1} | \mathcal {C}) \quad \text { a.s. } \tag {4.3.4}$$

当 $\mathcal{C} = (\Omega, \phi)$ a.s. 时，则称狭义平稳过程 $\{\xi_k\}$ 具有遍历性，这时

$$\frac {1}{n} \sum_ {k = 1} ^ {n} \xi_ {k} \underset {n \to \infty} {\longrightarrow} E (\xi_ {1}) \quad \text { a.s. } \tag {4.3.5}$$

当 $\{\xi_k\}$ 为 iid 序列时, 据 Kolmogorov 强大数法则, 当 $E|\xi_1| < \infty$ 时, $\frac{1}{n} \sum_{k=1}^{n} \xi_k \to E\xi_1$ , 也就是具有遍历性.
