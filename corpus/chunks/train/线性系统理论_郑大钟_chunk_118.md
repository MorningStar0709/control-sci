$$e ^ {- k T \mathrm{Re} _ {1} ^ {2}} \cdot (k T) ^ {- p}$$

就可得到

$$
\begin{array}{l} e ^ {- k T \mathrm{Re} \lambda_ {1}} (k T) ^ {- \nu} (\alpha^ {T} e ^ {A k T} B) _ {\eta} \\ = \left\{e ^ {i k T \operatorname{Im} \lambda_ {1}} \left[ d _ {1 0} ^ {\eta} + d _ {1 1} ^ {\eta} (k T) ^ {- 1} + \dots \right] + \dots \right. \\ + e ^ {i k T \operatorname{Im} \lambda} \zeta \left[ d _ {\zeta_ {0}} ^ {\eta} + d _ {\zeta_ {1}} ^ {\eta} (k T) ^ {- 1} + \dots \right] \} + \left\{e ^ {i k T \operatorname{Im} \lambda} \zeta + 1 \left[ d _ {\zeta + 1, 0} ^ {\eta} (k T) ^ {- 1} \right. \right. \\ + \dots ] + \dots + e ^ {j k T \operatorname{Im} \lambda_ {r}} \left[ d _ {r 0} ^ {\eta} (k T) ^ {- 1} + \dots \right] \} \\ + \left\{e ^ {- k T (\operatorname{Re} \lambda_ {1} - \operatorname{Re} \lambda_ {r + 1})} e ^ {j k T \operatorname{Im} \lambda_ {r + 1}} \left[ d _ {r + 1, 0} ^ {\eta} (k T) ^ {- (p - f)} \right. \right. \\ + \dots ] + \dots \}, \eta = 1, 2, \dots , p \tag {3.155} \\ \end{array}
$$

不难看出，由于 $k=0,1,2,\cdots$ ，故上式当 $k\to\infty$ 时也应成立，且其在 $k\to\infty$ 的极限为

$$\left(d _ {1 0} ^ {\eta} e ^ {j k T \operatorname{Im} \lambda_ {1}} + \dots + d _ {\zeta 0} ^ {\eta} e ^ {j k T \operatorname{Im} \lambda_ {\zeta}}\right) _ {k \rightarrow \infty} \tag {3.156}$$

从数学上可证明，当结论条件满足时，式(3.156)的极限值不恒为零。也即，成立

$$\lim _ {k \rightarrow \infty} a ^ {T} e ^ {A k T} B \neq 0 \tag {3.157}$$

显然，(3.157)和(3.148)是矛盾的。表明，反设不成立，即有 $e^{AkT}B$ 行线性无关。

最后,综合上面的推证结果即证明了:在(3.138)和(3.139)的条件下, $\Sigma_{T}$ 保持能控性。

同理，也可证得，在结论给出的条件下， $\Sigma_{T}$ 可保持能观测性。至此，证明完成。

例 设有线性连续时间系统为

$$
\begin{array}{l} \dot {x} = \left[ \begin{array}{l l} 0 & 1 \\ - 1 & 0 \end{array} \right] x + \left[ \begin{array}{l} 1 \\ 0 \end{array} \right] u \\ y = [ 0 \quad 1 ] x \\ \end{array}
$$

易知，系统为能控和能观测，其特征值为 $\lambda_{1}=j$ 和 $\lambda_{2}=-j$ 。于是，利用上述结论可知，当选择采样周期 T 的数值使

$$T \neq \frac {2 l \pi}{\operatorname{Im} \left(\lambda_ {1} - \lambda_ {2}\right)} = \frac {2 l \pi}{2} = l \pi , \quad l = 1, 2, \dots$$

时,其时间离散化系统

$$
\boldsymbol {x} (k + 1) = \left[ \begin{array}{l l} \cos T & \sin T \\ - \sin T & \cos T \end{array} \right] - \boldsymbol {x} (k) + \left[ \begin{array}{l} \sin T \\ \cos T - 1 \end{array} \right] u (k)
y (k) = [ 0 \quad 1 ] x (k)
$$

必保持为能控和能观测。

此外，若直接由时间离散化系统来导出能控性和能观测性判别矩阵，有

$$
[ H | G H ] = \left[ \begin{array}{c c} \sin T & 2 \sin T \cos T - \sin T \\ \cos T - 1 & \cos^ {2} T - \sin^ {2} T - \cos T \end{array} \right]

\left[ \begin{array}{c} C \\ C G \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ - \sin T & \cos T \end{array} \right]
$$

那么，根据

$$
\det [ H \mid G H ] = 2 \sin T [ \cos T - 1 ] \left\{ \begin{array}{l l} = 0, & T = l \pi \\ \neq 0, & T \neq l \pi \end{array} \right.

\det \left[ \begin{array}{l} C \\ C G \end{array} \right] = \sin T \left\{ \begin{array}{l l} = 0, & T = l _ {\pi} \\ \neq 0, & T \neq l _ {\pi} \end{array} \right.
$$

可知，当 $T \neq l\pi$ 时离散化系统为能控和能观测。这验证了上面的判断结果。
