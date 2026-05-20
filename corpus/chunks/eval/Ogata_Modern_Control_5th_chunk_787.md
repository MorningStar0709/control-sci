Referring to Equation (10–95), the characteristic equation for the minimum-order observer is

$$
\begin{array}{l} \left| s \mathbf {I} - \mathbf {A} _ {b b} + \mathbf {K} _ {e} \mathbf {A} _ {a b} \right| = (s - \mu_ {1}) (s - \mu_ {2}) \\ = (s + 1 0) (s + 1 0) \\ = s ^ {2} + 2 0 s + 1 0 0 = 0 \\ \end{array}
$$

In what follows, we shall use Ackermann’s formula given by Equation (10–97).

$$
\mathbf {K} _ {e} = \phi (\mathbf {A} _ {b b}) \left[ \begin{array}{c} \mathbf {A} _ {a b} \\ \dots \\ \mathbf {A} _ {a b} \mathbf {A} _ {b b} \end{array} \right] ^ {- 1} \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] \tag {10-99}
$$

where

$$\phi \left(\mathbf {A} _ {b b}\right) = \mathbf {A} _ {b b} ^ {2} + \hat {\alpha} _ {1} \mathbf {A} _ {b b} + \hat {\alpha} _ {2} \mathbf {I} = \mathbf {A} _ {b b} ^ {2} + 2 0 \mathbf {A} _ {b b} + 1 0 0 \mathbf {I}$$

Since

$$
\widetilde {\mathbf {x}} = \left[ \begin{array}{c} x _ {a} \\ \dots \\ \widetilde {\mathbf {x}} _ {b} \end{array} \right] = \left[ \begin{array}{c} x _ {1} \\ \hdashline \widetilde {x} _ {2} \\ \widetilde {x} _ {3} \end{array} \right], \qquad \mathbf {A} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ \hdashline 0 & 0 & 1 \\ - 6 & - 1 1 & - 6 \end{array} \right], \qquad \mathbf {B} = \left[ \begin{array}{c} 0 \\ \hdashline 0 \\ 1 \end{array} \right]
$$

we have

$$
A _ {a a} = 0, \qquad \mathbf {A} _ {a b} = [ 1 \quad 0 ], \qquad \mathbf {A} _ {b a} = \left[ \begin{array}{c} 0 \\ - 6 \end{array} \right]

\mathbf {A} _ {b b} = \left[ \begin{array}{c c} 0 & 1 \\ - 1 1 & - 6 \end{array} \right], \qquad B _ {a} = 0, \qquad \mathbf {B} _ {b} = \left[ \begin{array}{c} 0 \\ 1 \end{array} \right]
$$

Equation (10–99) now becomes

$$
\begin{array}{l} \mathbf {K} _ {e} = \left\{\left[ \begin{array}{c c} 0 & 1 \\ - 1 1 & - 6 \end{array} \right] ^ {2} + 2 0 \left[ \begin{array}{c c} 0 & 1 \\ - 1 1 & - 6 \end{array} \right] + 1 0 0 \left[ \begin{array}{c c} 1 & 0 \\ 0 & 1 \end{array} \right] \right\} \left[ \begin{array}{c c} 1 & 0 \\ 0 & 1 \end{array} \right] ^ {- 1} \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] \\ = \left[ \begin{array}{c c} 8 9 & 1 4 \\ - 1 5 4 & 5 \end{array} \right] \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] = \left[ \begin{array}{c} 1 4 \\ 5 \end{array} \right] \\ \end{array}
$$

(A MATLAB computation of this Ke is given in MATLAB Program 10–10.)

MATLAB Program 10–10
