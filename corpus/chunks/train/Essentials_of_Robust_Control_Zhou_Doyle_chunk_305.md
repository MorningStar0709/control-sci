Conversely, suppose K is proper and achieves internal stability. Introduce an rcf of K over $\mathcal { R } \mathcal { H } _ { \infty }$ as $K = U V ^ { - 1 }$ . Then by Lemma 5.7, $Z : = \tilde { M } V - \tilde { N } U$ is invertible in $\mathcal { R } \mathcal { H } _ { \infty }$ . Define $Q _ { r }$ by the equation

$$U _ {0} + M Q _ {r} = U Z ^ {- 1}, \tag {11.9}$$

so

$$Q _ {r} = M ^ {- 1} (U Z ^ {- 1} - U _ {0}).$$

Then, using the Bezout identity, we have

$$
\begin{array}{l} V _ {0} + N Q _ {r} = V _ {0} + N M ^ {- 1} \left(U Z ^ {- 1} - U _ {0}\right) \\ = V _ {0} + \tilde {M} ^ {- 1} \tilde {N} (U Z ^ {- 1} - U _ {0}) \\ = \tilde {M} ^ {- 1} (\tilde {M} V _ {0} - \tilde {N} U _ {0} + \tilde {N} U Z ^ {- 1}) \\ = \tilde {M} ^ {- 1} (I + \tilde {N} U Z ^ {- 1}) \\ = \tilde {M} ^ {- 1} (Z + \tilde {N} U) Z ^ {- 1} \\ = \tilde {M} ^ {- 1} \tilde {M} V Z ^ {- 1} \\ = V Z ^ {- 1}. \tag {11.10} \\ \end{array}
$$

Thus,

$$
\begin{array}{l} K = U V ^ {- 1} \\ = (U _ {0} + M Q _ {r}) (V _ {0} + N Q _ {r}) ^ {- 1}. \\ \end{array}
$$

To see that Qr belongs to $\mathcal { R } \mathcal { H } _ { \infty } .$ observe first from equation (11.9) and then from equation (11.10) that both $M Q _ { r }$ and $N Q _ { i }$ r belong to $\mathcal { R } \mathcal { H } _ { \infty }$ . Then

$$Q _ {r} = (\tilde {V} _ {0} M - \tilde {U} _ {0} N) Q _ {r} = \tilde {V} _ {0} (M Q _ {r}) - \tilde {U} _ {0} (N Q _ {r}) \in \mathcal {R H} _ {\infty}.$$

Finally, since V and Z evaluated at $s = \infty$ are both invertible, so is $V _ { 0 } + N Q$ r from equation (11.10), and hence so is $I + V _ { 0 } ^ { - 1 } N Q _ { \ i }$ .

Similarly, the parameterization given in equation (11.6) can be obtained.

To show that the controller can be written in the form of equation (11.7), note that

$$(U _ {0} + M Q _ {y}) (V _ {0} + N Q _ {y}) ^ {- 1} = U _ {0} V _ {0} ^ {- 1} + (M - U _ {0} V _ {0} ^ {- 1} N) Q _ {y} (I + V _ {0} ^ {- 1} N Q _ {y}) ^ {- 1} V _ {0} ^ {- 1}$$

and that $U _ { 0 } V _ { 0 } ^ { - 1 } = \tilde { V } _ { 0 } ^ { - 1 } \tilde { U } _ { 0 }$ . We have

$$(M - U _ {0} V _ {0} ^ {- 1} N) = (M - \tilde {V} _ {0} ^ {- 1} \tilde {U} _ {0} N) = \tilde {V} _ {0} ^ {- 1} (\tilde {V} _ {0} M - \tilde {U} _ {0} N) = \tilde {V} _ {0} ^ {- 1}$$

and

$$K = U _ {0} V _ {0} ^ {- 1} + \tilde {V} _ {0} ^ {- 1} Q _ {y} (I + V _ {0} ^ {- 1} N Q _ {y}) ^ {- 1} V _ {0} ^ {- 1}.$$

![](image/daadb401b9b52379ffa320f290771e88fb53bd9708d2d3e65d9dd32cde0a66cb.jpg)

Corollary 11.7 Given an admissible controller K with coprime factorizations $K =$ $U V ^ { - 1 } = \tilde { V } ^ { - 1 } \tilde { U }$ , the free parameter $Q _ { y } \in \mathcal { R } \mathcal { H } _ { \infty }$ in Youla parameterization is given by

$$Q _ {y} = M ^ {- 1} (U Z ^ {- 1} - U _ {0})$$

where $Z : = \tilde { M } V - \tilde { N } U$ .
