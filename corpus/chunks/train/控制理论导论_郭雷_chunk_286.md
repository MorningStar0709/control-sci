$$
\begin{array}{l} \phi (\lambda) \stackrel {\text { def }} {=} \int_ {- \infty} ^ {\infty} \dots \int_ {- \infty} ^ {\infty} \mathrm{e} ^ {\mathrm{i} \lambda^ {\mathrm{T}} x} \frac {1}{(2 \pi) ^ {l / 2} (\det R) ^ {1 / 2}} \exp \left\{- \frac {1}{2} (x - \mu) ^ {\mathrm{T}} R ^ {- 1} (x - \mu) \right\} \mathrm{d} x \\ = \mathrm{e} ^ {\mathrm{i} \lambda^ {\mathrm{T}} \mu} \exp \left\{- \frac {\lambda^ {\mathrm{T}} R \lambda}{2} \right\}, \quad \lambda \in \mathbb {R} ^ {l}. \tag {4.1.13} \\ \end{array}
$$

由于特征函数和分布函数的相互对应关系，所以用式(4.1.13)可以定义正态分布：如果 $\pmb{\xi}$ 的特征函数由式(4.1.13)给出，那么称 $\pmb{\xi}$ 的分布函数服从正态分布，或 $\pmb{\xi}$ 为正态或Gauss随机向量，或 $\pmb{\xi}$ 为正态，记作 $\pmb{\xi} \in \mathcal{N}(\mu, R)$ .

注意到式 (4.1.13) 中不出现 $R$ 的逆阵，所以用式 (4.1.13) 来定义正态随机向量比用式 (4.1.6) 来定义更广，它包括了退化情形。例如一个常量，它的方差为 0，可看成是退化的正态变量。
