证明 (1) $\Longrightarrow$ (2) $\Longrightarrow$ (4) 和 (2) $\Longrightarrow$ (3) 显然成立. 我们证明另外两个关系:

现在证明 (3) $\Longrightarrow$ (2). 令 $I = \{i_1, \cdots, i_s\}$ , 和 $X, Y \in \Delta_I$ . 于是 $X, Y$ 可表示为 $X = X_1 + \cdots + X_s$ , $Y = Y_1 + \cdots + Y_s$ , $X_j, Y_j \in \Delta_i$ ; 且

$$[ X, Y ] = \sum_ {j, k = 1} ^ {s} [ X _ {j}, Y _ {k} ] \subset \sum_ {j, k = 1} ^ {s} (\Delta_ {i _ {j}} + \Delta_ {i _ {k}}) = \Delta_ {I}.$$

$((4) \Longrightarrow (1))$ 由于 $\Delta$ 是非奇异且是对合，故存在 $n_0 (= n - \operatorname{rank}(\Delta))$ 个线性无关的光滑函数，记作 $a_1^0, \dots, a_{n_0}^0$ ，使得

$$\left\langle \mathrm{d} a _ {j} ^ {0}, \Delta \right\rangle = 0, \quad j = 1, \dots , n _ {0}. \tag {8.4.39}$$

类似地，由于 $\Delta^{-i}$ 是非奇异且对合的，故存在 $n_{i}(=\operatorname{rank}(\Delta_{i}))$ 个光滑函数，记作 $a_{1}^{i},\cdots,a_{n_{i}}^{i}$ ，使得 $a_{1}^{0},\cdots,a_{n_{0}}^{0}$ 和 $a_{1}^{i},\cdots,a_{n_{i}}^{i}$ 线性无关，且

$$\left\langle \mathrm{d} a _ {j} ^ {i}, \Delta^ {- i} \right\rangle = 0, \quad j = 1, \dots , n _ {i}, i = 1, \dots , k. \tag {8.4.40}$$

我们证明 n 个余向量场 $da_{j}^{i}, \quad i = 0, 1, \cdots, k, \quad j = 1, \cdots, n_{i}$ 在 $x_{0}$ 上线性无关。为此令 $\lambda_{j}^{i} \in R^{1}$ ，且

$$\omega := \sum_ {i = 0} ^ {k} \sum_ {j = 0} ^ {n _ {i}} \lambda_ {j} ^ {i} \mathrm{d} a _ {j} ^ {i} = 0. \tag {8.4.41}$$

记 $\omega = \sum_{i=0}^{k} \omega_i$ , 这里 $\omega_i := \sum_{j=0}^{n_i} \lambda_j^i \mathrm{d}a_j^i$ . 选择一向量场

$$X \in \Delta_ {i} \subset \Delta^ {- j}, \quad j \neq i, 1 \leqslant i \leqslant k.$$

由定义有 $\langle \omega_i, \Delta^{-i} \rangle = 0$ .

又因为 $\langle \omega, X \rangle = \langle \omega_i, X \rangle = 0, \quad X \in \Delta_i$ ，所以 $\langle \omega_i, \Delta_i \rangle = 0$ .

于是 $\langle \omega_{i},\Delta \rangle = 0$ ，即

$$\omega_ {i} \in \Delta^ {\perp} = \operatorname{span} \left\{\mathrm{d} a _ {j} ^ {0} \mid j = 1, \dots , n _ {0} \right\}.$$

注意到 $\omega_{i}, i > 0$ 与 $\operatorname{span}\left\{\mathrm{d}a_{j}^{0} \mid j = 1, \cdots, n_{0}\right\}$ 线性独立，故

$$\lambda_ {j} ^ {i} = 0, \quad i = 1, \dots , k, j = 1, \dots , n _ {i}.$$

于是式 (8.4.41) 成为

$$\omega = \sum_ {j = 0} ^ {n _ {0}} \lambda_ {j} ^ {0} \mathrm{d} a _ {j} ^ {0} = 0,$$

这说明

$$\lambda_ {j} ^ {0} = 0, \quad j = 1, \dots , n _ {0},$$

从而独立性获证．于是我们可以选局部坐标

$$x _ {j} ^ {i} = a _ {j} ^ {i}, \quad i = 0, \dots , k, j = 1, \dots , n _ {i}.$$

根据式 (8.4.39) 及式 (8.4.40), 有
