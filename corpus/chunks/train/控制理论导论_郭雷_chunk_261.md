定义3.10.7 一个流形 $M$ 称为可定向的，如果存在一个 $C^r$ 的 $n-$ 形式 $\omega$ 使得

$$\omega (p) \neq 0, \quad \forall p \in M.$$

最后, 我们定义外微分. 我们已经知道对于一个光滑函数 $h \in C^r(M) = \Omega^0(M)$ , 其微分 $\mathbf{d}: h \mapsto \mathrm{d}h$ 是一个从 $\Omega^0(M)$ 到 $\Omega^1(M)$ 的 $\mathbb{R}$ 线性映射. 一般地, 我们定义一个 $\mathbb{R}$ 线性映射 $d: C^k(M) \to C^{k+1}(M)$ 如下, 它称为外微分: 设 $\omega = a(x)\mathrm{d}x^{i_1} \wedge \cdots \wedge \mathrm{d}x^{i_k}$ , 那么

$$\mathrm{d} \omega = \mathrm{d} a (x) \wedge \mathrm{d} x ^ {i _ {1}} \wedge \dots \wedge \mathrm{d} x ^ {i _ {k}}. \tag {3.10.10}$$

因为 d 是 R 线性的，上式唯一地定义了这个映射.

定理 3.10.1 (1)

$$\mathrm{d} ^ {2} \omega = 0; \tag {3.10.11}$$

(2) 设 $\theta \in \Omega^r(M)$ 及 $\omega \in \Omega^s(M)$ . 那么

$$\mathrm{d} (\theta \wedge \omega) = \mathrm{d} \theta \wedge \omega + (- 1) ^ {r} \theta \wedge \mathrm{d} \omega . \tag {3.10.12}$$

证明 不失一般性，我们可假定 $\omega$ 只有一项，即 $\omega = a(x)\mathrm{d}x^{i_1}\wedge \dots \wedge \mathrm{d}x^{i_s}$ 那么

$$\mathrm{d} ^ {2} \omega = \sum_ {j, k \neq i _ {1}, \dots , i _ {s}} \frac {\partial^ {2} a (x)}{\partial x ^ {j} \partial x ^ {k}} \mathrm{d} x ^ {k} \wedge \mathrm{d} x ^ {j} \wedge \mathrm{d} x ^ {i _ {1}} \wedge \dots \wedge \mathrm{d} x ^ {i _ {s}}.$$

由 $\frac{\partial^2a(x)}{\partial x^j\partial x^k} = \frac{\partial^2u(x)}{\partial x^k\partial x^j}$ 及 $\mathrm{d}x^{k}\wedge \mathrm{d}x^{j} = -\mathrm{d}x^{j}\wedge \mathrm{d}x^{k}$ ，立即可得式(3.10.11）.

要证明式 (3.10.12)，设 $\theta = a(x)\mathrm{d}x^{i_1}\wedge \dots \wedge \mathrm{d}x^{i_r}$ 及 $\omega = b(x)\mathrm{d}x^{j_1}\wedge \dots \wedge \mathrm{d}x^{j_s}$ . 假定

$$i ^ {p} \neq j ^ {q}, \quad p = 1, \dots , r, \quad q = 1, \dots , s.$$

否则，式(3.10.12)的两边均为零，等式显然成立．那么
