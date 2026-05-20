$$\overline {{\sigma}} (P K) = \overline {{\sigma}} (P W _ {1} K _ {\infty} W _ {2}) \leq \overline {{\sigma}} (W _ {2} P W _ {1}) \overline {{\sigma}} (K _ {\infty}) \kappa (W _ {2}).$$

Similarly, the corresponding deterioration in plant input loop shape is obtained by comparing $\overline { { \sigma } } ( W _ { 1 } K _ { \infty } W _ { 2 } P )$ to $\overline { { \sigma } } ( W _ { 2 } P W _ { 1 } )$ , where

$$\overline {{\sigma}} (K P) = \overline {{\sigma}} (W _ {1} K _ {\infty} W _ {2} P) \leq \overline {{\sigma}} (W _ {2} P W _ {1}) \overline {{\sigma}} (K _ {\infty}) \kappa (W _ {1}).$$

Hence, in each case, $\overline { { \sigma } } ( K _ { \infty } )$ is required to obtain a bound on the deterioration in the loop shape at high-frequency. In an identical manner to Theorem 16.10, we now show that $\overline { { \sigma } } ( K _ { \infty } )$ is explicitly bounded by functions of $\gamma$ and $\overline { { \sigma } } ( P _ { s } )$ , the maximum singular value of the shaped plant.

Theorem 16.11 Any controller $K _ { \infty }$ satisfying equation (16.5) also satisfies

$$\overline {{\sigma}} (K _ {\infty} (j \omega)) \leq \frac {\sqrt {\gamma^ {2} - 1} + \overline {{\sigma}} (P _ {s} (j \omega))}{1 - \sqrt {\gamma^ {2} - 1} \overline {{\sigma}} (P _ {s} (j \omega))}$$

for all ω such that

$$\overline {{\sigma}} (P _ {s} (j \omega)) < \frac {1}{\sqrt {\gamma^ {2} - 1}}.$$

Furthermore, $\mathit { i f } \overline { { \sigma } } ( P _ { s } ) \ll 1 / \sqrt { \gamma ^ { 2 } - 1 }$ , then $\overline { { \sigma } } ( K _ { \infty } ( j \omega ) )$ / $\sqrt { \gamma ^ { 2 } - 1 }$ , where $\lessapprox$ denotes asymptotically less than or equal to as $\overline { { \sigma } } ( P _ { s } )  0$ .

Proof. The proof of Theorem 16.11 is similar to that of Theorem 16.10 and is only sketched here: As in the proof of Theorem 16.10, we have $\tilde { M } _ { s } ^ { * } \tilde { M } _ { s } = ( I + P _ { s } P _ { s } ^ { * } ) ^ { - 1 }$ and

$$(I + K _ {\infty} ^ {*} K _ {\infty}) \leq \gamma^ {2} (I + K _ {\infty} ^ {*} P _ {s} ^ {*}) (\tilde {M} _ {s} ^ {*} \tilde {M} _ {s}) (I + P _ {s} K _ {\infty}). \tag {16.9}$$

Since $\begin{array} { r } { \overline { { \sigma } } ( P _ { s } ) < \frac { 1 } { \sqrt { \gamma ^ { 2 } - 1 } } } \end{array}$ γ 2 1

$$I - \gamma^ {2} P _ {s} ^ {*} (I + P _ {s} P _ {s} ^ {*}) ^ {- 1} P _ {s} > 0$$

and there exists a spectral factorization

$$V ^ {*} V = I - \gamma^ {2} P _ {s} ^ {*} (I + P _ {s} P _ {s} ^ {*}) ^ {- 1} P _ {s}.$$

Now, completing the square in equation (16.9) with respect to $K _ { \infty }$ yields

$$(K _ {\infty} ^ {*} + M ^ {*}) V ^ {*} V (K _ {\infty} + M) \leq (\gamma^ {2} - 1) Y ^ {*} Y$$

where
