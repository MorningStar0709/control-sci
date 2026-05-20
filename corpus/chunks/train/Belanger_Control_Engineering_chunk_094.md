# Example 3.6 (dc Servo)

Calculate the transfer function $\theta / v$ and $\theta / T_L$ for the system of Equation 2.19, Example 2.1 (Chapter 2).

Solution In this case,

$$
A = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 4. 4 3 8 \\ 0 & - 1 2 & - 2 4 \end{array} \right], \quad B = \left[ \begin{array}{c c} 0 & 0 \\ 0 & - 7. 3 9 6 \\ 2 0 & 0 \end{array} \right], \quad C = \left[ \begin{array}{l l l} 1 & 0 & 0 \end{array} \right].
$$

The first column of $B$ is used to compute $\theta / v$ , the second to obtain $\theta / T_L$ . The results are

$$\frac {\theta}{v} = \frac {8 8 . 7 6}{s (s + 2 1 . 5 2 6) (s + 2 . 4 7 4)} \tag {3.21}\frac {\theta}{T _ {L}} = \frac {- 7 . 3 9 6 (s + 2 4)}{s (s + 2 1 . 5 2 6) (s + 2 . 4 7 4)}. \tag {3.22}$$

For future reference, other transfer functions are computed (MATLAB ss2zp) for the examples of Chapter 2. They are as follows:

For Example 2.2 (active suspension), with $y = x_{1} - x_{2}$ ( $C = [1 - 100]$ ),

$$\frac {y}{u} = \frac {. 0 2 3 3 4 (s ^ {2} + 8 5 . 8 6 1)}{(s ^ {2} + 1 2 . 3 0 5 s + 6 3 9 . 7 6) (s ^ {2} + 1 . 6 9 5 4 s + 9 . 3 7 8 7)} \tag {3.23}\frac {y}{y _ {R}} = \frac {- 6 0 0 s ^ {2}}{(s ^ {2} + 1 2 . 3 0 5 s + 6 3 9 . 7 6) (s ^ {2} + 1 . 6 9 5 4 s + 9 . 3 7 8 7)}. \tag {3.24}$$

For Example 2.8 (level control), with $F_{d} = .01 \, \mathrm{m}^{3}/\mathrm{s}$ , $\ell_{d} = 1 \, \mathrm{m}$ ,

$$\frac {\Delta \ell}{\Delta u} = \frac {- 2 . 0}{s + . 0 0 5} \tag {3.25}\frac {\Delta \ell}{\Delta F _ {\mathrm{in}}} = \frac {1}{s + . 0 0 5}. \tag {3.26}$$

For Example 2.9 (pendulum on a cart), with $y = x$ ,

$$\frac {x}{F} = \frac {(s + 3 . 1 3 0 5) (s - 3 . 1 3 0 5)}{s ^ {2} (s - 4 . 4 2 7 2) (s + 4 . 4 2 7 2)}. \tag {3.27}$$
