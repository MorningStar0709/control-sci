$$
\left[ \begin{array}{l} M _ {i} \\ N _ {i} \end{array} \right] = \left[ \begin{array}{c c} A _ {i} + B _ {i} F _ {i} & B _ {i} R _ {i} ^ {- 1 / 2} \\ \hline F _ {i} & R _ {i} ^ {- 1 / 2} \\ C _ {i} + D _ {i} F _ {i} & D _ {i} R _ {i} ^ {- 1 / 2} \end{array} \right], \quad \begin{array}{l} R _ {i} = I + D _ {i} ^ {*} D _ {i} \\ \tilde {R} _ {i} = I + D _ {i} D _ {i} ^ {*} \\ F _ {i} = - R _ {i} ^ {- 1} (B _ {i} ^ {*} X _ {i} + D _ {i} ^ {*} C _ {i}) \end{array}
$$

where

$$
X _ {i} = \mathrm{Ric} \left[ \begin{array}{c c} A _ {i} - B _ {i} R _ {i} ^ {- 1} D _ {i} ^ {*} C _ {i} & - B _ {i} R _ {i} ^ {- 1} B _ {i} ^ {*} \\ - C _ {i} ^ {*} \tilde {R} _ {i} ^ {- 1} C _ {i} & - (A _ {i} - B _ {i} R _ {i} ^ {- 1} D _ {i} ^ {*} C _ {i}) ^ {*} \end{array} \right].
$$

2. Define a generalized system

$$
\begin{array}{l} G (s) = \left[ \begin{array}{c c} {\left[ \begin{array}{c} M _ {1} \\ N _ {1} \end{array} \right]} & {\left[ \begin{array}{c} M _ {2} \\ N _ {2} \end{array} \right]} \\ {- I} & 0 \end{array} \right] \\ = \left[ \begin{array}{c c c c} A _ {1} + B _ {1} F _ {1} & 0 & B _ {1} R _ {1} ^ {- 1 / 2} & 0 \\ 0 & A _ {2} + B _ {2} F _ {2} & 0 & B _ {2} R _ {2} ^ {- 1 / 2} \\ \hline F _ {1} & F _ {2} & R _ {1} ^ {- 1 / 2} & R _ {2} ^ {- 1 / 2} \\ C _ {1} + D _ {1} F _ {1} & C _ {2} + D _ {2} F _ {2} & D _ {1} R _ {1} ^ {- 1 / 2} & D _ {2} R _ {2} ^ {- 1 / 2} \\ \hline 0 & 0 & - I & 0 \end{array} \right]. \\ \end{array}
$$

3. Apply standard $\mathcal { H } _ { \infty }$ algorithm to

$$
\vec {\delta} _ {g} (P _ {1}, P _ {2}) = \inf _ {Q \in \mathcal {H} _ {\infty}} \left\| \left[ \begin{array}{c} M _ {1} \\ N _ {1} \end{array} \right] - \left[ \begin{array}{c} M _ {2} \\ N _ {2} \end{array} \right] Q \right\| _ {\infty} = \inf _ {Q \in \mathcal {H} _ {\infty}} \| \mathcal {F} _ {\ell} (G, Q) \| _ {\infty} .
$$

Using the above procedure, it is easy to show that

$$\delta_ {g} \left(\frac {1}{s}, \frac {1}{s + 0 . 1}\right) = 0. 0 9 9 5,$$

which confirms that the two systems given at the beginning of this chapter are indeed close in the gap metric. This example shows an important feature about the gap metric (similarly, the ν-gap metric defined in the next section): The distance between two plants, as measured by the gap metric $\delta _ { g }$ (or the ν-gap metric $\delta _ { \nu } )$ , has very little to do with any difference between their open-loop behavior (indeed, there is no reason why it should). This point will be further illustrated by an example in the next section.

A lower bound for the gap metric can also be obtained easily without actually solving the corresponding $\mathcal { H } _ { \infty }$ optimization. Let
