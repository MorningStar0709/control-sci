# Solution

The definition of conditional density gives

$$p _ {\xi | \eta} (x | y) = \frac {p _ {\xi , \eta} (x , y)}{p _ {\eta} (y)}$$

Because $( \xi , \eta )$ is jointly normal, we know from Example A.38

$$p _ {\eta} (y) = \frac {1}{(2 \pi) ^ {n _ {\eta / 2}} (\det P _ {y}) ^ {1 / 2}} \exp \left(- (1 / 2) (y - m _ {y}) ^ {\prime} P _ {y} ^ {- 1} (y - m _ {y})\right)$$

and therefore

$$
p _ {\xi | \eta} (x | y) = \frac {(\det P _ {y}) ^ {1 / 2}}{(2 \pi) ^ {n _ {\xi} / 2} \left(\det \left[ \begin{array}{c c} P _ {x} & P _ {x y} \\ P _ {y x} & P _ {y} \end{array} \right]\right) ^ {1 / 2}} \exp (- 1 / 2 a) \tag {A.36}
$$

in which the argument of the exponent is

$$
a = \left[ \begin{array}{c} x - m _ {x} \\ y - m _ {y} \end{array} \right] ^ {\prime} \left[ \begin{array}{c c} P _ {x} & P _ {x y} \\ P _ {y x} & P _ {y} \end{array} \right] ^ {- 1} \left[ \begin{array}{c} x - m _ {x} \\ y - m _ {y} \end{array} \right] - (y - m _ {y}) ^ {\prime} P _ {y} ^ {- 1} (y - m _ {y})
$$

If we use $P = P _ { x } - P _ { x y } P _ { y } ^ { - 1 } P _ { y x }$ as defined in (A.35) then we can use the partitioned matrix inversion formula to express the matrix inverse in the previous equation as

$$
\left[ \begin{array}{c c} P _ {x} & P _ {x y} \\ P _ {y x} & P _ {y} \end{array} \right] ^ {- 1} = \left[ \begin{array}{c c} P ^ {- 1} & - P ^ {- 1} P _ {x y} P _ {y} ^ {- 1} \\ - P _ {y} ^ {- 1} P _ {y x} P ^ {- 1} & P _ {y} ^ {- 1} + P _ {y} ^ {- 1} P _ {y x} P ^ {- 1} P _ {x y} P _ {y} ^ {- 1} \end{array} \right]
$$

Substituting this expression and multiplying out terms yields

$$
\begin{array}{l} a = (x - m _ {x}) ^ {\prime} P ^ {- 1} (x - m _ {x}) - 2 (y - m _ {y}) ^ {\prime} (P _ {y} ^ {- 1} P _ {y x} P ^ {- 1}) (x - m _ {x}) \\ + (y - m _ {y}) ^ {\prime} (P _ {y} ^ {- 1} P _ {y x} P ^ {- 1} P _ {x y} P _ {y} ^ {- 1}) (y - m _ {y}) \\ \end{array}
$$

which is the expansion of the following quadratic term

$$a = \left[ (x - m _ {x}) - P _ {x y} P _ {y} ^ {- 1} (y - m _ {y}) \right] ^ {\prime} P ^ {- 1} \left[ (x - m _ {x}) - P _ {x y} P _ {y} ^ {- 1} (y - m _ {y}) \right]$$

in which we use the fact that $P _ { x y } = P _ { y x } ^ { \prime }$ . Substituting (A.34) into this expression yields

$$a = (x - m) ^ {\prime} P ^ {- 1} (x - m) \tag {A.37}$$

Finally noting that for the partitioned matrix

$$
\det \left[ \begin{array}{l l} P _ {x} & P _ {x y} \\ P _ {y x} & P _ {y} \end{array} \right] = \det P _ {y} \det P \tag {A.38}
$$

and substitution of equations (A.38) and (A.37) into (A.36) yields

$$p _ {\xi | \eta} (x | y) = \frac {1}{(2 \pi) ^ {n _ {\xi / 2}} (\det P) ^ {1 / 2}} \exp \left(- \frac {1}{2} (x - m) ^ {\prime} P ^ {- 1} (x - m)\right)$$

which is the desired result.
