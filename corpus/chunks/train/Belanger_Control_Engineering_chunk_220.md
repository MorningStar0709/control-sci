One of the important properties of a Blaschke product is that $|B_p(j\omega)| = 1$ for all $\omega$ ; i.e., it is an all-pass transfer function.

To show this, let $p_1$ be real. Then

$$\left| \frac {- p _ {1} + j \omega}{p _ {1} + j \omega} \right| ^ {2} = \frac {p _ {1} ^ {2} + \omega^ {2}}{p _ {1} ^ {2} + \omega^ {2}} = 1.$$

If $p_1$ is complex, then

$$
\begin{array}{l} \left| \frac {- p _ {1} + j \omega}{p _ {1} + j \omega} \right| ^ {2} \left| \frac {- p _ {1} ^ {*} + j \omega}{p _ {1} ^ {*} + j \omega} \right| ^ {2} = \frac {(R e p _ {1}) ^ {2} + (\omega - I _ {m} p _ {1}) ^ {2}}{(R e p _ {1}) ^ {2} + (\omega + I _ {m} p _ {1}) ^ {2}} \cdot \frac {(R e p _ {1}) ^ {2} + (\omega + I _ {m} p _ {1}) ^ {2}}{(R e p _ {1}) ^ {2} + (\omega - I _ {m} p _ {1}) ^ {2}} \\ = 1. \\ \end{array}
$$

Since $B_{p}(s)$ is a product of such terms, it follows that $B_{p}(j\omega) = 1$ .

Since $B_{p}(s)$ is a product of all three zeros. If $S(s)$ is proper, then so is $\widetilde{S}(s)$ , since $B_{p}(s)$ has equal numbers of poles and zeros. Thus, with $S(s)$ assumed proper, $\widetilde{S}(s)$ is a proper, stable transfer function with no zeros in the open RHP, and Equation 4.22 applies:

$$\frac {1}{\pi} \int_ {- \infty} ^ {\infty} \log | \widetilde {S} (j \omega) | f (s _ {0}, \omega) d \omega = \log | \widetilde {S} (s _ {0}) | \tag {4.51}$$

where $s_0$ is any RHP point and $f(s_0, \omega)$ is as in Equation 4.24.

From Equation 4.50,

$$\widetilde {S} (s) = \frac {S (s)}{B _ {p} (s)}.$$

It follows that

$$\widetilde {S} (s _ {0}) = \frac {S (s _ {0})}{B _ {p} (s _ {0})}$$

and also that

$$| \widetilde {S} (j \omega) | = \frac {| S (j \omega) |}{| B _ {p} (j \omega) |} = | S (j \omega) |$$

since $|B_p(j\omega)| = 1$ .

Therefore, Equation 4.51 becomes

$$\frac {1}{\pi} \int_ {- \infty} ^ {\infty} \log | S (j \omega) | f (s _ {0}, \omega) d \omega = \log \frac {| S (s _ {0}) |}{| B _ {p} (s _ {0}) |}. \tag {4.52}$$

Equation 4.52 is informative if there exists an RHP point (or points) where $S$ has a known value. That is the case when $P$ has RHP zeros: by the interpolation condition, $S(z_0) = 1$ if $z_0$ is a zero of $P$ in the open RHP. Thus,

$$\frac {1}{\pi} \int_ {- \infty} ^ {\infty} \log | S (j \omega) | f (z _ {0}, \omega) d \omega = \log \frac {1}{| B _ {p} (z _ {0}) |}. \tag {4.53}$$

In the absence of RHP poles, $B_{p}(z_{0}) = 1$ and the right-hand side (RHS) of Equation 4.53 is zero. This equation is the same as Equation 4.23 in the open-loop case,

![](image/44dbe9197b6a0dab6594e16915384fd61fa10adc1fd3995bfde5b3e37271b676.jpg)
