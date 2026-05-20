由于 $\alpha \neq 0$ ，所以式(9-107)意味着 $S$ 为行线性相关，即 $\operatorname{rank} S < n$ ，这显然和已知 $\operatorname{rank} S = n$ 相矛盾。因而反设不成立，系统应为完全可控。

必要性:已知系统完全可控,欲证 $\operatorname{rank}S = n$ 。

采用反证法。反设 $\operatorname{rank} S < n$ ，这意味着 $S$ 为线性相关，因此必存在一个非零 $n$ 维常数向量 $\alpha$ 使

$$\boldsymbol {\alpha} ^ {T} \boldsymbol {S} = \boldsymbol {\alpha} ^ {T} [ \boldsymbol {B} \quad \boldsymbol {A B} \quad \dots \quad \boldsymbol {A} ^ {n - 1} \boldsymbol {B} ] = \boldsymbol {0}$$

成立。考虑到问题的一般性，由上式可导出

$$\boldsymbol {\alpha} ^ {\mathrm{T}} \boldsymbol {A} ^ {i} \boldsymbol {B} = \mathbf {0}; \quad i = 0, 1, 2, \dots , n - 1 \tag {9-108}$$

根据凯莱-哈密顿定理, $A^{n},A^{n+1},\cdots$ 均可表示为A的n-1阶多项式，因而式(9-108)又可写为

$$\boldsymbol {\alpha} ^ {\mathrm{T}} \boldsymbol {A} ^ {i} \boldsymbol {B} = \mathbf {0}; \quad i = 0, 1, 2, 3, \dots \tag {9-109}$$

从而对任意 $t_1 > 0$ 有

$$(- 1) ^ {i} \boldsymbol {\alpha} ^ {\mathrm{T}} \frac {\boldsymbol {A} ^ {i} t ^ {i}}{i !} \boldsymbol {B} = \mathbf {0}; \quad \forall t \in [ 0, t _ {1} ]; \quad i = 0, 1, 2, \dots$$

或 $\alpha^{T}\left[I-A t+\frac{1}{2}A^{2}t^{2}-\frac{1}{3!}A^{3}t^{3}+\cdots\right]B=\alpha^{T}e^{-A t}B=0,\forall t\in[0,t_{1}]$ (9-110)

因而有

$$\boldsymbol {\alpha} ^ {\mathrm{T}} \int_ {0} ^ {t _ {1}} \mathrm{e} ^ {- \boldsymbol {A} t} \boldsymbol {B} \boldsymbol {B} ^ {\mathrm{T}} \mathrm{e} ^ {- \boldsymbol {A} ^ {\mathrm{T}} t} \mathrm{d} t \boldsymbol {\alpha} = \boldsymbol {\alpha} ^ {\mathrm{T}} \boldsymbol {W} (0, t _ {1}) \boldsymbol {\alpha} = \mathbf {0} \tag {9-111}$$

因为已知 $\pmb{\alpha} \neq \mathbf{0}$ , 若式(9-111)成立, 则 $W(0, t_1)$ 必为奇异, 系统为不完全可控, 与已知结果相矛盾。于是有 $\operatorname{rank} S = n$ , 必要性得证。秩判据证毕。

例 9-10 桥式网络如图 9-20 所示,试用可控性判据判断其可控性。

![](image/7f317bf5b4a0fcd7a5b64e3682b49a198df42d9f0549472ec037e4a2dcefa305.jpg)

<details>
<summary>text_image</summary>

i1
L
u
R1
i1
i2
R2
uC
C
i3
R3
i4
R4
u
</details>

图 9-20 桥式网络

解 该桥式网络的微分方程为

$$i _ {L} = i _ {1} + i _ {2} = i _ {3} + i _ {4}R _ {4} i _ {4} + u _ {C} = R _ {3} i _ {3}R _ {1} i _ {1} + u _ {c} = R _ {2} i _ {2}L \frac {\mathrm{d} i _ {L}}{\mathrm{d} t} + R _ {1} i _ {1} + R _ {3} i _ {3} = u$$

选取状态变量 $x_{1} = i_{L}, x_{2} = u_{C}$ ，消去微分方组中的 $i_{1}, i_{2}, i_{3}, i_{4}$ ，可得状态方程：
