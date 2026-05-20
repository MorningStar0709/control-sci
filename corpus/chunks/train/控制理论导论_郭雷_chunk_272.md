事实上，式(3.12.2)有一般性．下面的定理是一个基本关系．直接证明参见文献[14].

定理 3.12.1(Darboux) 在一个 2n 维流形 M 上，一个 2- 形式是一个辛结构，当且仅当对任一点 $p \in M$ ，存在 p 附近的一个坐标卡 $(U, (x, y))$ 使得 $\omega$ 可局部表示为

$$\omega = \sum_ {i = 1} ^ {n} \mathrm{d} x ^ {i} \wedge \mathrm{d} y ^ {i}.$$

定义3.12.2 设 $(M, \omega)$ 为一辛流形，且 $X \in V(M)$ 及 $\mu \in V^{*}(M)$ 由下式联系起来：

$$i _ {X} (\omega) \stackrel {\mathrm{def}} {=} \omega (X, \cdot) = \mu .$$

定义两个同构： $\sharp :V^{*}(M)\to V(M)$ 及 $b:V(M)\to V^{*}(M)$ 如下：

$$X = \mu^ {\flat}, \quad \text {及} \quad \mu = X ^ {\flat} \tag {3.12.3}$$

如果存在一个函数 $H$ 使得 $X = (\mathrm{d}H)^{\mathfrak{p}}$ , 那么 $H$ 称为一个Hamilton函数且 $X$ 称为由 $H$ 导出的Hamilton向量场, 记作 $X = X_{H}$ .

设 $M$ 及 $N$ 为两个流形， $F: M \to N$ 为一微分同胚， $\omega \in \Omega^k(N)$ . 那么一个导出映射 $F^*: \Omega^k(N) \to \Omega^k(M)$ 可定义如下：

$$F ^ {*} (\omega) (X _ {1}, \dots , X _ {k}) = \omega (F _ {*} (X _ {1}), \dots , F _ {*} (X _ {k})), \quad \forall X _ {1}, \dots , X _ {k} \in V (M). \tag {3.12.4}$$

下面的定理通常也称为结构不变性. 它是由冯康等创建的辛算法的基础[8].

定理 3.12.2(Liouville 定理) 设 $(M,\omega)$ 为一辛流形， $X_{H}$ 为一 Hamilton 向量场．那么

$$(\phi_ {t} ^ {X _ {H}}) ^ {*} (\omega (x)) = \omega (\phi_ {t} ^ {X _ {H}} (x)). \tag {3.12.5}$$

证明参见文献 [1].

由于辛几何只能处理偶数维的动力系统，为了给出更一般的几何结构，我们引进 Poisson 流形.

定义 3.12.3 流形 M 上的一个 Poisson 括号是一个光滑映射 $\{\cdot,\cdot\}:C^{r}(M)\times C^{r}(M)\to C^{r}(M)$ ，它带有以下的基本性质：

P1. (双线性性) $\{cF + dP, H\} = c\{F, H\} + d\{P, H\}$ , $\{F, cH + dP\} = c\{F, H\} + d\{F, P\}$ , 其中常数 $c, d \in \mathbb{R}$ ;

P2. (Leibniz 规则) $\{F, GH\} = \{F, G\} H + G\{F, H\}$ ;

P3. (反对称) $\{F, H\} = -\{H, F\}$ ;

P4. (Jacobi 等式) $\{F, \{G, H\}\} + \{G, \{H, F\}\} + \{H, \{F, G\}\} = 0$ .

一个流形 $M$ 带上一个 Poisson 括号 $\{\cdot, \cdot\}$ 称为一个 Poisson 流形， Poisson 括号在 $M$ 上定义了一个 Poisson 结构.

要说明 Poisson 流形更一般，我们给出以下结果：

命题3.12.2 设 $(M, \omega)$ 为一辛流形，则存在一个Poisson括号使 $M$ 成为一个Poisson流形.

证明 对任意两个函数 $f, g \in C^r(M)$ , 定义一个 Poisson 括号如下:

$$\{f, g \} = \omega (X _ {f}, X _ {g}), \quad \forall f, g \in C ^ {\tau} (M). \tag {3.12.6}$$

读者可自行验证它确为一个 Poisson 括号.

定义3.12.4 设 $M$ 为一 Poisson 流形。一个光滑的实函数 $C: M \to \mathbb{R}$ 称为一个 Casimir 函数，如果 $C$ 和任何函数的 Poisson 括号均为零，即 $\{C, H\} = 0, \forall H \in C^r(M)$ .

对给定的一个动力系统，当我们寻找作为 Lyapunov 函数的 Hamilton 函数时，Casimir 函数会给我们更多的自由度，因为对一个 Casimir 函数 C，我们总有 $X_{H} = X_{H+C}$ .

定义3.12.5 设 $M$ 为一Poisson流形， $H: M \to \mathbb{R}$ 为一光滑函数。由 $H$ 生成的向量场 $V_{H}$ 是 $M$ 上唯一的向量场，满足

$$V _ {H} (F) = \{F, H \} = - \{H, F \}, \quad \forall F: M \rightarrow \mathbb {R}.$$

命题3.12.3 设 $M$ 为一Poisson流形， $F, H \in C^{r}(M)$ ，其相应的Hamilton
