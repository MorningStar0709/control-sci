引理8.5.2 对系统(8.5.1)，如果相对阶向量在 $x_0$ 有定义，且解耦矩阵 $A(x_0)$ 行满秩，则以下函数组局部线性无关：

$$\left\{d h _ {1}, \dots , d L _ {f} ^ {\rho_ {1} - 1} h _ {1}, \dots , d h _ {p}, \dots , d L _ {f} ^ {\rho_ {p} - 1} h _ {p} \right\}.$$

证明 设

$$\omega = \sum_ {i = 1} ^ {p} \sum_ {k = 0} ^ {\rho_ {i} - 1} \lambda_ {i k} \mathrm{d} L _ {f} ^ {k} h _ {i},$$

且 $\omega (x_0) = 0$ ，于是

$$\langle \omega , g \rangle = (\lambda_ {1 \rho_ {1} - 1}, \dots , \lambda_ {p \rho_ {p} - 1}) A (x _ {0}) = 0.$$

由于 $A(x_{0})$ 是行满秩的，故 $\lambda_{i\rho_{i}-1}=0, i=1,\cdots,p.$ 此外，我们有

$$\langle \omega , \mathrm{ad} _ {f} g \rangle = L _ {f} \langle \omega , g \rangle - \langle L _ {f} \dot {\omega}, g \rangle= - (\lambda_ {1} \dots \dots , \lambda_ {2} - 2) A (m _ {n}) = 0$$

故 $\lambda_{ij} = 2 \equiv 0, i = 1, \ldots, p$ 注意：如果 $\rho_{i} = 1$ 则在上述方程中将没有 $\lambda_{tp}$ 相应地 $\overline{A(x_{0})}$ 的第 $x$ 行也将被删去。由无 $\overline{A(x_{0})}$ 剩下的行仍然是线性无关的，这组系数仍为零重复上述过程，我们最后得到 $\lambda_{ij} \equiv 0$ ；引理获证：

定理8.5.1 设相对阶在 $x_0$ 上有定义，则局部输入输出解耦问题在 $x_0$ 是可解的充分必要条件是解耦矩阵在 $x_0$ 有秩 $p$ .

证明 (必要性) 设问题可由正则反馈控制 $(\alpha(x), \beta(x))$ 解决. 由于现在块控制 $v^j$ 不影响 $y_i, j \neq i$ , 故有

$$L _ {\bar {g} ^ {j}} L _ {\bar {f}} ^ {k} h _ {i} (x) = 0, \quad j \neq i, k \geqslant 0, x \in U.$$

于是，相应的这个反馈的解耦阵变为

$$
\tilde {A} (x) = \left[ \begin{array}{c c c c} \tilde {A} _ {1} & 0 & \dots & 0 \\ 0 & \tilde {A} _ {2} & \dots & 0 \\ 0 & 0 & \dots & \tilde {A} _ {p} \end{array} \right].
$$

由于相对阶向量有定义，故每一个 $\tilde{A}_i(x_0)$ 应该有秩1.因此

$$\operatorname{rank} (A (x _ {0})) = \operatorname{rank} (\tilde {A} (x _ {0})) = p.$$

(充分性) 由假设，存在 $x_0$ 的一个邻域 $U$ ，使得

$$\operatorname{rank} (A (x)) = p, \quad x \in U.$$

不失一般性，可将 $A(x)$ 表示为

$$A (x) = \left(A _ {1} (x), A _ {2} (x)\right),$$

并假定 $A_{1}(x)$ 是非奇异的，因此，可找到作列消去的 $\beta_{1}(x)$ 使得

$$A (x) \beta_ {1} (x) = (A _ {1} (x), 0).$$

令

$$
\beta_ {2} (x) = \left[ \begin{array}{c c} A _ {1} ^ {- 1} (x) & 0 \\ 0 & I _ {m - p} \end{array} \right],
$$

及

$$\beta (x) = \beta_ {1} (x) \beta_ {2} (x).$$

那么 $\beta (x)$ 是非奇异的，且

$$A (x) \beta (x) = (I _ {r}, 0).$$

设

$$
\alpha (x) = - \beta_ {1} (x) \left[ \begin{array}{c} A _ {1} ^ {- 1} (x) b (x) \\ 0 \end{array} \right],
$$

则

$$
A (x) \alpha (x) = (A _ {1} (x), 0) \left[ \begin{array}{c} - A _ {1} ^ {- 1} (x) b (x) \\ 0 \end{array} \right] = - b (x),
$$

即 $\bar{b}(x)=0.$

在这个反馈控制下，我们有

$$
\left\{ \begin{array}{l} L _ {\bar {g} _ {j}} L _ {\bar {f}} ^ {\rho_ {i} - 1} h _ {i} (x) = \delta_ {i j}, \\ L _ {\bar {f}} ^ {\rho_ {i}} h _ {i} (x) = 0. \end{array} \right. \tag {8.5.11}
$$

根据式 (8.5.11), 用归纳法可以证明
