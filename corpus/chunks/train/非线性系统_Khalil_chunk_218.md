# 7.1.2 Popov 判据

考虑系统(7.1)\~(7.3)的一个特例

$$\dot {x} = A x + B u \tag {7.13}y = C x \tag {7.14}u _ {i} = - \psi_ {i} (y _ {i}), 1 \leqslant i \leqslant p \tag {7.15}$$

其中 $x \in R^n, u, y \in R^p, (A, B)$ 是可控的， $(A, C)$ 是可观测的，且 $\psi_i: R \to R$ 是局部利普希茨的、无记忆的非线性函数，属于扇形区域 $[0, k_i]$ 。在此特例中，传递函数 $G(s) = C(sI - A)^{-1}B$ 是严格正则的， $\psi$ 是时不变去耦的，即 $\psi_i(y) = \psi_i(y_i)$ 。由于 $D = 0$ ，因此反馈连接有明确定义的状态模型。下面的定理称为 Popov 多变量判据，其证明应用了形如 $V = (1/2)x^{\mathrm{T}}Px + \sum \gamma_i \int_0^{y_i} \psi_i(\sigma)d\sigma$ 的（Lure 型）李雅普诺夫函数，该方法使环路变换得到进一步应用，即把系统(7.13)～(7.15)转换为两个无源系统的反馈连接。

定理7.3 系统(7.13)\~(7.15)若满足下述条件,则是绝对稳定的:当 $1 \leqslant i \leqslant p$ 时, $\psi_{i} \in [0, k_{i}]$ , 其中 $0 < k_{i} \leqslant \infty$ , 且存在常数 $\gamma_{i} \geqslant 0$ , 对于 $A$ 的每个特征值 $\lambda_{k}$ , 有 $(1 + \lambda_{k}\gamma_{i}) \neq 0$ , 使得 $M + (I + s\Gamma)G(s)$ 是严格正实的, 其中 $\Gamma = \text{diag}(\gamma_{1}, \cdots, \gamma_{p}), M = \text{diag}(1/k_{1}, \cdots, 1/k_{p})$ 。如果扇形区域条件 $\psi_{i} \in [0, k_{i}]$ 仅在集合 $Y \subset R^{p}$ 内满足, 那么前述条件保证了系统是有限区域绝对稳定的。

证明:由图7.12所示的环路变换得到 $\tilde{H}_{1}$ 和 $\tilde{H}_{2}$ 的反馈连接,其中 $\tilde{H}_{1}$ 是线性系统,其传递函数为

$$
\begin{array}{l} M + (I + s \Gamma) G (s) = M + (I + s \Gamma) C (s I - A) ^ {- 1} B \\ = M + C (s I - A) ^ {- 1} B + \Gamma C s (s I - A) ^ {- 1} B \\ = M + C (s I - A) ^ {- 1} B + \Gamma C (s I - A + A) (s I - A) ^ {- 1} B \\ = M + (C + \Gamma C A) (s I - A) ^ {- 1} B + \Gamma C B \\ \end{array}
$$

因而 $M + (I + s\Gamma)G(s)$ 可由状态模型 $\{\mathcal{A},\mathcal{B},\mathcal{C},\mathcal{D}\}$ 实现，其中 $\mathcal{A} = A,\mathcal{B} = B,\mathcal{C} = C + \Gamma CA,\mathcal{D} =$ $M + \Gamma CB$ 。设 $\lambda_{k}$ 是 $A$ 的一个特征值， $v_{k}$ 为其相应的特征向量，则有

$$(C + \Gamma C A) v _ {k} = (C + \Gamma C \lambda_ {k}) v _ {k} = (I + \lambda_ {k} \Gamma) C v _ {k}$$

条件 $(1+\lambda_{k}\gamma_{i})\neq0$ 是指 $(\mathcal{A},\mathcal{C})$ 是可观测的,因此 $\{\mathcal{A},\mathcal{B},\mathcal{C},\mathcal{D}\}$ 是最小实现。如果 $M+(I+s\Gamma)G(s)$ 是严格正实的,则可应用Kalman-Yakubovich-Popov引理得出结论:存在矩阵 $P=P^{T}>0,L$ 和W及正常数 $\varepsilon$ ,满足 $PA+A^{T}P=-L^{T}L-\varepsilon P$ (7.16)

$$P B = (C + \Gamma C A) ^ {\mathrm{T}} - L ^ {\mathrm{T}} W \tag {7.17}W ^ {\mathrm{T}} W = 2 M + \Gamma C B + B ^ {\mathrm{T}} C ^ {\mathrm{T}} \Gamma \tag {7.18}$$

且 $V = (1 / 2)x^{\mathrm{T}}Px$ 是 $\tilde{H}_1$ 的存储函数。另一方面，可以验证 $\tilde{H}_2$ 是无源的（见习题6.2），其存储函数为 $\sum_{i=1}^{p}\gamma_i\int_0^{y_i}\psi_i(\sigma)d\sigma$ 。这样图7.12所示变换后的反馈连接的存储函数为
