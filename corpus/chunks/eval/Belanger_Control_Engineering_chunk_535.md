# ◆ ◆ ◆ REMARK

If $|a| < 1$ , the sequence tends to zero; it “blows up” if $|a| > 1$ . A negative value of a is possible (although not by sampling a real exponential) and indicates a sequence of values alternating in sign.

Equation 9.13 is valid for all $a$ , real or complex. It is used as the basis from which to derive $z$ -transforms for some of the following sequences:

(i) $\widehat{y}(k) = u_0(k)$ (discrete-time impulse):

$$\mathcal {Z} [ u _ {0} (k) ] = 1$$

directly from the definition, because $u_0(0) = 1$ , $u_0(k) = 0$ , for $k \neq 0$ .

(ii) $\widehat{y}(k) = u_{-1}(k)$ (discrete step). For $a = 1$ ,

$$\mathcal {Z} [ \widehat {y} (k) ] = \frac {1}{1 - z ^ {- 1}} = \frac {z}{z - 1}, \quad | z | > 1.$$

(iii) $\widehat{y}(k) = a^k\cos (\omega k)$ :

$$
\begin{array}{l} \mathcal {Z} [ \widehat {y} (k) ] = \mathcal {Z} \left[ \frac {1}{2} \left(a e ^ {j \omega}\right) ^ {k} + \frac {1}{2} \left(a e ^ {- j \omega}\right) ^ {k} \right] \\ = \frac {1 / 2}{z - a e ^ {j \omega}} + \frac {1 / 2}{z - a e ^ {- j \omega}} \\ = \frac {z - a \cos \omega}{z ^ {2} - (2 a \cos \omega) z + a ^ {2}}, \quad | z | > | a |. \\ \end{array}
$$

(iv) $\widehat{y} (k) = a^{k}\sin (\omega k)$

$$
\begin{array}{l} \mathcal {Z} [ \widehat {y} (k) ] = \frac {1 / 2 j}{z - a e ^ {j \omega}} - \frac {1 / 2 j}{z - a e ^ {- j \omega}} \\ = \frac {a \sin \omega}{z ^ {2} - (2 a \cos \omega) z + a ^ {2}}, \quad | z | > | a |. \\ \end{array}
$$

We shall need a few of the z-transform theorems.

■ Theorem 9.1 Delay Theorem $\mathcal{Z}[\widehat{y}(k - 1)u_{-1}(k - 1)] = z^{-1}\widehat{y}(z)$ .

Proof: $\mathcal{Z}[\widehat{y}(k - 1)u_{-1}(k - 1)] = \sum_{k=1}^{\infty}\widehat{y}(k - 1)z^{-k}$ . Let $k' = k - 1$ . Then

$$
\begin{array}{l} \mathcal {Z} [ \widehat {y} (k - 1) u _ {- 1} (k - 1) ] = \sum_ {k ^ {\prime} = 0} ^ {\infty} \widehat {y} (k ^ {\prime}) z ^ {- k ^ {\prime} - 1} \\ = z ^ {- 1} \sum_ {k ^ {\prime} = 0} ^ {\infty} \widehat {y} (k ^ {\prime}) z ^ {- k ^ {\prime}} \\ = z ^ {- 1} \widehat {y} (z). \quad \blacksquare \\ \end{array}
$$

■ Theorem 9.2 Advance Theorem $\mathcal{Z}[\widehat{y}(k + 1)] = z[\widehat{y}(z) - \widehat{y}(0)]$ .

Proof: $\mathcal{Z}[\widehat{y}(k + 1)] = \sum_{k=0}^{\infty} \widehat{y}(k + 1)z^{-k}$ . Let $k' = k + 1$ . Then
