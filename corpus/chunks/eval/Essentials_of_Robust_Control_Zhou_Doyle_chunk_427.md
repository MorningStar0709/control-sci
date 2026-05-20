where $( \tilde { N } _ { s } , \tilde { M } _ { s } )$ is a normalized left coprime factorization of $P _ { s } ,$ and the parameter γ is defined to simplify the notation to follow. The following result shows that $\underline { { \sigma } } ( K _ { \infty } )$ is explicitly bounded by functions of  and $\underline { { \sigma } } ( P _ { s } )$ , the minimum singular value of the shaped plant, and hence by equation (16.3) and (16.4) $K _ { \infty }$ will only have a limited effect on the specified loop shape at low-frequency.

Theorem 16.10 Any controller $K _ { \infty }$ satisfying equation $( 1 6 . 5 )$ , where $P _ { s }$ is assumed square, also satisfies

$$\underline {{\sigma}} (K _ {\infty} (j \omega)) \geq \frac {\underline {{\sigma}} (P _ {s} (j \omega)) - \sqrt {\gamma^ {2} - 1}}{\sqrt {\gamma^ {2} - 1} \underline {{\sigma}} (P _ {s} (j \omega)) + 1}$$

for all ω such that

$$\underline {{\sigma}} (P _ {s} (j \omega)) > \sqrt {\gamma^ {2} - 1}.$$

Furthermore, if $\underline { { \sigma } } ( P _ { s } ) \gg \sqrt { \gamma ^ { 2 } - 1 }$ , then $\underline { { \sigma } } ( K _ { \infty } ( j \omega ) ) \underset { \approx } { \overset { } { \approx } } 1 / \sqrt { \gamma ^ { 2 } - 1 }$ , where $\gtrapprox$ denotes asymptotically greater than or equal to as $\underline { { \sigma } } ( P _ { s } ) \to \infty$ .

Proof. First note that $\underline { { \sigma } } ( P _ { s } ) > \sqrt { \gamma ^ { 2 } - 1 }$ implies that

$$I + P _ {s} P _ {s} ^ {*} > \gamma^ {2} I.$$

Further, since $( \tilde { N } _ { s } , \tilde { M } _ { s } )$ is a normalized left coprime factorization of $P _ { s }$ , we have

$$\tilde {M} _ {s} \tilde {M} _ {s} ^ {*} = I - \tilde {N} _ {s} \tilde {N} _ {s} ^ {*} = I - \tilde {M} _ {s} P _ {s} P _ {s} ^ {*} \tilde {M} _ {s} ^ {*}.$$

Then

$$\tilde {M} _ {s} ^ {*} \tilde {M} _ {s} = (I + P _ {s} P _ {s} ^ {*}) ^ {- 1} < \gamma^ {- 2} I.$$

Now

$$
\left\| \left[ \begin{array}{c} I \\ K _ {\infty} \end{array} \right] (I + P _ {s} K _ {\infty}) ^ {- 1} \tilde {M} _ {s} ^ {- 1} \right\| _ {\infty} \leq \gamma
$$

can be rewritten as

$$(I + K _ {\infty} ^ {*} K _ {\infty}) \leq \gamma^ {2} (I + K _ {\infty} ^ {*} P _ {s} ^ {*}) (\tilde {M} _ {s} ^ {*} \tilde {M} _ {s}) (I + P _ {s} K _ {\infty}). \tag {16.6}$$

We will next show that $K _ { \infty }$ is invertible. Suppose that there exists an x such that $K _ { \infty } x = 0$ , then $x ^ { * } \times$ equation $( 1 6 . 6 ) \times x$ gives

$$\gamma^ {- 2} x ^ {*} x \leq x ^ {*} \tilde {M} _ {s} ^ {*} \tilde {M} _ {s} x,$$
