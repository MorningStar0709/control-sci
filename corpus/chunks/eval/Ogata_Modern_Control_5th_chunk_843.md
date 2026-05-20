# MATLAB Program 10–25

$$
\begin{array}{l} A = [ 0 \quad 1 \quad 0; 0 \quad 0 \quad 1; - 6 \quad - 1 1 \quad - 6 ]; \\ B = [ 0; 0; 1 0 ]; \\ J = \left[ - 2 + j ^ {*} 2 ^ {*} \operatorname{sqrt} (3) - 2 - J ^ {*} 2 ^ {*} \operatorname{Sqrt} (3) - 1 0 \right]; \\ K = \text { place } (A, B, J) \\ \text { place:   ndigits } = 1 5 \\ K = \\ \begin{array}{c c c} 1 5. 4 0 0 0 & 4. 5 0 0 0 & 0. 8 0 0 0 \end{array} \\ \end{array}
$$

A–10–7. Consider a completely observable system

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x}y = \mathbf {C x}$$

Define the observability matrix as N:

$$
\mathbf {N} = \left[ \begin{array}{c c c c} \mathbf {C} ^ {*} & \mathbf {A} ^ {*} \mathbf {C} ^ {*} & \dots & (\mathbf {A} ^ {*}) ^ {n - 1} \mathbf {C} ^ {*} \end{array} \right]
$$

Show that

$$
\mathbf {N} ^ {*} \mathbf {A} (\mathbf {N} ^ {*}) ^ {- 1} = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & \dots & 0 \\ 0 & 0 & 1 & \dots & 0 \\ \cdot & \cdot & \cdot & & \cdot \\ \cdot & \cdot & \cdot & & \cdot \\ \cdot & \cdot & \cdot & & \cdot \\ 0 & 0 & 0 & \dots & 1 \\ - a _ {n} & a _ {n - 1} & - a _ {n - 2} & \dots & - a _ {1} \end{array} \right] \tag {10-146}
$$

where $a _ { 1 } , a _ { 2 } , \ldots , a _ { n }$ are the coefficients of the characteristic polynomial

$$\left| s \mathbf {I} - \mathbf {A} \right| = s ^ {n} + a _ {1} s ^ {n - 1} + \dots + a _ {n - 1} s + a _ {n}$$

Solution. Let us consider the case where n=3. Then Equation (10–146) can be written as

$$
\mathbf {N} ^ {*} \mathbf {A} (\mathbf {N} ^ {*}) ^ {- 1} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - a _ {3} & - a _ {2} & - a _ {1} \end{array} \right] \tag {10-147}
$$

Equation (10–147) may be rewritten as

$$
\mathbf {N} ^ {*} \mathbf {A} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - a _ {3} & - a _ {2} & - a _ {1} \end{array} \right] \mathbf {N} ^ {*} \tag {10-148}
$$

We shall show that Equation (10–148) holds true. The left-hand side of Equation (10–148) is

$$
\mathbf {N} ^ {*} \mathbf {A} = \left[ \begin{array}{c} \mathbf {C} \\ \mathbf {C A} \\ \mathbf {C A} ^ {2} \end{array} \right] \mathbf {A} = \left[ \begin{array}{c} \mathbf {C A} \\ \mathbf {C A} ^ {2} \\ \mathbf {C A} ^ {3} \end{array} \right] \tag {10-149}
$$

The right-hand side of Equation (10–148) is
