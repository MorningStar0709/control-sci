证明 充分性. 当状态反馈阵 $K$ 中第 $i$ 行 $j$ 列元 $k_{ij} \neq -\infty$ 时, $K$ 使系统 (11.5.1) 的事件图中增加了从 $x_i$ 到 $u_j$ 间的位置, 位置中数字为 $k_{ij}$ . 类似于上节, 当 $X_i$ 中某 $x_j$ 到 $u_r$ 间有位置时, 在系统 (11.5.1) 的凝网中画一弧 $X_i u_r$ , 否则不画, 这就得到了系统 (11.6.1) 的凝网. 令 $K$ 的行按 $X_i$ 分块, 列按一列一块, 取 $K$ 为对角块形, 每个对角块 $K_{ii}$ 中仅含一个元 $k_{si} \neq -\infty$ , 则 $K$ 仅形成了 $X_i u_i$ 弧, $1 \leqslant i \leqslant \omega$ . 由条件 (1), $u_i$ 与 $X_i$ 间强连通, 因此可进一步凝成一个点. 因为系统 (11.5.1) 的凝网具有标准序, 而由条件 (2), $X_i$ 经弧 $X_i u_i$ 后没有弧 $u_i X_j$ , $1 \leqslant j < i \leqslant \omega$ , 能形成 $X_i$ 到 $X_j, j < i$ , 的路, 所以系统 (11.6.1) 的凝网仍具有标准序, 于是仍有 $\omega$ 个 $X_i$ , 不会减少, 本节定理 11.6.1 证明了: 对每个 $i$ , $A \oplus KB$ 的周期 $\tilde{\lambda}_i$ 是 $k_{si}$ 的连续增函数, 取值在 $[\lambda_i, +\infty)$ 中, 因此系统 (11.5.1) 的周期能配置.

必要性. 令 $\tilde{\lambda}_i$ 取 $\omega$ 个不同的值, 为配置这些值系统 (11.6.1) 的凝网中必有 $\omega$ 个 $X_i$ . 为配置每一个周期, $K$ 必须形成 $X_i$ 到 $X_i$ 的新回路. 因此必然存在一个 $u_r$ 下标 $r$ 的编号次序, 使得条件 (1) 满足, 且有 $K$ 形成的 $X_i u_i$ 弧, $1 \leqslant i \leqslant \omega$ . 这样, 式 (11.6.1) 的凝网中 $u_i$ 与 $X_i$ 强连通, 并可进一步凝成一个点. 易知凝网中没有回路, 且一定存在标准序 (由于 $K$ 的作用, 系统 (11.6.1) 的新凝网的标准序可以与系统 (11.5.1) 的凝网原来随便取的标准序不同), 在这序下没有 $X_i X_j$ 弧, $1 \leqslant j < i \leqslant \omega$ . 因为 $X_i$ 与 $u_i$ 已凝成一点, 所以也就没有 $u_i X_j$ 弧, $1 \leqslant j < i \leqslant \omega$ . 条件 (2) 满足.

极大代数 $D$ 的运算特性是 $\oplus$ 为取极大，乘为普通加，而Petri网运行特征是并行“位置”取极大，串行“位置”取和。它们之间的这种对应，正好是两种描述可对应交换的基础，同时也使 $A \oplus KB$ 形成的系统(11.6.1)的凝网恰如定理11.6.2证明中所示。极大代数 $D$ 的这种特性使它成为联系离散的Petri网，DEDS与连续元素矩阵 $A, B, C$ 构成的系统(11.5.1)之间的桥梁。

由于从系统 (11.5.1) 的具有标准序的强凝网可推出式 (11.5.2)，类似于定理 11.5.2 的证明，可由定理 11.6.2 得到矩阵语言描述的如下定理：

定理 11.6.3 $^{[11]}$ 系统 (11.5.1) 能用状态反馈配置周期的充要条件是：A, B 等价于 $\hat{A}, \hat{B}$ 这里

$$
\widehat {\boldsymbol {A}} = \left[ \begin{array}{c c c c} \boldsymbol {A} _ {i _ {1}} & \boldsymbol {A} _ {i _ {1} i _ {2}} & \dots & \boldsymbol {A} _ {i _ {1} i _ {\omega}} \\ \phi & \boldsymbol {A} _ {i _ {2}} & \dots & \boldsymbol {A} _ {i _ {2} i _ {\omega}} \\ \vdots & \vdots & & \vdots \\ \phi & \phi & \dots & \boldsymbol {A} _ {i _ {\omega}} \end{array} \right], \quad \widehat {\boldsymbol {B}} = \left[ \begin{array}{c c c c} & \boldsymbol {B} ^ {*} \\ B _ {1 1} & B _ {1 2} & \dots & B _ {1 \omega} \\ \phi & B _ {2 2} & \dots & B _ {2 \omega} \\ \vdots & \vdots & & \vdots \\ \phi & \phi & \dots & B _ {\omega \omega} \end{array} \right], \tag {11.6.6}
$$
