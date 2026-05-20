# 本征元测试法

在应用中，通常取 $H = L^{2}(\Omega)$ ， $\Omega$ 为 $\mathbb{R}^{n}$ 中一有界区域。我们研究局部分布控制。为此我们取 $U = L^{2}(\Omega)$ ， $b \in L^{\infty}(\Omega)$ 为一非负函数，而

$$B \varphi = b \varphi , \quad \forall \varphi \in L ^ {2} (\Omega),$$

u 取速度反馈控制： $u(t) = -\mathrm{d}y(t)/\mathrm{d}t$ 。于是相应的闭环系统成为

$$\frac {\mathrm{d} ^ {2} y (t)}{\mathrm{d} t ^ {2}} + A y (t) + b \frac {\mathrm{d} y (t)}{\mathrm{d} t} = 0, \quad t > 0. \tag {10.4.2}$$

此外，我们还考虑另一个相关的控制系统

$$\frac {\mathrm{d} ^ {2} y (t)}{\mathrm{d} t ^ {2}} + A y (t) = \delta_ {J} u (t), \tag {10.4.3}$$

其中 $\delta_J(\cdot)$ 是 $\Omega$ 上子集 $J$ 的特征函数

$$
\delta_ {J} (x) = \left\{ \begin{array}{l l} 1, & x \in J, \\ 0, & x \in \Omega \backslash J. \end{array} \right.
$$

设 $V = \mathcal{D}(A^{\frac{1}{2}})$ , $V$ 中内积规定为 $(v_{1}, v_{2})_{V} = (A^{\frac{1}{2}}v_{1}, A^{\frac{1}{2}}v_{2})_{H}$ , $\forall v_{1}, v_{2} \in V$ . 我们取能量空间 $\mathcal{H} = V \times L^{2}(\Omega)$ 作为状态空间, 并定义线性算子 $\mathcal{A}, \mathcal{B}: \mathcal{H} \to \mathcal{H}$ 和 $\mathcal{B}_{J}: L^{2}(\Omega) \to \mathcal{H}$ :

$$\mathcal {A} [ \varphi , \psi ] ^ {\mathrm{T}} = [ \psi , - A \varphi ] ^ {\mathrm{T}}, \quad \forall [ \varphi , \psi ] ^ {\mathrm{T}} \in \mathcal {D} (\mathcal {A}) = \mathcal {D} (A) \times V,\mathcal {B} [ \varphi , \psi ] ^ {\mathrm{T}} = [ 0, - b \psi ] ^ {\mathrm{T}}, \quad \forall [ \varphi , \psi ] ^ {\mathrm{T}} \in \mathcal {H},\boldsymbol {\mathcal {B}} _ {J} \psi = [ 0, \delta_ {J} \psi ] ^ {\mathrm{T}}, \quad \forall \psi \in L ^ {2} (\Omega).$$

于是式 (10.4.2) 和式 (10.4.3) 分别可以写成 $\mathcal{H}$ 中的线性发展方程

$$\frac {\mathrm{d} Y (t)}{\mathrm{d} t} = \mathcal {A} Y (t) + \mathcal {B} Y (t), \tag {10.4.4}\frac {\mathrm{d} Y (t)}{\mathrm{d} t} = \mathcal {A} Y (t) + \mathcal {B} _ {J} u (t), \tag {10.4.5}$$

其中 $Y(t) = [y(t), \dot{y}(t)]^{\mathrm{T}}$ . 下面我们研究方程 (10.4.4) 的稳定性和方程 (10.4.5) 的能控性之间的关系，见文献 [28]. 为此我们定义集合 $G = \{x \in \Omega \mid b(x) \geqslant b_0\}$ ，其中 $b_0 > 0$ 是某个固定的常数.

定理 10.4.1 (1) 假定 $G \supset J$ ，并且方程 (10.4.5) 是精确能控的，则方程 (10.4.4) 是指数稳定的；

(2) 若 $J \sup b$ (函数 $b$ 的支集), 并且方程 (10.4.4) 是指数稳定的, 则方程 (10.4.5) 是精确能控的.

在证明这一定理之前，我们先证明一个引理.

引理10.4.1 设 $T(t)$ 是Hilbert空间 $H$ 上闭稠定耗散线性算子 $A$ 生成的 $C_0$ 压缩半群，并设 $F \in \mathcal{L}(H)$ 满足
