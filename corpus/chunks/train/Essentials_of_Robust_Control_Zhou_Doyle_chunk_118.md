$$
u (t) = \left[ \begin{array}{c} u _ {1} \sin (\omega_ {0} t + \phi_ {1}) \\ u _ {2} \sin (\omega_ {0} t + \phi_ {2}) \\ \vdots \\ u _ {q} \sin (\omega_ {0} t + \phi_ {q}) \end{array} \right], \quad \hat {u} = \left[ \begin{array}{c} u _ {1} \\ u _ {2} \\ \vdots \\ u _ {q} \end{array} \right].
$$

Show that the steady-state response of the system is given by

$$
y (t) = \left[ \begin{array}{c} y _ {1} \sin (\omega_ {0} t + \theta_ {1}) \\ y _ {2} \sin (\omega_ {0} t + \theta_ {2}) \\ \vdots \\ y _ {p} \sin (\omega_ {0} t + \theta_ {p}) \end{array} \right], \quad \hat {y} = \left[ \begin{array}{c} y _ {1} \\ y _ {2} \\ \vdots \\ y _ {p} \end{array} \right]
$$

for some $y _ { i }$ and $\theta _ { i } , ~ i = 1 , 2 , \ldots , p .$ Show that $\operatorname* { s u p } _ { \phi _ { i } , \omega _ { o } , \| \hat { \boldsymbol u } \| _ { 2 } \leq 1 } \| \hat { \boldsymbol y } \| _ { 2 } = \| \boldsymbol G \| _ { \infty } .$ .

Problem 4.7 Write a Matlab program to plot, versus $\gamma$ , the distance from the imaginary axis to the nearest eigenvalue of the Hamiltonian matrix for a given state-space model with stable A. Try it on

$$
\left[ \begin{array}{c c} \frac {s + 1}{(s + 2) (s + 3)} & \frac {s}{s + 1} \\ \frac {s ^ {2} - 2}{(s + 3) (s + 4)} & \frac {s + 4}{(s + 1) (s + 2)} \end{array} \right].
$$

Read off the value of the $\mathcal { H } _ { \infty }$ -norm. Compare with the Matlab function hinfnorm.

Problem 4.8 Let $G ( s ) = { \frac { 1 } { ( s ^ { 2 } + 2 \xi s + 1 ) ( s + 1 ) } }$ . Compute $\| G ( s ) \| _ { \infty }$ using the Bode plot and state-space algorithm, respectively for $\xi = 1 , 0 . 1 , 0 . 0 1 , 0 . 0 0 1$ and compare the results.
