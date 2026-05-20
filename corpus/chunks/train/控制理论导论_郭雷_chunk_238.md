$$F: t \mapsto \left(\sin \frac {1}{2} \pi t, \cos \frac {1}{2} \pi t\right).$$

选择任一 $t$ , 譬如 $t = 1$ , 那么 $F_{*}: T_{1}(\mathbb{R}) \to T_{(1,0)}(\mathbb{R}^{2})$ 将 $X|_{t=1} = 2 \frac{\mathrm{d}}{\mathrm{d} t}$ 映为

$$
F _ {*} (X _ {t = 1}) = \left. \frac {\mathrm{d}}{\mathrm{d} t} \left[ \begin{array}{l} F _ {1} \\ F _ {2} \end{array} \right] \right| _ {t = 1} = \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] \in T _ {(1, 0)} (\mathbb {R} ^ {2}).
$$

对任一 $t$ , 我们可以这样定义 $F_{*}$ . 但显然 $\{F_{*}(X_{t}) \mid t \in \mathbb{R}\}$ 不是 $\mathbb{R}^{2}$ 上的向量场, 因为它不是处处有定义.

不难看出，如果 $F: M \to N$ 是一个微分同胚且 $X \in V(M)$ ，那么 $F_{*}(X)$ 是 $N$ 上的一个向量场，而且

$$F _ {*} (X) = J _ {F} X (\circ F ^ {- 1}), \tag {3.6.7}$$

式 (3.6.7) 是式 (3.6.5) 的一个推广.

例3.6.2 设 $\pmb{T} \in \mathrm{GL}(n, \mathbb{R})$ , $F: \mathbb{R}^n \to \mathbb{R}^n$ 定义为 $y = \pmb{T}\pmb{x}$ , 且

$$\boldsymbol {X} = \left[ v _ {1} (x), \dots , v _ {n} (x) \right] ^ {\mathbf {T}},$$

那么

$$F _ {*} (X) = J _ {F} X | _ {y = T x} = T X (T ^ {- 1} y).$$

今给一个特殊例子，设 $X = [\sin (x_1 + x_2),\exp (x_1)]^{\mathrm{T}}$ 且 $\pmb {y} = \pmb {T}\pmb{x},$ 这里

$$
\boldsymbol {T} = \left[ \begin{array}{l l} 1 & 0 \\ 1 & 1 \end{array} \right].
$$

那么

$$
\begin{array}{l} F _ {*} (X) = \left[ \begin{array}{l l} 1 & 0 \\ 1 & 1 \end{array} \right] \left. \left[ \begin{array}{c} \sin \left(x _ {1} + x _ {2}\right) \\ \mathrm{e} ^ {x _ {1}} \end{array} \right] \right| _ {y = T x} \\ = \left. \left[ \begin{array}{c} \sin (x _ {1} + x _ {2}) \\ \mathrm{e} ^ {x _ {1}} + \sin (x _ {1} + x _ {2}) \end{array} \right] \right| _ {x = T ^ {- 1} y} = \left[ \begin{array}{c} \sin y _ {2} \\ \mathrm{e} ^ {y _ {1}} + \sin y _ {2} \end{array} \right]. \\ \end{array}
$$

定义3.6.4 设 $\theta: I \to M$ 为 $M$ 上的一条曲线，这里区间 $I$ 为 $0 \in I \subset \mathbb{R}$ . 如果存在一个向量场 $X \in V(M), x_0 \in M$ ，使得

$$\frac {\mathrm{d}}{\mathrm{d} t} \theta (t) = X _ {\theta (t)}, \qquad \theta (0) = x _ {0},$$

则 $\theta(t)$ 称为 $X$ 的积分曲线且其初值为 $\theta(0) = x_0$ .

$\theta (t)$ 作为一个常微分方程的解具有以下性质：

(1) $\theta(t) \circ \theta(s) = \theta(t + s)$ ;   
(2) $\theta(-t) \circ \theta(t) = \theta(0) = \mathrm{id}$ , 这里 $\mathrm{id}$ 是恒等映射.

因此 $\theta(t)$ 相对于 $t$ 形成一个群 (假定 $\theta(t)$ 总有定义). 这个群称为由 $X$ 生成的单参数群.

为表示积分曲线对向量场的依赖，单参数群通常记作 $\phi_t^{\mathbf{Y}}(x_0)$ 。当用这个记号时，我们总假定 $t$ 属于最大的区间 $0 \in I \subset \mathbb{R}$ ，使在这个区间上积分曲线有定义。

定义3.6.5 一个向量场 $X \in V(M)$ 称为完备的，如果它完全可积，即对任一 $x_0 \in M$ 积分曲线对所有的 $t \in (-\infty, \infty)$ 有定义.

如果 $\mathbb{R}^n$ 上的一个向量场满足Lipschitz条件，即存在一个 $\gamma >0$ 使得
