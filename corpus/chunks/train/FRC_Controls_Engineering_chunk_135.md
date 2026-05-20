# 6.4 Eigenvalues and stability

If a system is stable, its output will tend toward equilibrium (steady-state) over time. For a general system $\dot { \mathbf { x } } = f ( \mathbf { x } , \mathbf { u } )$ , equilibrium points are points where x˙ = 0. If we let x = 0 and u = 0 in x˙ = Ax + Bu, we can see that x˙ = 0, so x = 0 is an equilibrium point.

We’d like to know whether all possible unforced system trajectories (u = 0) move toward or away from the equilibrium point. If we solve the system of linear differential equations $\dot { \mathbf { x } } = \mathbf { A } \mathbf { x }$ , we get $\mathbf { x } ( t ) = e ^ { \mathbf { \bar { A } } t } \mathbf { x } _ { 0 } . ^ { [ 1 ] } \ e ^ { \mathbf { A } t }$ is the superposition of $e ^ { \lambda _ { j } t }$ terms where $\{ \lambda _ { j } \}$ is the set of A’s eigenvalues.[2]

For now, let’s consider when all the eigenvalues are real numbers.

$$
\left\{ \begin{array}{l l} \lambda_ {j} <   0, & e ^ {\lambda_ {j} t} \text {   decays   to   zero   (stable) } \\ \lambda_ {j} = 0, & e ^ {\lambda_ {j} t} = 1 \text {(marginally   stable)} \\ \lambda_ {j} > 0, & e ^ {\lambda_ {j} t} \text {   grows   to   infinity   (unstable) } \end{array} \right.
$$

So the system tends toward the equilibrium point (i.e., it’s stable) if $\lambda _ { j } < 0$ for all j.

Now let’s consider when the eigenvalues are complex numbers. What does that mean for the system response? Let $\lambda _ { j } = a _ { j } + b _ { j } i$ . Each of the exponential terms in the solution can be written as

$$e ^ {\lambda_ {j} t} = e ^ {(a _ {j} + b _ {j} i) t} = e ^ {a _ {j} t} e ^ {i b _ {j} t}$$

The complex exponential can be rewritten using Euler’s formula.[3]

$$e ^ {i b _ {j} t} = \cos (b _ {j} t) + i \sin (b _ {j} t)$$

Therefore,

$$e ^ {\lambda_ {j} t} = e ^ {a _ {j} t} (\cos (b _ {j} t) + i \sin (b _ {j} t))$$

When the eigenvalue’s imaginary part $b _ { j } \neq 0$ , it contributes oscillation to the real part’s response.

The eigenvalues of A are called poles.[4] Figure 6.1 shows the impulse responses in the time domain for systems with various pole locations in the complex plane (real numbers on the x-axis and imaginary numbers on the y-axis). Each response has an initial condition of 1.

Poles in the left half-plane (LHP) are stable; the system’s output may oscillate but it converges to steady-state. Poles on the imaginary axis are marginally stable; the system’s output oscillates at a constant amplitude forever. Poles in the right half-plane (RHP) are unstable; the system’s output grows without bound.
