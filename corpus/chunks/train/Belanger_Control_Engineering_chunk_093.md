# Example 3.5 Calculate the transfer function for

$$
A = \left[ \begin{array}{c c} 0 & 1 \\ - 2 & - 3 \end{array} \right], \qquad B = \mathbf {b} = \left[ \begin{array}{c} 1 \\ 1 \end{array} \right], \qquad C = \mathbf {c} ^ {T} = \left[ \begin{array}{c c} 1 & 0 \end{array} \right], \qquad D = 0.
$$

Solution By Equation 3.19,

$$H (s) = \mathbf {c} ^ {T} (s I - A) ^ {- 1} \mathbf {b}.$$

Now, $(sI - A)^{-1}$ has already been calculated in Example 3.2. Using that result,

$$
\begin{array}{l} H (s) = \left[ \begin{array}{c c} 1 & 0 \end{array} \right] \frac {1}{s ^ {2} + 3 s + 2} \left[ \begin{array}{c c} s + 3 & 1 \\ - 2 & s \end{array} \right] \left[ \begin{array}{c} 1 \\ 1 \end{array} \right] \\ = \left[ \begin{array}{l l} 1 & 0 \end{array} \right] \frac {1}{s ^ {2} + 3 s + 2} \left[ \begin{array}{l} s + 4 \\ s - 2 \end{array} \right] \\ = \frac {s + 4}{s ^ {2} + 3 s + 2}. \\ \end{array}
$$
