We next discuss when we can solve (1.41). We also note that for constrained systems, we must impose the constraints on the steady state $( x _ { s } , u _ { s } )$ . The matrix in (1.41) is a $( n + p ) \times ( n + m )$ matrix. For (1.41) to have a solution for all $y _ { \mathrm { s p } }$ , it is sufficient that the rows of the matrix are linearly independent. That requires $p \leq m !$ : we require at least as many inputs as outputs with setpoints. But it is not uncommon in applications to have many more measured outputs than manipulated inputs. To handle these more general situations, we choose a matrix H and denote a new variable $r = H y$ as a selection of linear combinations of the measured outputs. The variable $r \in \mathbb { R } ^ { n _ { c } }$ is known as the controlled variable. For cases in which $p > m$ , we choose some set of outputs $n _ { c } \le m$ , as controlled variables, and assign setpoints to r , denoted $r _ { \mathrm { s p } }$ .

We also wish to treat systems with more inputs than outputs, $m > p$ . For these cases, the solution to (1.41) may exist for some choice of H and $r _ { \mathrm { s p } }$ , but cannot be unique. If we wish to obtain a unique steady state, then we also must provide desired values for the steady inputs, $u _ { \mathrm { s p } }$ . To handle constrained systems, we simply impose the constraints on $( x _ { s } , u _ { s } )$ .

Steady-state target problem. Our candidate optimization problem is therefore

$$\min _ {x _ {s}, u _ {s}} \frac {1}{2} \left(\left| u _ {s} - u _ {\mathrm{sp}} \right| _ {R _ {s}} ^ {2} + \left| C x _ {s} - y _ {\mathrm{sp}} \right| _ {Q _ {s}} ^ {2}\right) \tag {1.42a}$$

subject to:

$$
\left[ \begin{array}{c c} I - A & - B \\ H C & 0 \end{array} \right] \left[ \begin{array}{l} x _ {s} \\ u _ {s} \end{array} \right] = \left[ \begin{array}{l} 0 \\ r _ {\mathrm{sp}} \end{array} \right] \tag {1.42b}
E u _ {s} \leq e \tag {1.42c}F C x _ {s} \leq f \tag {1.42d}
$$

We make the following assumptions:

Assumption 1.7 (Target feasibility and uniqueness).

(a) The target problem is feasible for the controlled variable setpoints of interest $r _ { \mathrm { s p } }$ .

(b) The steady-state input penalty $R _ { s }$ is positive definite.
