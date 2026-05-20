# EXAMPLE 2–3

Consider again the mechanical system shown in Figure 2–15. State-space equations for the system are given by Equations (2–20) and (2–21).We shall obtain the transfer function for the system from the state-space equations.

By substituting A, B, C, and D into Equation (2–29), we obtain

$$
\begin{array}{l} G (s) = \mathbf {C} (s \mathbf {I} - \mathbf {A}) ^ {- 1} \mathbf {B} + D \\ = \left[ \begin{array}{c c} 1 & 0 \end{array} \right] \left\{\left[ \begin{array}{c c} s & 0 \\ 0 & s \end{array} \right] - \left[ \begin{array}{c c} 0 & 1 \\ - \frac {k}{m} & - \frac {b}{m} \end{array} \right] \right\} ^ {- 1} \left[ \begin{array}{c} 0 \\ \frac {1}{m} \end{array} \right] + 0 \\ = \left[ \begin{array}{c c} 1 & 0 \end{array} \right] \left[ \begin{array}{c c} s & - 1 \\ \frac {k}{m} & s + \frac {b}{m} \end{array} \right] ^ {- 1} \left[ \begin{array}{c} 0 \\ \frac {1}{m} \end{array} \right] \\ \end{array}
$$

Note that

$$
\left[ \begin{array}{c c} s & - 1 \\ \frac {k}{m} & s + \frac {b}{m} \end{array} \right] ^ {- 1} = \frac {1}{s ^ {2} + \frac {b}{m} s + \frac {k}{m}} \left[ \begin{array}{c c} s + \frac {b}{m} & 1 \\ - \frac {k}{m} & s \end{array} \right]
$$

(Refer to Appendix C for the inverse of the 2  2 matrix.)

Thus, we have

$$
\begin{array}{l} G (s) = \left[ \begin{array}{c c} 1 & 0 \end{array} \right] \frac {1}{s ^ {2} + \frac {b}{m} s + \frac {k}{m}} \left[ \begin{array}{c c} s + \frac {b}{m} & 1 \\ - \frac {k}{m} & s \end{array} \right] \left[ \begin{array}{c} 0 \\ \frac {1}{m} \end{array} \right] \\ = \frac {1}{m s ^ {2} + b s + k} \\ \end{array}
$$

which is the transfer function of the system. The same transfer function can be obtained from Equation (2–16).

Transfer Matrix. Next, consider a multiple-input, multiple-output system. Assume that there are r inputs $u _ { 1 } , u _ { 2 } , \ldots , u _ { r }$ and m outputs, $y _ { 1 } , y _ { 2 } , \ldots , y _ { m }$ Define.

$$
\mathbf {y} = \left[ \begin{array}{c} y _ {1} \\ y _ {2} \\ . \\ . \\ . \\ y _ {m} \end{array} \right], \quad \mathbf {u} = \left[ \begin{array}{c} u _ {1} \\ u _ {2} \\ . \\ . \\ . \\ u _ {r} \end{array} \right]
$$

The transfer matrix G(s) relates the output Y(s) to the input U(s), or

$$\mathbf {Y} (s) = \mathbf {G} (s) \mathbf {U} (s)$$

where G(s) is given by

$$\mathbf {G} (s) = \mathbf {C} (s \mathbf {I} - \mathbf {A}) ^ {- 1} \mathbf {B} + \mathbf {D}$$

[The derivation for this equation is the same as that for Equation (2–29).] Since the input vector u is r dimensional and the output vector y is m dimensional, the transfer matrix G(s) is an m\*r matrix.
