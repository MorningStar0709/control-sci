$$
D _ {l r} D _ {k r} ^ {- 1} = \left[ \begin{array}{c c} 4 & 0 \\ 5 & 0 \\ 2 & 0 \\ - 1 & 3 \\ - 2 & 2 \end{array} \right], D _ {k r} ^ {- 1} = \left[ \begin{array}{c c} 0 & 1 \\ - 1 & 0 \end{array} \right]
$$

于是,利用前述结论,就即可定出:

$$
A _ {c o} = \left[ \begin{array}{r r r r r} 0 & 0 & - 2 & 0 & 0 \\ 1 & 0 & - 5 & 0 & 0 \\ 0 & 1 & - 4 & 0 & 0 \\ \hdashline 0 & 0 & 2 & 0 & - 2 \\ 0 & 0 & 1 & 1 & - 3 \end{array} \right], B _ {c o} = \left[ \begin{array}{r r r r r} 1 & 0 \\ 0 & 0 \\ 0 & 0 \\ \hdashline 0 & 1 \\ 0 & 0 \end{array} \right]
$$

再进一步算出

$$
C _ {o} = \left[ \begin{array}{c c c c c} 0 & 0 & 0 & 1 & 0 \\ - 1 & 0 & 0 & 0 & 0 \end{array} \right]

\begin{array}{l} c _ {o} \tilde {I} = \left[ \begin{array}{c c c c c} 0 & 0 & 0 & 0 & 1 \\ 0 & 0 & - 1 & 0 & 0 \end{array} \right] \\ N (s) C _ {o} \tilde {I} = \left[ \begin{array}{c c c c c} 0 & 0 & 0 & 0 & s \\ 0 & 0 & - s ^ {2} & 0 & - s \end{array} \right] \\ = \left[ \begin{array}{c c c c c} 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & - 1 & 0 & 0 \end{array} \right] s ^ {2} + \left[ \begin{array}{c c c c c} 0 & 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 & - 1 \end{array} \right] s \\ \end{array}
$$

从而，又可定出：

$$
C _ {c o} = [ N (s) C _ {o} \tilde {I} ] _ {s \rightarrow A _ {c o}} = \left[\begin{array}{r r r r r}0&0&1&1&- 3\\- 1&4&- 1 2&- 1&3\end{array}\right]
$$

左 MFD 的能观测性形实现 给定 $q \times p$ 严格真左 MFD $D_{L}^{-1}(s) N_{L}(s)$ , $D_{L}(s)$ 为列既约, 则称如下的一个状态空间描述

$$\dot {\boldsymbol {x}} = A _ {o b} \boldsymbol {x} + B _ {o b} \boldsymbol {u}, \boldsymbol {y} = C _ {o b} \boldsymbol {x}, \boldsymbol {x} \in \mathcal {R} ^ {*} \tag {9.192}$$

为 $D_{L}^{-1}(s)N_{L}(s)$ 的维数是 $n = \deg \det D_L(s)$ 的能观测性形实现，如果其满足如下条件：

① $C_{ob}(sI - A_{ob})^{-1}B_{ob} = D_{L}^{-1}(s)N_{L}(s);$

② 表 $C_{ob}^{T} = [C_{1}^{T}, C_{2}^{T}, \cdots, C_{q}^{T}]$ ，其中“ $T$ ”表示取转置，而 $k_{i} = \delta_{ci} D_{L}(s)$ 为列次数，则有

$$\left[ C _ {1} ^ {T} A _ {o b} ^ {T} C _ {1} ^ {T} \dots \left(A _ {o b} ^ {T}\right) ^ {k _ {1} - 1} C _ {1} ^ {T} \right\rvert \dots \left| C _ {q} ^ {T} A _ {o b} ^ {T} C _ {q} ^ {T} \dots \left(A _ {o b} ^ {T}\right) ^ {k _ {q} - 1} C _ {q} ^ {T} \right] = I _ {\bullet} \tag {9.193}$$

左 MFD 的能观测性形实现是和右 MFD 的能控性形实现相对偶的。利用这种对偶关系，可以直接由能控性形实现 $(A_{co}, B_{co}, C_{co})$ 的结论来导出能观测性形实现 $(A_{ob}, B_{ob}, C_{ob})$ 的结论。

结论 给定 $q \times p$ 的严格真左 MFD $D_{L}^{-1}(s)N_{L}(s)$ , $D_{L}(s)$ 为列既约, 则对其能观测性形实现 $(A_{ob}, B_{ob}, C_{ob})$ , 有:

① 确定 $(A_{ob}, B_{ob}, C_{ob})$ 的关系式为:

$$A _ {o b} = \tilde {I} _ {n} A _ {c} \tilde {I} _ {n}, B _ {o b} = \left[ \tilde {I} _ {n} B _ {c} N _ {L} (s) \right] _ {s \rightarrow A _ {o b}}, C _ {o b} = C _ {c} \tilde {I} _ {n} \tag {9.194}$$

其中 $(A_{c}, B_{c}, C_{c})$ 为 $I_{q}D_{L}^{-1}(s)$ 的控制器形实现，可按下述关系式来确定：
