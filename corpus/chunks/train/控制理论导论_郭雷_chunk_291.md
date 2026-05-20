# 条件期望

设 $(\Omega, \mathcal{F}, P)$ 为概率空间， $A \in \mathcal{F}, B \in \mathcal{F}, PB > 0$ 。给定 $B$ 时 $A$ 的条件概率定义为 $P(A|B) = \frac{P(A \cap B)}{PB}$ ，从几何图形上看

![](image/920f95498994bd148140ed5907a01286dd204e770ea51158977a14513f385d51.jpg)

<details>
<summary>text_image</summary>

A
A∩B
B
</details>

它的含义非常直观易懂.

固定 $B, A$ 在 $\mathcal{F}$ 内任意变化时得到集合函数

$$P ^ {B} (A) \stackrel {\mathrm{def}} {=} P (A | B).$$

显然 $P^B(A)$ 也是定义在 $\mathcal{F}$ 上的概率测度，有了测度，就可以定义相对 $P^B(A)$ 的积分： $E^B\xi \stackrel{\mathrm{def}}{=} \int \xi \mathrm{d}P^B$ ，它就是给定 $B$ 时， $\xi$ 的条件期望。

注意到给定 $B^{c}$ , 类似地可定义 $P^{B^{c}}(A)$ 及 $E^{B^{c}}\xi$ , 而给定集合 $B$ , 实际上就是给定了 $\sigma$ -代数 $\mathcal{F}_{1} \stackrel{\mathrm{def}}{=} \{\Omega, \phi, B, B^{c}\}$ .

所以我们可以定义给定 $\sigma$ -代数 $\mathcal{F}_1$ 时的条件概率

$$P ^ {\mathcal {F} _ {1}} (A) \stackrel {{\mathrm{def}}} {{=}} (P ^ {B} A) I _ {B} + (P ^ {B ^ {c}} A) I _ {B ^ {c}},$$

以及给定 $\mathcal{F}_1$ 时 $\xi$ 的条件期望

$$E ^ {\mathcal {F} _ {1}} \xi \stackrel {{\mathrm{def}}} {{=}} (E ^ {B} \xi) I _ {B} + (E ^ {B ^ {c}} \xi) I _ {B ^ {c}}.$$

但这里的 $\sigma$ -代数是 $\mathcal{F}$ 的一个特殊的子 $\sigma$ -代数，它仅由集合 $B$ 生成。今后我们要在一般的 $\sigma$ -代数 $\mathcal{F}_1(\subset F)$ 的条件下定义条件期望。为此我们要用如下定理：

Radon-Nikodym 定理 设 $\phi(A)$ 是定义在 $\sigma$ -代数 $\mathcal{F}_1$ 上的集合函数, 它 $P$ -连续, 即当 $PA \to 0$ 时, $\phi(A) \to 0$ , 并且 $\sigma$ -可加, 即对互不相交的 $A_i \in \mathcal{F}_1, i = 1,2,\cdots$ , 成立 $\phi\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} \phi(A_i)$ , 那么必存在唯一 (精确到等价类) $\mathcal{F}_1$ 可测函数 $\eta$ , 使 $\phi(A)$ 是 $\eta$ 的一个不定积分

$$\phi (A) = \int_ {A} \eta \mathrm{d} P = E (\eta I _ {A}), \quad \forall A \in \mathcal {F} _ {1}.$$

设 $\xi$ 是定义在 $(\Omega, \mathcal{F}, P)$ 上的一个随机变量， $E\xi$ 有意义。那么定义在 $\mathcal{F}_1(\subset \mathcal{F})$ 上的集合函数 $\phi(A) \stackrel{\mathrm{def}}{=} \int_A \xi \mathrm{d}P$ 为 $P$ -连续， $\sigma$ -可加。所以，据 Radon-Nikodym 定理，存在唯一（精确到等价类，即只可能在零概率集上有差异）对 $\mathcal{F}_1$ 可测的函数（随机变量），记为 $E^{\mathcal{F}_1}\xi$ 或 $E(\xi|\mathcal{F}_1)$ 使

$$\int_ {A} \xi \mathrm{d} P = \int_ {A} E ^ {\mathcal {F} _ {1}} \xi \mathrm{d} P, \quad \text { a.s. } \tag {4.1.23}$$

$E^{\mathcal{F}_1}\xi (E(\xi |\mathcal{F}_1))$ 叫给定 $\mathcal{F}_1$ 时 $\xi$ 的条件期望.

当 $\xi = I_A, A \in \mathcal{F}$ 时，记 $P^{\mathcal{F}_1}A \stackrel{\mathrm{def}}{=} E^{\mathcal{F}_1}I_A, P^{\mathcal{F}_1}A$ 或 $P(A|\mathcal{F}_1)$ 叫给定 $\mathcal{F}_1$ 时， $A$ 的条件概率.
