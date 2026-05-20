$$
H \left[ \begin{array}{l} X _ {1} \\ X _ {2} \end{array} \right] = \left[ \begin{array}{l} X _ {1} \\ X _ {2} \end{array} \right] H _ {-}.
$$

(H is a matrix representation of $H | _ { \mathcal { X } _ { - } ( H ) \cdot } )$ Premultiply this equation by

$$
\left[ \begin{array}{c} X _ {1} \\ X _ {2} \end{array} \right] ^ {*} J
$$

to get

$$
\left[ \begin{array}{l} X _ {1} \\ X _ {2} \end{array} \right] ^ {*} J H \left[ \begin{array}{l} X _ {1} \\ X _ {2} \end{array} \right] = \left[ \begin{array}{l} X _ {1} \\ X _ {2} \end{array} \right] ^ {*} J \left[ \begin{array}{l} X _ {1} \\ X _ {2} \end{array} \right] H _ {-}. \tag {12.5}
$$

Since JH is symmetric, so is the left-hand side of equation (12.5) and so is the right-hand side:

$$
\begin{array}{l} (- X _ {1} ^ {*} X _ {2} + X _ {2} ^ {*} X _ {1}) H _ {-} = H _ {-} ^ {*} (- X _ {1} ^ {*} X _ {2} + X _ {2} ^ {*} X _ {1}) ^ {*} \\ = - H _ {-} ^ {*} \left(- X _ {1} ^ {*} X _ {2} + X _ {2} ^ {*} X _ {1}\right). \\ \end{array}
$$

This is a Lyapunov equation. Since H is stable, the unique solution is

$$- X _ {1} ^ {*} X _ {2} + X _ {2} ^ {*} X _ {1} = 0.$$

This proves equation (12.4). Hence $X : = X _ { 2 } X _ { 1 } ^ { - 1 } = ( X _ { 1 } ^ { - 1 } ) ^ { * } ( X _ { 1 } ^ { * } X _ { 2 } ) X _ { 1 } ^ { - 1 }$ is Hermitian. Since $X _ { 1 }$ and $X _ { 2 }$ can always be chosen to be real and X is unique, X is real symmetric.

(ii) Start with the equation

$$
H \left[ \begin{array}{l} X _ {1} \\ X _ {2} \end{array} \right] = \left[ \begin{array}{l} X _ {1} \\ X _ {2} \end{array} \right] H _ {-}
$$

and postmultiply by $X _ { 1 } ^ { - 1 }$ to get

$$
H \left[ \begin{array}{l} I \\ X \end{array} \right] = \left[ \begin{array}{l} I \\ X \end{array} \right] X _ {1} H _ {-} X _ {1} ^ {- 1}. \tag {12.6}
$$

Now pre-multiply by $\begin{array} { r l } { [ X } & { { } - I ] } \end{array}$ :

$$
[ X \quad - I ] H \left[ \begin{array}{c} I \\ X \end{array} \right] = 0.
$$

This is precisely the Riccati equation.

(iii) Premultiply equation (12.6) by $\begin{array} { r l } { [ I } & { { } 0 ] } \end{array}$ to get

$$A + R X = X _ {1} H _ {-} X _ {1} ^ {- 1}.$$

Thus $A + R X$ is stable because $H _ { - } \ \mathrm { i s . }$ .

![](image/e5c8bff5a7b27b58d321922d910d1b6510ed0257dfa5e0b616b70fb046be4db0.jpg)

Now we are going to state one of the main theorems of this section; it gives the necessary and sufficient conditions for the existence of a unique stabilizing solution of equation (12.1) under certain restrictions on the matrix R.
