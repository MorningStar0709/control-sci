# THE ROUTH CRITERION

It was stated in the preceding section that the polynomial $D_{L}(s) + N_{L}(s)$ must be stable. This can always be verified by computing the roots and checking that the real parts are all negative. In a design context, where $D_{L}$ and $N_{L}$ are also functions of some design parameters, this could become tedious, as roots would have to be computed for several values of the design parameters.

Routh's contribution [1] was a test to ascertain, without computing roots, whether or not all roots of a polynomial had negative real parts. Given the difficulty of calculating roots in the precomputer era, Routh's work was an important step forward. The result is presented algorithmically, without proof, as it is difficult to establish without a good deal of background material.

We begin with a polynomial,

$$Q (s) = a _ {n} s ^ {n} + a _ {n - 1} s ^ {n - 1} + \dots + a _ {1} s + a _ {0}$$

with $a_{n}\neq 0$

We form the Routh array as follows. The first two rows, labeled $n$ and $n - 1$ , are:

$$
\begin{array}{c c c c c c} n & | & a _ {n} & a _ {n - 2} & a _ {n - 4} & \ldots \\ n - 1 & | & a _ {n - 1} & a _ {n - 3} & a _ {n - 5} & \ldots \end{array}
$$

The process continues until we run out of coefficients. If the last entry, $a_0$ , is in row $n$ , a zero is placed below $a_0$ in row $n - 1$ .

Row $n - 2$ is formed as follows:

$$n - 2 \quad | \quad \frac {a _ {n - 1} a _ {n - 2} - a _ {n} a _ {n - 3}}{a _ {n - 1}} \quad \frac {a _ {n - 1} a _ {n - 4} - a _ {n} a _ {n - 5}}{a _ {n - 1}} \quad \dots$$

The numerators are determinant-like quantities; they are formed in a manner similar to the determinants of $2 \times 2$ matrices, but with the order reversed. The process of forming row n - 2 continues until we run out of elements.

Subsequent rows are formed in exactly the same way, each time from the previous two rows. This process is carried out until the row label is 0.

The Routh–Hurwitz test is as follows. All roots of the polynomial $Q(s)$ have negative real parts if, and only if, the elements of the leftmost column of the array are nonzero and all have the same sign. Furthermore, the number of sign reversals encountered while scanning the column is the number of RHP roots of $Q(s)$ .

Example 5.1 Set up the Routh array for the polynomial $Q(s) = s^4 - s^3 + 3s^2 + 0s + 2$ and calculate the number of RHP roots.

Solution The first three rows are

$$
\begin{array}{c c c c c c} 4 & | & 1 & 3 & 2 & 0 \\ 3 & | & - 1 & 0 & 0 & 0 \\ 2 & | & \frac {(- 1) (3) - (1) (0)}{- 1} & \frac {(- 1) (2) - (1) (0)}{- 1} & 0 \end{array}
$$

The complete array is
