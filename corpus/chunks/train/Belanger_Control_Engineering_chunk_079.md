# 3.3.2 Solution by Laplace Transforms

An aphorism credited to A. J. Laub is stated as follows: "If it's a good method for hand calculation, it's a poor method for computer implementation; if it's a good numerical method, it's a poor one for pencil and paper." This holds true for the computation of the matrix exponential: the series evaluation is difficult to do by hand, so we rely on a Laplace transform solution.

Transformation of Equation 3.4 and use of the real differentiation theorem yield

$$s \mathbf {x} (s) - \mathbf {x} (0) = A \mathbf {x} (s)$$

or

$$(s I - A) \mathbf {x} (s) = \mathbf {x} (0)$$

and

$$\mathbf {x} (s) = (s I - A) ^ {- 1} \mathbf {x} (0). \tag {3.10}$$

(Note the introduction of the $n \times n$ identity matrix $I$ in the second step, so as to have a difference of two $n \times n$ matrices in the parentheses.)

Now

$$\mathbf {x} (t) = e ^ {A t} \mathbf {x} (0).$$

Transformation of each side yields

$$\mathbf {x} (s) = \mathcal {L} [ e ^ {A t} ] \mathbf {x} (0).$$

Comparing this with Equation 3.10, we obtain

$$\mathcal {L} [ e ^ {A t} ] = (s I - A) ^ {- 1}. \tag {3.11}$$

Example 3.1 Calculate $e^{At}$ for $A = \begin{bmatrix} 0 & 1 \\ -2 & -3 \end{bmatrix}$ .

Solution

$$
\begin{array}{l} s I - A = \left[ \begin{array}{l l} s & 0 \\ 0 & s \end{array} \right] - \left[ \begin{array}{c c} 0 & 1 \\ - 2 & - 3 \end{array} \right] \\ = \left[ \begin{array}{c c} s & - 1 \\ 2 & s + 3 \end{array} \right]. \\ \end{array}
$$

Now,

$$\det (s I - A) = s ^ {2} + 3 s + 2$$

and

$$
\begin{array}{l} (s I - A) ^ {- 1} = \frac {1}{s ^ {2} + 3 s + 2} \left[ \begin{array}{c c} s + 3 & 1 \\ - 2 & s \end{array} \right] \\ = \frac {1}{(s + 1) (s + 2)} \left[ \begin{array}{c c} s + 3 & 1 \\ - 2 & s \end{array} \right]. \\ \end{array}
$$

To obtain $e^{At}$ , we invert each of the four elements of the matrix by partial fraction expansion.

$$
(s I - A) ^ {- 1} = \left[ \begin{array}{c c} \frac {2}{s + 1} - \frac {1}{s + 2} & \frac {1}{s + 1} - \frac {1}{s + 2} \\ \frac {- 2}{s + 1} + \frac {2}{s + 2} & \frac {- 1}{s + 1} + \frac {2}{s + 2} \end{array} \right]
$$

and

$$
e ^ {A t} = \left[ \begin{array}{c c} 2 e ^ {- t} - e ^ {- 2 t} & e ^ {- t} - e ^ {- 2 t} \\ - 2 e ^ {- t} + 2 e ^ {- 2 t} & - e ^ {- t} + 2 e ^ {- 2 t} \end{array} \right].
$$

Property I provides an easy check, and it is seen that the identity matrix results if $t = 0$ .
