$$
\left\{ \begin{array}{l} T (s I - A _ {1}) = (s I - A _ {2}) \vec {T} (s) \\ \overline {{T}} (s) = \overline {{V}} (s) - \overline {{U}} (s) (s I - A _ {1}) \end{array} \right. \tag {10.143}
$$

或

$$(s I - A _ {2}) ^ {- 1} T = \overline {{{T}}} (s) (s I - A _ {1}) ^ {- 1} \tag {10.144}$$

上式中， $(sI - A_2)^{-1}T$ 是严格真的，所以 $\overline{T}(s)(sI - A_1)^{-1}$ 也必须是严格真的。但特征矩阵 $(sI - A_1)$ 的列次数均为1，所以由此进一步可知 $\overline{T}(s)$ 必为常数矩阵，将其表为 $\overline{T}$ 。于是，还可把(10.143)改写为

$$T (s I - A _ {1}) = (s I - A _ {2}) \overline {{{T}}} \tag {10.145}$$

而由此又可导出

$$(T - \bar {T}) s + (A _ {2} \bar {T} - T A _ {1}) s ^ {0} = 0 \tag {10.146}$$

因此，进而就可得到

$$
\left\{ \begin{array}{l} T = \overline {{T}} \\ A _ {2} T = T A _ {1} \end{array} \right. \tag {10.147}
$$

下面，来证明 $T$ 是可逆的。因 $U(s)$ 为单模阵，可知 $U^{-1}(s)$ 也为多项式矩阵；再由(10.141)，可以导出如下的关系式：

$$U ^ {- 1} (s) \left(s I - A _ {2}\right) = \left(s I - A _ {1}\right) V (s) \tag {10.148}$$

一般而言 $(sI - A_1)^{-1}U^{-1}(s)$ 也不是严格真的，故运用矩阵除法，类似地有

$$U ^ {- 1} (s) = \left(s I - A _ {1}\right) \widetilde {U} (s) + \widetilde {T} \tag {10.149}$$

其中 $\tilde{T}$ 为常数矩阵。现将(10.142)左乘(10.149)，有

$$
\begin{array}{l} I = U (s) U ^ {- 1} (s) = \left(s I - A _ {2}\right) \bar {U} (s) \left(s I - A _ {1}\right) \tilde {U} (s) + \left(s I - A _ {2}\right) \bar {U} (s) \tilde {T} \\ + T (s I - A _ {1}) \tilde {U} (s) + T \tilde {T} \tag {10.150} \\ \end{array}
$$

但由(10.147)和(10.145)知

$$T (s I - A _ {1}) = (s I - A _ {2}) T \tag {10.151}$$

于是，将(10.151)代入(10.150)并加以整理，可以得到

$$(I - T \widetilde {T}) = (s I - A _ {2}) [ \widetilde {U} (s) (s I - A _ {1}) \widetilde {U} (s) + \overline {{U}} (s) \widetilde {T} + T \widetilde {U} (s) ] \tag {10.152}$$

或

$$(s I - A _ {2}) ^ {- 1} (I - T \widetilde {T}) = [ \bar {U} (s) (s I - A _ {1}) \widetilde {U} (s) + \bar {U} (s) \widetilde {T} + T \widetilde {U} (s) ] \tag {10.153}$$

容易看出，上式中，等式右边为多项式矩阵，而等式左边是有理分式矩阵。所以欲使等式成立只有两者均为零矩阵，也即成立

$$I - T \widetilde {T} = 0 \text {或} T \widetilde {T} = I \tag {10.154}$$

这表明 $T$ 是可逆的。这样，由(10.147)，即得

$$A _ {2} = T A _ {1} T ^ {- 1} \tag {10.155}$$

进而，由(10.140)，可以导出

$$U (s) B _ {1} = \left(s I - A _ {2}\right) \bar {Y} (s) + B _ {2} \tag {10.156}$$

再利用(10.142)，则上式可表为

$$(s I - A _ {2}) \bar {U} (s) B _ {1} + T B _ {1} = (s I - A _ {2}) \bar {Y} (s) + B _ {2} \tag {10.157}$$

或

$$\overline {{U}} (s) B _ {1} - \overline {{Y}} (s) = (s! - A _ {2}) ^ {- 1} (B _ {2} - T B _ {1}) \tag {10.158}$$

显见，上式左边为多项式矩阵，而右边为有理分式矩阵。所以，(10.158) 仅当 $B_{2}-TB_{1}=0$ 时才成立，从而有

$$B _ {2} = T B _ {1} \tag {10.159}$$

最后，由 $S_{1}(s)$ 和 $S_{2}(s)$ 具有相同的传递函数矩阵可有
