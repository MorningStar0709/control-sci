定义8.1.5 (1)系统(8.1.1)称在 $x_0\in M$ 能接近，如果 $R(x_0)$ 包含一个非空开集．系统称为能接近的，如果它在每一点 $x\in M$ 能接近；

(2) 系统 (8.1.1) 称在 $x_0 \in M$ 强能接近，如果对每一点 $T > 0, R(x_0, T)$ 包括一个非空开集。系统称为强能接近的，如果它在每一点 $x \in M$ 强能接近。

定理8.1.2 (1)对系统(8.1.1)设能控性秩条件在 $x_0\in M$ 满足，即

$$\operatorname{rank} (\mathcal {F} (x _ {0})) = n, \tag {8.1.6}$$

那么它在 $x_0$ 点能接近，并且对每个 $T > 0$ ，能达集

$$\bigcup_ {0 \leqslant t \leqslant T} R (x _ {0}, t) \tag {8.1.7}$$

有非空内点；

(2) 如果系统是解析的，那么能控性秩条件 (8.1.6) 是使系统在 $x_0$ 点能接近的充要条件；  
(3) 设系统是解析的且能控性秩条件 (8.1.6) 成立, 那么内点集在 $\bigcup_{0 \leqslant t \leqslant T} R(x_0, t)$ 中稠.

证明 (1) 回忆定理 8.1.1 的证明，显然在式 (8.1.4) 中所有 $t_i, i = 1, \dots, n$ 可选为正的。因此 $\pi_n(V_n)$ 是一个非空开集，且它包含于 $R(x_0)$ 。而且所有的 $t_i$ 可以选择得足够小，从而对任给 $T > 0$ ，我们可假定 $\| t\| < T$ ，即式(8.1.6)包括一个非空内点集；

(2) 我们只要证明必要性. 设

$$\operatorname{rank} (\mathcal {F} | _ {x _ {0}}) = k < n,$$

且 $p$ 为 $x_0$ 的能达集的一个内点。于是存在 $p$ 点的一个邻域，记作 $V_p$ ，使得 $V_p \subset R(x_0)$ 。如在证明命题8.1.2中所说的那样， $\operatorname{rank}\{\mathcal{F}\}$ 在 $R(x_0)$ 上均相等，因此 $\operatorname{rank}\{\mathcal{F}|_x\} = k, \forall x \in V_p$ 。利用 Frobenius 定理则知 $\mathcal{I}(\mathcal{F}, p) \cap V_p$ 是一个 $k$ 维子流形。但

$$\mathcal {I} (\mathcal {F}, p) = \mathcal {I} (\mathcal {F}, x _ {0}),$$

且

$$R (x _ {0}) \subset \mathcal {I} (\mathcal {F}, x _ {0}).$$

于是

$$V _ {p} = R (x _ {0}) \cap V _ {p} \subset \mathcal {I} (\mathcal {F}, p) \cap V _ {p} \neq V _ {p},$$

这导致矛盾；

(3) 设式 (8.1.6) 成立. 首先我们可找到 $F$ 的一个有限集 $D$ 使得

$$\dim (D _ {L A} (x _ {0})) = n. \tag {8.1.8}$$

因为 $\operatorname{rank}(\mathcal{F}(x_{0}))=n,$ 故存在 n 个向量场 $Y_{i}\in\mathcal{F}, i=1,\cdots,n,$ 它们在 $x_{0}$ 点线性无关. 现在由于每一个 $Y_{i}$ 可由 F 中的向量场经 Lie 括号得到，故存在有限个向量场

$$D = \{X _ {1}, \dots , X _ {k} \} \subset F,$$

使得式 (8.1.8) 成立. 不失一般性, 可设 $F = D$ . 将 $F$ 张成对称集得

$$\pm F = \left\{X _ {1}, \dots , X _ {k}, - X _ {1}, \dots , - X _ {k} \right\}.$$

选

$$t = \left(t _ {1}, t _ {2}, \dots , t _ {m}\right) \in \mathbb {R} _ {+} ^ {m}, \quad 0 \leqslant m < \infty ,$$

及

$$X _ {i _ {1}}, X _ {i _ {2}}, \dots , X _ {i _ {m}} \in \pm F,$$

于是对 t 所有可能的选择及 $i=(i_{1},i_{2},\cdots,i_{m})$ ，我们构造集合

$$R ^ {*} (x _ {0}) = \bigcup_ {i, t} \phi_ {t _ {1}} ^ {X _ {i _ {1}}} \phi_ {t _ {2}} ^ {X _ {i _ {2}}} \dots \phi_ {t _ {m}} ^ {X _ {i _ {m}}} (x _ {0}) := \bigcup_ {i, t} \phi_ {i} (t, x _ {0}),$$

这是 $\pm F$ 由 $x_0$ 出发的能达集. 因为 $\phi_t^{-X}(x_0) = \phi_{-t}^X (x_0)$ , 所以我们可等价地表示

$$\varphi_ {i} (t, x _ {0}) = \phi_ {t _ {1}} ^ {X _ {i _ {1}}} \phi_ {t _ {2}} ^ {X _ {i _ {2}}} \dots \phi_ {t _ {m}} ^ {X _ {i _ {m}}} (x _ {0}),$$
