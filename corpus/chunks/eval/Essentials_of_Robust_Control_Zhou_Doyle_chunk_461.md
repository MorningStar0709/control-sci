$$
\left[ \begin{array}{l} M _ {i} \\ N _ {i} \end{array} \right] = \left[ \begin{array}{c c} A _ {i} + B _ {i} F _ {i} & B _ {i} R _ {i} ^ {- 1 / 2} \\ \hline F _ {i} & R _ {i} ^ {- 1 / 2} \\ C _ {i} + D _ {i} F _ {i} & D _ {i} R _ {i} ^ {- 1 / 2} \end{array} \right], \quad \begin{array}{l} R _ {i} = I + D _ {i} ^ {*} D _ {i} \\ \tilde {R} _ {i} = I + D _ {i} D _ {i} ^ {*} \\ F _ {i} = - R _ {i} ^ {- 1} (B _ {i} ^ {*} X _ {i} + D _ {i} ^ {*} C _ {i}) \end{array}
$$

where

$$
X _ {i} = \text {Ric} \left[ \begin{array}{c c} A _ {i} - B _ {i} R _ {i} ^ {- 1} D _ {i} ^ {*} C _ {i} & - B _ {i} R _ {i} ^ {- 1} B _ {i} ^ {*} \\ - C _ {i} ^ {*} \tilde {R} _ {i} ^ {- 1} C _ {i} & - (A _ {i} - B _ {i} R _ {i} ^ {- 1} D _ {i} ^ {*} C _ {i}) ^ {*} \end{array} \right].
$$

2. Compute the zeros of

$$
\Theta (s) := N _ {2} ^ {\sim} N _ {1} + M _ {2} ^ {\sim} M _ {1} = \left[ \begin{array}{c} M _ {2} \\ N _ {2} \end{array} \right] ^ {\sim} \left[ \begin{array}{c} M _ {1} \\ N _ {1} \end{array} \right].
$$

Let $n _ { 0 } =$ number of imaginary axis zeros of $\Theta , n _ { + } =$ number of open right-half plane zeros of Θ, and $n =$ number of open right-half plane poles of Θ. Then wno det $\left( N _ { 2 } ^ { \sim } N _ { 1 } + M _ { 2 } ^ { \sim } M _ { 1 } \right) = n _ { + } - n$ .

3. If either $n _ { 0 } \neq 0 \mathrm { o r } n _ { + } \neq n , \delta _ { \nu } ( P _ { 1 } , P _ { 2 } ) = 1$ . Otherwise, $\delta _ { \nu } ( P _ { 1 } , P _ { 2 } ) = \| \Psi ( P _ { 1 } , P _ { 2 } ) \| _ { \infty }$ with $\Psi ( P _ { 1 } , P _ { 2 } ) = - \tilde { N } _ { 2 } M _ { 1 } + \tilde { M } _ { 2 } N _ { 1 }$ :

$$
\left[ \begin{array}{c} \tilde {M} _ {i} \\ \tilde {N} _ {i} \end{array} \right] = \left[ \begin{array}{c c c} A _ {i} + L _ {i} C _ {i} & L _ {i} & B _ {i} + L _ {i} D _ {i} \\ \hline \tilde {R} _ {i} ^ {- 1 / 2} C _ {i} & \tilde {R} _ {i} ^ {- 1 / 2} & \tilde {R} _ {i} ^ {- 1 / 2} D _ {i} \end{array} \right]
L _ {i} = - (B _ {i} D _ {i} ^ {*} + Y _ {i} C _ {i} ^ {*}) \tilde {R} _ {i} ^ {- 1}
$$

where

$$
Y _ {i} = \mathrm{Ric} \left[ \begin{array}{c c} (A _ {i} - B _ {i} D _ {i} ^ {*} \tilde {R} _ {i} ^ {- 1} C _ {i}) ^ {*} & - C _ {i} ^ {*} \tilde {R} _ {i} ^ {- 1} C _ {i} \\ - B _ {i} R _ {i} ^ {- 1} B _ {i} ^ {*} & - (A _ {i} - B _ {i} D _ {i} ^ {*} \tilde {R} _ {i} ^ {- 1} C _ {i}) \end{array} \right].
$$

The Matlab command nugap can be used to carry out the preceding computation:

$$\gg \delta_ {\nu} (\mathbf {P _ {1}}, \mathbf {P _ {2}}) = \operatorname{nugap} (\mathbf {P _ {1}}, \mathbf {P _ {2}}, \operatorname{tol})$$

where tol is the computational tolerance.

Example 17.4 Consider, for example, $P _ { 1 } = 1$ and $P _ { 2 } = { \frac { 1 } { s } } .$ Then

$$M _ {1} = N _ {1} = \frac {1}{\sqrt {2}}, \quad M _ {2} = \frac {s}{s + 1}, \quad N _ {2} = \frac {1}{s + 1}.$$

Hence
