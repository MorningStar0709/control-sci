$$D _ {F} (s) = D _ {\varepsilon} (s) D (s) + N _ {\varepsilon} (s) N (s) \tag {11.186}$$

且常称(11.186)为广义达芬廷（Diophantine）方程。

② 证明 $G_{o}(s)\pmb{t}_{1}$ 和 $G_{o}(s)$ 具有相同的 $\nu_{0}$ 已知 $G_{o}(s) = D_{oL}^{-1}(s)N_{oL}(s)$ 为不可简约 MFD， $\nu$ 为 $D_{oL}(s)$ 的最大行次数，也即是 $G_{o}(s)$ 的不可简约实现的能观测性指数。于是，由此可得 $G_{o}(s)\pmb{t}_{1} = D_{oL}^{-1}(s)N_{oL}(s)\pmb{t}_{1}$ ，且 $\Delta[G_{o}(s)] = k_{1}\Delta[G_{o}(s)\pmb{t}_{1}] = \det D_{oL}(s)$ 意味着 $\{D_{oL}(s), N_{oL}(s)\pmb{t}_{1}\}$ 也为左互质。从而， $G_{o}(s)\pmb{t}_{1}$ 的不可简约实现的能观测性指数也为 $\nu$ 。表明 $G_{o}(s)\pmb{t}_{1}$ 和 $G_{o}(s)$ 具有相同的 $\nu_{o}$

③ 证明当 $m \geqslant \nu - 1$ 时可任意配置 $n + m$ 个闭环极点。为此，表

$$D (s) = D _ {n} s ^ {n} + \dots + D _ {1} s + D _ {0}, D _ {n} \neq 0 \tag {11.187}N (s) = N _ {s} s ^ {n} + \dots + N _ {1} s + N _ {0} \tag {11.188}D _ {e} (s) = D _ {e m} s ^ {m} + \dots + D _ {e 1} s + D _ {e 0} \tag {11.189}N _ {e} (s) = N _ {e m} s ^ {m} + \dots + N _ {e 1} s + N _ {e 0} \tag {11.190}D _ {F} (s) = F _ {n + m} s ^ {n + m} + \dots + F _ {1} s + F _ {0} \tag {11.191}$$

那么，将(11.187)-(11.191)代入(11.186)，并由等式两边 $s^i (i = 0,1,\dots ,n + m)$ 的系数应相等而可导出如下的矩阵方程：

$$\left[ D _ {c 0} N _ {c 0} \mid D _ {c 1} N _ {c 1} \mid \dots \mid D _ {c m} N _ {c m} \right] S _ {m} = \left[ F _ {0} F _ {1} \dots F _ {n + m} \right] \tag {11.192}$$

其中 $(q + 1)(m + 1) \times (n + m + 1)$ 系数矩阵 $S_{\bullet}$ 为：

$$
S _ {n} = \underbrace {\left[ \begin{array}{c c c c c c c} D _ {0} & D _ {1} & \cdots & D _ {n} & 0 & \cdots & 0 \\ N _ {0} & N _ {1} & \cdots & N _ {n} & 0 & \cdots & 0 \\ \hline 0 & D _ {0} & \cdots & D _ {n - 1} & D _ {n} & 0 & \cdots & 0 \\ 0 & N _ {0} & \cdots & N _ {n - 1} & N _ {n} & 0 & \cdots & 0 \\ \hline & & & \vdots & & \\ \hline 0 & \cdots & 0 & D _ {0} & \cdots & D _ {n - m} & \cdots & D _ {n} \\ 0 & \cdots & 0 & N _ {0} & \cdots & N _ {n - m} & \cdots & N _ {n - m} \end{array} \right]} _ {n + m + 1} (q + 1) (m + 1) \tag {11.193}
$$

并且，一旦 $n + m$ 个期望的闭环极点给定，相应地 $D_{F}(s)$ 就随之确定，从而方程(11.192)中 $\{F_{i}, i = 0, 1, \dots, n + m\}$ 为已知。这表明， $\bar{C}(s)$ 存在而可任意配置极点的问题，即等价于方程（11.192）有解的问题。在代数方程论中已经证明，当 $S_{m}$ 为列满秩也即 $\operatorname{rank} S_{m} = n + m + 1$ 时，解 $\{D_{ci}, N_{ci}, j = 0, 1, \dots, m\}$ 存在。进而，由已知 $m \geqslant \nu - 1$ ，且 $G_{o}(s)t_{1}$ 和 $G_{o}(s)$ 具有相同的 $\nu$ ，所以此时 $S_{m}$ 的 $N$ 块行中线性无关的行总数必为 $n$ 。另一方面， $D_{a} (\alpha = 0, 1, \dots, n)$ 为标量，且所有 $m + 1$ 个 $D$ 行必为线性无关。于是可知，在 $m \geqslant \nu - 1$ 条件下，必有 $\operatorname{rank} S_{m} = n + m + 1$ ，即存在 $\bar{C}(s)$ 而可任意配置 $n + m$ 个极点。并且， $C(s) = t_{1}\bar{C}(s)$ 为真的。

④ 类似地，也可证明，当 $m \geqslant \mu - 1$ 时，也存在 $\bar{C}(s)$ 而可任意配置 $n + m$ 个极点。
