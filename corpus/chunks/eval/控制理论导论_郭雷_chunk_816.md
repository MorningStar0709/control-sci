$$\Gamma_ {1} u = \int_ {t} ^ {t _ {1}} B ^ {*} T ^ {*} (s - t) Q \int_ {t _ {0}} ^ {s} T (s - \tau) B u (\tau) \mathrm{d} \tau \mathrm{d} s \quad t _ {0} \leqslant t \leqslant t _ {1},\Gamma_ {2} u = \Lambda^ {*} (t _ {1}) G \Lambda (t _ {1}) u,\Gamma_ {3} x _ {0} = B ^ {*} T ^ {*} (t _ {1} - s) G T (t _ {1} - t _ {0}) x _ {0}, \quad t _ {0} \leqslant s \leqslant t _ {1},\Gamma_ {4} x _ {0} = \int_ {t} ^ {t _ {1}} B ^ {*} T ^ {*} (s - t) Q T (s - t _ {0}) x _ {0} \mathrm{d} s, \quad t _ {0} \leqslant t \leqslant t _ {1},$$

那么 $J(u; t_0, t_1, x_0)$ 可以写成

$$J (u; t _ {0}, t _ {1}, x _ {0}) = ((R + \Gamma_ {1} + \Gamma_ {2}) u, u) _ {L ^ {2} (t _ {0}, t _ {1}; U)} + 2 (u, (\Gamma_ {3} + \Gamma_ {4}) x _ {0}) _ {L ^ {2} (t _ {0}, t _ {1}; U)} + \alpha .$$

但显然 $\Gamma_1, \Gamma_2$ 是非负对称的，并且 $R$ 是正定的，故控制

$$u ^ {0} = - \left(R + \Gamma_ {1} + \Gamma_ {2}\right) ^ {- 1} \left(\Gamma_ {3} + \Gamma_ {4}\right) x _ {0} \tag {10.6.13}$$

使得泛函 $J(\cdot ;t_0,t_1,x_0)$ 在 $L^2 (t_0,t_1;U)$ 上达到极小．这证明了关于性能指标 $J(\cdot ;t_0,$ $t_1,x_0)$ 的最优控制的存在性．从式(10.6.13）可得

$$
\begin{array}{l} R u ^ {0} = - \left(\Gamma_ {1} + \Gamma_ {2}\right) u ^ {0} - \left(\Gamma_ {3} + \Gamma_ {4}\right) x _ {0} \\ = - B ^ {*} \left(\int_ {t} ^ {t _ {1}} T ^ {*} (s - t) Q x ^ {0} (s) \mathrm{d} s + T ^ {*} \left(t _ {1} - t\right) G x ^ {0} \left(t _ {1}\right)\right), \\ \end{array}
$$

即式 (10.6.12) 成立.

对于 $t \in [t_0, t_1)$ , 如果我们定义线性算子 $P(t): H \to H$ .

$$P (t) x = \int_ {t} ^ {t _ {1}} T ^ {*} (s - t) Q x ^ {0} (s; t, x) \mathrm{d} s + T ^ {*} (t _ {1} - t) G x ^ {0} (t _ {1}; t, x), \tag {10.6.14}$$

其中 $x^0 (s;t,x)$ 表示关于性能指标 $J(\cdot ;t,t_1,x)$ 的最优控制，则最优控制 $u^0 (t)$ 可以写成反馈形式

$$\boldsymbol {u} ^ {0} (t) = - R ^ {- 1} B ^ {*} P (t) x ^ {0} (t), \quad t _ {0} \leqslant t \leqslant t _ {1}. \tag {10.6.15}$$

另一方面，对于任意 $x, y \in H$ 和 $t \in [t_0, t_1)$ ，有

$$(P (t) x, y) = \int_ {t} ^ {t _ {1}} \left(Q x ^ {0} (s; t, x), T (s - t) y\right) d s + \left(G x ^ {0} \left(t _ {1}; t, x\right), T \left(t _ {1} - t\right) y\right)= \int_ {t} ^ {t _ {1}} \left[ \left(Q x ^ {0} (s; t, x), x ^ {0} (s; t, y)\right) + \left(R u ^ {0} (s), v ^ {0} (s)\right) \right] d s+ \left(G x ^ {0} (t _ {1}; t, x), x ^ {0} (t _ {1}; t, y)\right),$$

由此我们得到

$$(P (t) x, x) = m \left(t, t _ {1}, x\right). \tag {10.6.16}$$

于是 $P(t)$ 在 $H$ 上是非负对称的.

引理10.6.2 在上述记号下，我们有

(1) $P(t)$ 在 $[t_0, t_1)$ 上是单调递减的；  
(2) $P(t)$ 在 $[t_0, t_1)$ 上是一致有界的；  
(3) 对于固定的 $x \in H$ , $m(t, t_1, x)$ 是 $[t_0, t_1)$ 上 $t$ 的连续函数.

证明 我们已经看到， $(P(t)x, x) = m(t, t_1, x)$ ，并且从引理 10.6.1 可得

$$m (t, t _ {1}, x) \geqslant m (t ^ {\prime}, t _ {1}, x), \quad \forall t \leqslant t ^ {\prime}.$$
