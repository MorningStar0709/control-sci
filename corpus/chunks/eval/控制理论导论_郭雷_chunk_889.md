$$\boldsymbol {x} = \boldsymbol {A} \boldsymbol {x} \oplus \tilde {\boldsymbol {v}} \oplus \mathbf {0} \stackrel {\text { def }} {=} \boldsymbol {A} \boldsymbol {x} \oplus \boldsymbol {v}, \tag {11.9.2}$$

其中 A 由式 (11.9.1) 确定， $\tilde{v}$ 由无输入变迁的位置或弧导出的已知序列确定，0 为每个分量为 $\bar{0}$ 的向量，而 $\bar{0}$ 表示全零序列 $\langle0,0,0,\cdots,0,\cdots\rangle$ .

以上定理指出了如何用双子代数方法对ETEG建模。我们应用这个方法可对例11.9.1中的系统建模。由式(11.9.1)易得(算子复合运算记号 $\otimes$ 常被省略)

$$
\begin{array}{l} \langle t \rangle_ {1} = [ z ^ {- 1} ] [ \tilde {t} _ {0} ] \langle t \rangle_ {1} \oplus [ z ^ {- 2} ] \langle t \rangle_ {n + m + 6} \oplus \overline {{{u}}}, \\ \langle t \rangle_ {2} = [ \tilde {t _ {0}} ] \langle t \rangle_ {1} \oplus [ z ^ {- 1} ] \langle t \rangle_ {n + m + 6} \oplus \overline {{{0}}}, \\ \langle t \rangle_ {3} = [ \Delta^ {N + 1} ] [ \nabla^ {M} ] \langle t \rangle_ {2} \oplus [ \Delta^ {N + 1} ] [ z ^ {- N - 1} ] [ \widetilde {t _ {2}} ] \langle t \rangle_ {n + m + 5} \oplus \overline {{0}}, \\ \langle t \rangle_ {n + 3} = \langle t \rangle_ {n + 2} \oplus [ z ^ {- 1} ] \langle t \rangle_ {n + 3} \oplus \overline {{{0}}}, \\ \langle t \rangle_ {n + 4} = \langle t \rangle_ {n + 3} \oplus [ z ^ {- 1} ] [ \widetilde {t _ {1}} ] \langle t \rangle_ {n + 4} \oplus \overline {{{0}}}, \\ \langle t \rangle_ {n + 5} = [ \tilde {t} _ {1} ] \langle t \rangle_ {n + 4} \oplus [ z ^ {- 1} ] \langle t \rangle_ {n + 5} \oplus \overline {{{0}}}, \\ \langle t \rangle_ {n + m + 4} = \langle t \rangle_ {n + m + 3} \oplus [ z ^ {- 1} ] \langle t \rangle_ {n + m + 4} \oplus \overline {{{0}}}, \\ \langle t \rangle_ {n + m + 5} = [ \widetilde {t _ {r}} ] \langle t \rangle_ {n + m + 4} \oplus [ z ^ {- 1} ] [ \widetilde {t _ {2}} ] \langle t \rangle_ {n + m + 5} \oplus \overline {{{0}}}, \\ \langle t \rangle_ {n + m + 6} = [ \Delta^ {k} ] \langle t \rangle_ {3} \oplus \overline {{{0}}}. \\ \end{array}
$$

:

• • •

令 $x = [\langle t \rangle_{1}, \langle t \rangle_{2}, \cdots, \langle t \rangle_{n+m+6}]^{T}$ ，则上面式子矩阵形式为

$$\boldsymbol {x} = \boldsymbol {A} \boldsymbol {x} \oplus \overline {{\boldsymbol {v}}},$$

其中 $\overline{v}=[\overline{u},\overline{0},\cdots,\overline{0}]^{T}$ ，A 为下面图 11.9.2 的关联矩阵.

![](image/6e0e4995441ac978e2f161ab3a2fa62f10f1a4437c35779e0041ea629acaea37.jpg)

<details>
<summary>flowchart</summary>
