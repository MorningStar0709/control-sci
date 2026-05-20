图11.9.1中 $-,|$ 表示变迁，表示一个初始标识。 $p_{n + m + 5}$ 中初始标识为 $N + 1$ 个， $p_{2n + 2m + 9}$ 中初始标识为2个，其余初始标识数为1或0。图中未标出的 $u,v$ 值均为 $u = v = 1$ ，未标出的延迟时间为0，非零的延迟时间均标在位置旁边。

图中 $N \stackrel{\mathrm{def}}{=} \lceil \tilde{t}_r / \tilde{t}_1 \rceil, k \stackrel{\mathrm{def}}{=} \lfloor M / (N + 1) \rfloor$ ; 为了叙述简单, 不妨设 $\tilde{t}_1 | \tilde{t}_r, (N + 1) | M$ . $M$ 个轧件分为 $k$ 个小批, 每批为 $N + 1$ 个轧件, 当第一个轧件度过 $\tilde{t}_r$ 的冷却时间后, 可连续加工后面 $N$ 个轧件, 不妨设 $n \geqslant m \geqslant N$ , 这 $N + 1$ 个轧件可串行存在 $m$ 个存储器与轧机上, 待第一个轧件冷却结束, 把全部轧件串行移到 $n$ 个存储器与轧机上 (这个反向倒移过程忽略过去, 不在图中表示, 所有移动过程的时间也看作零), 然后进行第二次加工.

ETEG 有很强的描述与仿真能力，但分析能力相对弱些。人们在探讨相应的代数模型与方法，希望有可能得到更强一些的分析与控制能力。本节介绍文献[19]

提出，并由文献 [30] 改进的建模过程.

令 $\epsilon \stackrel{\mathrm{def}}{=} -\infty, w \stackrel{\mathrm{def}}{=} +\infty, \tilde{R} = \mathbb{R} \cup \varepsilon \cup w,$ 其中 $\mathbb{R}$ 是实数集. 设 $\mathbb{N}$ 是正整数集,

定义 11.9.1 如果 $\langle s\rangle = \langle s_{0}, s_{1}, \cdots, s_{k}, \cdots \rangle, \forall k \in N \cup \{0\}, s_{k} \leqslant s_{k+1}, s_{k} \in \widetilde{R}$ ，则 $\langle s\rangle$ 称为时间序列.

设 $\langle s\rangle$ 的全体为 S，位置序列 $\langle p\rangle_{i}\stackrel{\operatorname{def}}{=} \langle\tilde{p}_{0},\tilde{p}_{1},\cdots,\tilde{p}_{k},\cdots\rangle\in S$ 表示位置 $p_{i}$ 的时间序列，其中 $\tilde{p}_{k}$ 表示第 k 个标志到达的时刻；变迁序列 $\langle t\rangle_{i}\stackrel{\operatorname{def}}{=} \langle\tilde{t}_{0},\tilde{t}_{1},\cdots,\tilde{t}_{k},\cdots\rangle\in S$ 表示变迁 $t_{i}$ 的时间序列，其中 $\tilde{t}_{k}$ 表示第 k 次激发的时刻.

定义 11.9.2 $^{[19]}$ 定义 S 上的函数 (或称为算子) 如下:

(1) $[z^{-k}]$ 是右移函数， $[z^{-k}] \circ \langle s \rangle = \langle \varepsilon, \cdots, \varepsilon, s_0, s_1, \cdots \rangle, k \in \mathbb{N} \cup \{0\}$ ，共有 $k$ 个 $\varepsilon$ ;  
(2) $[z^k]$ 是左移函数， $[z_k] \circ \langle s \rangle = \langle s_{k-1}, s_k, \cdots \rangle, k \in \mathbb{N} \cup \{0\}$ ;  
(3) $[\nabla^k]$ 是复制函数， $[\nabla^k] \circ \langle s \rangle = \langle s_0, \dots, s_0, s_1, \dots, s_1, \dots \rangle, k \in \mathbb{N}$ ，每个复制 $k$ 个；  
(4) $[r]$ 是加函数， $[r] \circ \langle s \rangle = \langle s_0 + r, s_1 + r, \cdots \rangle, r \in \tilde{R};$   
(5) $[\Delta]$ 是抽样函数， $[\Delta^{k}]\circ\langle s\rangle=\langle s_{k-1},s_{2k-1},\cdots\rangle,k\in\mathbb{N}$ ，每 k 个抽取最后一个并组成一个新序列.

令
