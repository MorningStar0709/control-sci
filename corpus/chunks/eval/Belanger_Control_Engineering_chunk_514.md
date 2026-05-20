$$
\frac {d}{d t} \left[ \begin{array}{l} q _ {1} \\ q _ {2} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ - 6 4 6 7 & - 2 0 2. 9 \end{array} \right] \left[ \begin{array}{l} q _ {1} \\ q _ {2} \end{array} \right] + \left[ \begin{array}{l} 0 \\ 1 \end{array} \right] a

z _ {1} = \left[ \begin{array}{l l} 2 2 8 5 0 4 & 3 6 3 8 6 \end{array} \right] \left[ \begin{array}{l} q _ {1} \\ q _ {2} \end{array} \right].
$$

The acceleration, of course, is simply $\dot{v}_{1}$ . Putting the pieces together,

$$
\frac {d}{d t} \left[ \begin{array}{l} \ell_ {1} \\ \ell_ {2} \\ v _ {1} \\ v _ {2} \\ q _ {1} \\ q _ {2} \end{array} \right] = \left[ \begin{array}{c c c c c c} 0 & 0 & 1 & - 1 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 & 0 \\ - 1 0 & 0 & - 2 & 2 & 0 & 0 \\ 7 2 0 & - 6 6 0 & 1 2 & - 1 2 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 1 \\ - 1 0 & 0 & - 2 & 2 & - 6 4 6 7 & - 2 0 2. 9 \end{array} \right] \left[ \begin{array}{l} \ell_ {1} \\ \ell_ {2} \\ v _ {1} \\ v _ {2} \\ q _ {1} \\ q _ {2} \end{array} \right]

+ \left[ \begin{array}{c} 0 \\ -. 5 \\ 0 \\ 0 \\ 0 \\ 0 \end{array} \right] w + \left[ \begin{array}{c} 0 \\ 0 \\ . 0 0 3 3 4 \\ -. 0 2 \\ 0 \\ 0 \end{array} \right] u

z = \left[ \begin{array}{c c c c c c} 0 & 0 & 0 & 0 & 2 2 8 5 0 4 & 3 6 3 8 6 \\ \frac {1}{. 1 5} & 0 & 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 \end{array} \right] \left[ \begin{array}{l} \ell_ {1} \\ \ell_ {2} \\ v _ {1} \\ v _ {2} \\ q _ {1} \\ q _ {2} \end{array} \right] + \left[ \begin{array}{c} 0 \\ 0 \\ 1 / 4 5 0 \end{array} \right] u

y = \left[ \begin{array}{c c c c c c} 1 & 0 & 0 & 0 & 0 & 0 \end{array} \right] \left[ \begin{array}{c} \ell_ {1} \\ \ell_ {2} \\ v _ {1} \\ v _ {2} \\ q _ {1} \\ q _ {2} \end{array} \right].
$$

We verify controllability from the input u (MATLAB ctrb). The system is not observable from y (the weight function $W_{1}(s)$ is not connected to the output), but is nevertheless detectable (the modes contributed by $W_{1}$ are stable).

We check $D_{12}{}^T D_{12} = (1/450)^2$ . We note that $D_{21} = 0$ ; we require $D_{21}D_{21}{}^T$ to be nonsingular so we resort to fictitious measurement noise, letting $y = \ell_1 + .01n$ . This leads to two modifications:

$$
B _ {1} = \left[ \begin{array}{c c} 0 & 0 \\ -. 5 & 0 \\ 0 & 0 \\ 0 & 0 \\ 0 & 0 \\ 0 & 0 \end{array} \right] \quad \text { and } \quad D _ {2 1} = \left[ \begin{array}{l l} 0 & . 0 1 \end{array} \right].
$$

Since there is bound to be some noise in the measurement of $\ell_{1}$ , this step is surely justified. The factor of 0.01 signifies measurement errors of the order of 1 cm, since n is considered to have unit norm.
