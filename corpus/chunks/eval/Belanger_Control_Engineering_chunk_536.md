$$
\begin{array}{l} \mathcal {Z} [ \widehat {y} (k + 1) ] = \sum_ {k ^ {\prime} = 1} ^ {\infty} \widehat {y} (k ^ {\prime}) z ^ {- k ^ {\prime} + 1} \\ = z \left[ \sum_ {k ^ {\prime} = 0} ^ {\infty} \widehat {y} (k ^ {\prime}) z ^ {- k ^ {\prime}} - \widehat {y} (0) \right] \\ = z [ \widehat {y} (z) - \widehat {y} (0) ]. \\ \end{array}
$$

■ Theorem 9.3 Complex Differentiation Theorem

$$\mathcal {Z} [ k \widehat {y} (k) ] = z ^ {- 1} \frac {d}{d z ^ {- 1}} \widehat {y} (z).$$

Proof:

$$
\begin{array}{l} \frac {d}{d z ^ {- 1}} \widehat {y} (z) = \sum_ {k = 0} ^ {\infty} k \widehat {y} (k) (z ^ {- 1}) ^ {k - 1} \\ = z \mathcal {Z} [ k \widehat {y} (k) ]. \\ \end{array}
$$

■ Theorem 9.4 Initial-Value Theorem

$$\widehat {y} (k) \mid_ {k = 0} = \lim _ {z \rightarrow \infty} \widehat {y} (z).$$

Proof: Obvious from the definition.

■ Theorem 9.5 Final-Value Theorem If it exists, the asymptotic value of $\widehat{y}(k)$ is

$$\lim _ {k \rightarrow \infty} \widehat {y} (k) = \lim _ {z \rightarrow 1} (z - 1) \widehat {y} (z).$$

Proof: By partial fractions, this operation computes the step component of $\widehat{y}(z)$ .

Example 9.3 Compute the $z$ -transform of $ka^k u_{-1}(k)$ .

Solution We apply the complex differentiation theorem. We have

$$\mathcal {Z} [ a ^ {k} ] = \frac {z}{z - a} = \frac {1}{1 - a z ^ {- 1}}\mathcal {Z} [ k a ^ {k} ] = z ^ {- 1} \frac {a}{(1 - a z ^ {- 1}) ^ {2}} = \frac {a z}{(z - a) ^ {2}}.$$

As in the case of Laplace transforms, the partial fraction expansion is the principal tool for the inversion of the z-transform. The following examples demonstrate this.

Example 9.4 Invert $\widehat{y}(z) = [z(z + 1)] / [(z - 1)(z - .5)^2]$ .

Solution We save the z from the numerator, and write

$$\frac {z + 1}{(z - 1) (z -. 5) ^ {2}} = \frac {8}{z - 1} - \frac {3}{(z -. 5) ^ {2}} - \frac {8}{z -. 5}$$

and

$$\widehat {y} (z) = 8 \frac {z}{z - 1} - 3 \frac {z}{(z - . 5) ^ {2}} - 8 \frac {z}{z - . 5}.$$

Using the results of Example 9.3,

$$\widehat {y} (k) = 8 - 6 k (. 5) ^ {k} - 8 (. 5) ^ {k}, \quad k \geq 0.$$

Example 9.5 Invert $\widehat{y}(z) = (z + .5) / [z(z + .7)(z - .7)]$ .

Solution

$$\frac {(z + . 5)}{(z + . 7) (z - . 7)} = \frac {0 . 1 4 3}{z + . 7} + \frac {0 . 8 5 7}{z - . 7}$$

and

$$\widehat {y} (z) = z ^ {- 2} \left[ 0. 1 4 3 \frac {z}{z + . 7} + 0. 8 5 7 \frac {z}{z - . 7} \right]. \tag {9.14}$$

The bracketed expression is the transform of $\widehat{y}(k) = 0.143(-.7)^k + 0.857(.7)^k$ . If we apply the delay theorem twice, we obtain

$$\mathcal {Z} [ \widehat {y} (k - 2) u _ {- 1} (k - 2) ] = z ^ {- 2} \widehat {y} (z)$$

so the inversion yields

$$\widehat {y} (k) = [ 0. 1 4 3 (-. 7) ^ {k - 2} + 0. 8 5 7 (. 7) ^ {k - 2} ] u _ {- 1} (k - 2).$$
