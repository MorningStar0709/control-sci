定义 11.10.3 在 $G(S)$ 中，把 $u_{1},\cdots,u_{\eta}$ 合并为一点 u、把 $y_{1},\cdots,y_{p}$ 合并为一点 y，相应的弧也合并，所得弧不定义权重，此图称为 S 的简图，记 $G_{0}(S)$ .

$S$ 有 $|I|$ 个线性子系统 $S_{\tau}$

$$
\left\{ \begin{array}{l} \boldsymbol {x} (k + 1) = \boldsymbol {A} _ {r} \boldsymbol {x} (k) \vee \boldsymbol {B} \boldsymbol {u} (k), \\ \boldsymbol {y} (k) = \boldsymbol {C} \boldsymbol {x} (k), \quad r \in I. \end{array} \right. \tag {11.10.2}
$$

当 $x_{i}$ 在上述 $|I|$ 个子系统中全部结构能达时，称系统 $S$ 的 $x_{i}$ 为结构能达的。当系统 $S$ 的所有 $x_{i}, 1 \leqslant i \leqslant n$ ，结构能达时，称系统 $S$ 为结构能达的。结构能观测性可类似定义。关于结构能达能观测性的判据，只需把11.5节关于 $(A, B, C)$ 的判据用到每一个 $(A_{r}, B, C)$ 上，不详述。基于 $S$ 的结构能达能观测性，也能得到类似于11.5节的 $S$ 的标准结构，详参见文献[25]。这部分拓广是比较容易的。

关于分别能达与上限能观测的定义，类似于11.5节，不详述。但判据就不同了，显示出非线性DEDS的复杂性。下面来详述。

定义 11.10.4 N 步能达点 t 满足条件:

(1) 从 $u$ 到 $t$ 至少有一条长为 $N$ 的 $r$ 色路， $\forall r \in I$ ;

(2) 所有上述各条路中， $t$ 的上邻点 (即以 $t$ 为终点的弧的起点) 均为 $N - 1$ 步能达点.

由定义易知，对于系统 $S$ ，总存一个 $N_0'(\leqslant n)$ ，当 $N \leqslant N_0'$ 时有 $N$ 步能达点；当 $N > N_0'$ 时没有 $N$ 步能达点.

定理 11.10.1 $^{[14]}$ 系统 S 的 $x_{t}$ 为分别能达分量的充要条件是存在一个 $N, 0 \leqslant N < n$ ，使得 t 为 $G_{0}(S)$ 中的 N 步能达点.

由上限能观测的定义及式 (11.10.1) 易知，当且仅当存在一个 $N$ ，使方程

$$\boldsymbol {y} (N) = C F ^ {N} (\boldsymbol {x} (0)) \tag {11.10.3}$$

的解中 $x_{t}(0)$ 均有上限时， $x_{t}$ 为上限能观测分量，这里

$$F ^ {N} (\pmb {x} (0)) = \underbrace {\bigwedge_ {r _ {N} \in I} \left(\pmb {A} _ {r _ {N}} \bigwedge_ {r _ {N - 1} \in I} \left(\pmb {A} _ {r _ {N - 1}} \cdots \bigwedge_ {r _ {1} \in I} (\pmb {A} _ {r _ {1}} \pmb {x} (0)) \dots\right)\right)} _ {N \text {个} \bigwedge_ {r _ {i} \in I}}.$$

N = 0 时表示 $x(0)$ .

定义11.10.5 在图 $G_0(S)$ 中，点 $l$ 称为点 $t$ 的 $N$ 步出口，是指

(1) 对每颜色， $t$ 到 $l$ 至少有长为 $N$ 的一条路；  
(2) 在上述每种颜色的一条路中， $l$ 的上邻点均是 $t$ 的 $N - 1$ 步出口.

我们规定 $N = 0$ 时， $t$ 就是 $t$ 的 0 步出口。于是用归纳递推法可找出 $t$ 的全部 $N$ 步出口。此外，这里的“路”是不含相同点的（即不绕回路），因而有 $N < n$ 。

定理 11.10.2 $^{[14]}$ 系统 S 的 $x_{t}$ 为上限能观测分量的充要条件是存在一个 $0 \leqslant N < n$ ，使 $G_{0}(S)$ 中至少有 t 的一个 N 步出口 l 到 y 有弧。

以上两定理用矩阵语言表达为：

定理11.10.3 (1) 系统 $S$ 的 $x_{t}$ 为分别能达分量的充要条件是存在 $0 \leqslant N < n$ , 使得 $(F^{N}B^{*})_{t} \neq -\infty$ , 这里 $B^{*} = \vee_{1 \leqslant j \leqslant q} b_{\cdot j}, (F^{N}B^{*})_{t}$ 表示 $F^{N}B^{*}$ 的第 $t$ 个分量;

(2) 系统 $S$ 的 $x_{t}$ 为上限能观测分量的充要条件是存在一个 $0 \leqslant N < n$ , 使得

$$C ^ {*} F ^ {N} [ - \infty , \dots , - \infty , 0, - \infty , \dots , - \infty ] ^ {T} \neq - \infty ,$$

这里0是第 $t$ 个分量， $C^* = \bigvee_{1\leqslant i\leqslant p}C_{i},C_{i}$ 是 $\pmb{C}$ 的第 $i$ 行.
