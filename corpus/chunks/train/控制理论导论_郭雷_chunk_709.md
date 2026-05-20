$$
\begin{array}{l} \prod_ {j = i + 1} ^ {n} \left[ 1 + \lambda^ {- 1} C \left(\alpha_ {j} \delta_ {j} \log r _ {j - 1}\right) ^ {2} \right] \\ \leqslant \prod_ {j = i + 1} ^ {n} \left[ 1 + \left(\frac {\delta \alpha_ {j}}{2}\right) ^ {2} \right] \cdot \prod_ {j = i} ^ {n} \left[ 1 + \lambda^ {- 1} C \left(\frac {2}{\delta} \delta_ {j} \log r _ {j - 1}\right) ^ {2} \right] \\ \leqslant \exp \left\{\delta \sum_ {j = i + 1} ^ {n} \alpha_ {j} \right\} \cdot \exp \left\{\frac {4}{\delta} \left(\frac {C}{\lambda}\right) ^ {1 / 2} \sum_ {j = i + 1} ^ {n} \delta_ {j} \log r _ {j - 1} \right\} \\ \leqslant \exp \left\{\epsilon \log r _ {n} \right\} \cdot \exp \left\{(\log r _ {n}) \left[ \frac {4}{\delta} \left(\frac {C}{\lambda}\right) ^ {1 / 2} \sum_ {j = i} ^ {n} \delta_ {j} \right] \right\} \\ \leqslant r _ {n} ^ {\epsilon} \exp \left\{\left(\log r _ {n}\right) \epsilon \right\} = r _ {n} ^ {2 \epsilon} \quad \text { a.s. } \tag {9.5.58} \\ \end{array}
$$

进一步，利用不等式 $1 + x \leqslant e^{x}, x \geqslant 0$ ，有

$$
\begin{array}{l} \prod_ {j = i} ^ {n} \left(1 + \lambda^ {- 1} C \alpha_ {j} \delta_ {j}\right) \leqslant \exp \left\{\delta \sum_ {j = i} ^ {n} \alpha_ {j} \right\} \exp \left\{\frac {C}{\lambda \delta} \sum_ {j = i} ^ {n} \delta_ {j} \right\} \\ = O (r _ {n} ^ {\epsilon}) \quad \text { a.s. } \quad \forall n \geqslant i \geqslant i _ {0}, \tag {9.5.59} \\ \end{array}
$$

由于 $\Delta \hat{b}_{1n} \to 0$ , 故存在 $i_0 > 0$ 使

$$\sup _ {j \geqslant i _ {0}} \left\{1 + C \lambda^ {- 1} (\Delta \hat {b} _ {1 j}) ^ {2} \right\} < 2 - \lambda ,$$

所以对 $\forall n\geqslant i\geqslant i_0$

$$\prod_ {j = i + 1} ^ {n} \left(1 + C \lambda^ {- 1} (\Delta \hat {b} _ {1 j}) ^ {2}\right) \leqslant (2 - \lambda) ^ {n - i}. \tag {9.5.60}$$

最后利用 $f_{j}$ 的定义从式(9.5.58)\~(9.5.60)得

$$
\begin{array}{l} \prod_ {j = i + 1} ^ {n} \left(1 + C \lambda^ {- 1} f _ {j}\right) \\ \leqslant \prod_ {j = i + 1} ^ {n} \left(1 + C \lambda^ {- 1} \left(\alpha_ {j} \delta_ {j} \log r _ {j - 1}\right) ^ {2}\right) \prod_ {j = i + 1} ^ {n} \left(1 + C \lambda^ {- 1} \alpha_ {j} \delta_ {j}\right) \prod_ {j = i + 1} ^ {n} \left(1 + \frac {C \lambda^ {- 1}}{\log r _ {j}}\right) \\ = O \left(r _ {n} ^ {3 \epsilon} (2 - \lambda) ^ {n - i}\right) \quad \text { a   .   s   . } \quad \forall n \geqslant i \geqslant i _ {0} \\ \end{array}
$$

将此式代入式 (9.5.56), 经化简得

$$L _ {n + 1} = O (r _ {n} ^ {3 \epsilon} d _ {n} \log^ {4} r _ {n}), \quad \forall \epsilon > 0.$$

利用 $\epsilon$ 的任意性得

$$y _ {n + 1} ^ {2} \leqslant L _ {n + 1} = O (r _ {n} ^ {\epsilon}), \quad \epsilon > 0.$$
