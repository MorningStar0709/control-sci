证 设 $G(s)$ 为 $p \times q$ 有理分式矩阵, 则分别各有 $C_{p}^{i}$ 和 $C_{q}^{i}$ 种方式来选取 $i$ 个行和 $i$ 个列以组成 $G(s)$ 的 $i \times i$ 子式, 其中 $C_{p}^{i}$ 和 $C_{q}^{i}$ 表示由 $p$ 和 $q$ 中取 $i$ 的组合。令 $|G|_{k}^{i}$ 表示按规定顺序中由第 $k$ 个方式选取 $i$ 个行和由第 $l$ 个方式选取 $i$ 个列而形成的 $G(s)$ 的 $i \times i$ 子式, 则由宾奈特-柯西 (Binet-Cauchy) 定理可导出, 对矩阵等式

$$G (s) = U (s) M (s) V (s) \tag {8.48}$$

必定成立

$$\left| G \right| _ {k l} ^ {i} = \sum_ {m, h} \left| U \right| _ {k m} ^ {i} \left| M \right| _ {m h} ^ {i} \left| V \right| _ {l h} ^ {i} \tag {8.49}$$

再令

$$\tilde {v} _ {\alpha} = v _ {\alpha} (| M | _ {m h} ^ {i}) = \text {子式} | M | _ {m h} ^ {i} \text {在} s = \alpha \text {的评价值}$$

那么,根据定义(8.43)即可得到

$$\left| M \right| _ {m h} ^ {i} = (s - \alpha) ^ {\theta_ {\alpha}} \frac {b _ {m h} (s)}{a _ {m h} (s)} \tag {8.50}$$

其中， $\{b_{mk}(s), a_{mk}(s)\}$ 为互质，且 $b_{mk}(s)$ 和 $a_{mk}(s)$ 均不能被 $(s - \alpha)$ 除尽。将(8.50)代入(8.49)，并令

$$\nu_ {a} ^ {(i)} (M) = \min _ {m, h} \left\{\nu_ {a} \left(\left| M \right| _ {m b} ^ {i}\right) \right\} \tag {8.51}$$

于是进一步可导出

$$\left| G \right| _ {k l} ^ {i} = (s - \alpha) ^ {\nu_ {a} ^ {(i)} (M)} \cdot \beta (s) \tag {8.52}$$

其中， $\beta(s)$ 是一个有理分式。并且，由(8.51)，并考虑到 $U(s)$ 和 $V(s)$ 为多项式矩阵，可知 $\beta(s)$ 只能包含 $(s - \alpha)$ 的正幂次项，而不可能包含 $(s - \alpha)$ 的负幂次项。这表明，对所有 $k, l$ 必成立

$$v _ {a} \left(\left| G \right| _ {k l} ^ {i}\right) \geqslant v _ {a} ^ {(i)} (M) \tag {8.53}$$

从而，再根据定义式(8.44)，又可得到

$$\nu_ {a} ^ {(i)} (G) \geqslant \nu_ {a} ^ {(i)} (M) \tag {8.54}$$

进而，把式(8.48)改写为

$$M (s) = U ^ {- 1} (s) G (s) V ^ {- 1} (s) \tag {8.55}$$

其中，由于 $U(s)$ 和 $V(s)$ 为单模阵，故可知 $U^{-1}(s)$ 和 $V^{-1}(s)$ 也为多项式矩阵。于是，通过和前类同的推证过程，还可导出

$$v _ {a} ^ {(i)} (M) \geqslant v _ {a} ^ {(i)} (G) \tag {8.56}$$

这样，由(8.54)和(8.56)，即证明了：

$$v _ {a} ^ {(i)} (G) = v _ {a} ^ {(i)} (M), i = 1, 2, \dots , r \tag {8.57}$$

而(8.47)中的右边的等式成立则是显然的。至此，结论的证明完成。

结论2 令 $S_{sp}$ 为给定传递函数矩阵 $G(s)$ 的有限极点零点集，则对任一 $\gamma \in S_{sp}$ ，必有

$$v _ {r} ^ {(i)} (G) = 0, i = 1, 2, \dots , r \tag {8.58}$$

证 由已知 $\gamma$ 不是 $G(s)$ 的零点或极点表明， $\varepsilon_{i}(s)$ 和 $\psi_{i}(s)$ 中均不包含因子 $(s - \gamma)$ ，因此根据评价值的定义，即得

$$v _ {r} ^ {(i)} (M) = 0, i = 1, 2, \dots , r \tag {8.59}$$

进而由结论1又可知

$$\nu_ {\gamma} ^ {(i)} (G) = \nu_ {\gamma} ^ {(i)} (M) = 0 \tag {8.60}$$

从而结论得证。

结论3 给定传递函数矩阵 $G(s)$ , $\operatorname{rank} G(s) = r$ , 表 $\{\sigma_1(\alpha), \cdots, \sigma_r(\alpha)\}$ 为 $G(s)$ 在 $s = \alpha$ 处的结构指数, $\{\nu_a^{(1)}(s), \cdots, \nu_a^{(r)}(s)\}$ 为 $G(s)$ 在 $s = \alpha$ 处的各阶评价值, 则两者之间成立如下的关系式:
