Then the observer gain matrix $\mathbf { K } _ { e }$ can be obtained from Equation (10–61) as follows:

$$
\mathbf {K} _ {e} = (\mathbf {W N} ^ {*}) ^ {- 1} \left[ \begin{array}{c} \alpha_ {2} - a _ {2} \\ \alpha_ {1} - a _ {1} \end{array} \right] = \left[ \begin{array}{c c} 1 & 0 \\ 0 & 1 \end{array} \right] \left[ \begin{array}{c} 1 0 0 + 2 0. 6 \\ 2 0 - 0 \end{array} \right] = \left[ \begin{array}{c} 1 2 0. 6 \\ 2 0 \end{array} \right]
$$

Method 2: Referring to Equation (10–59):

$$\dot {\mathbf {e}} = \left(\mathbf {A} - \mathbf {K} _ {e} \mathbf {C}\right) \mathbf {e}$$

the characteristic equation for the observer becomes

$$\left| s \mathbf {I} - \mathbf {A} + \mathbf {K} _ {e} \mathbf {C} \right| = 0$$

Define

$$
\mathbf {K} _ {e} = \left[ \begin{array}{c} k _ {e 1} \\ k _ {e 2} \end{array} \right]
$$

Then the characteristic equation becomes

$$
\begin{array}{l} \left| \left[ \begin{array}{c c} s & 0 \\ 0 & s \end{array} \right] - \left[ \begin{array}{c c} 0 & 2 0. 6 \\ 1 & 0 \end{array} \right] + \left[ \begin{array}{c} k _ {e 1} \\ k _ {e 2} \end{array} \right] [ 0 \quad 1 ] \right| = \left| \begin{array}{c c} s & - 2 0. 6 + k _ {e 1} \\ - 1 & s + k _ {e 2} \end{array} \right| \\ = s ^ {2} + k _ {e 2} s - 2 0. 6 + k _ {e 1} = 0 \tag {10-66} \\ \end{array}
$$

Since the desired characteristic equation is

$$s ^ {2} + 2 0 s + 1 0 0 = 0$$

by comparing Equation (10–66) with this last equation, we obtain

$$k _ {e 1} = 1 2 0. 6, \quad k _ {e 2} = 2 0$$

or

$$
\mathbf {K} _ {e} = \left[ \begin{array}{c} 1 2 0. 6 \\ 2 0 \end{array} \right]
$$

Method 3: We shall use Ackermann’s formula given by Equation (10–65):

$$
\mathbf {K} _ {e} = \phi (\mathbf {A}) \left[ \begin{array}{c} \mathbf {C} \\ \mathbf {C A} \end{array} \right] ^ {- 1} \left[ \begin{array}{c} 0 \\ 1 \end{array} \right]
$$

where

$$\phi (s) = \bigl (s - \mu_ {1} \bigr) \bigl (s - \mu_ {2} \bigr) = s ^ {2} + 2 0 s + 1 0 0$$

Thus,

$$\phi (\mathbf {A}) = \mathbf {A} ^ {2} + 2 0 \mathbf {A} + 1 0 0 \mathbf {I}$$

and

$$
\begin{array}{l} \mathbf {K} _ {e} = \left(\mathbf {A} ^ {2} + 2 0 \mathbf {A} + 1 0 0 \mathbf {I}\right) \left[ \begin{array}{c c} 0 & 1 \\ 1 & 0 \end{array} \right] ^ {- 1} \left[ \begin{array}{c} 0 \\ 1 \end{array} \right] \\ = \left[ \begin{array}{c c} 1 2 0. 6 & 4 1 2 \\ 2 0 & 1 2 0. 6 \end{array} \right] \left[ \begin{array}{l l} 0 & 1 \\ 1 & 0 \end{array} \right] \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] = \left[ \begin{array}{c} 1 2 0. 6 \\ 2 0 \end{array} \right] \\ \end{array}
$$
