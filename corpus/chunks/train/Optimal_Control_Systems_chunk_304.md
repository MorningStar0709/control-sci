# Example 5.6

We now illustrate the previous procedure by considering the same system of the Example 5.3. Let us say that we are interested in tracking $x_{1}(k)$ with respect to the desired trajectory $z_{1}(k)=2$ and we do not have any condition on the second state $x_{2}(k)$ . Then the various matrices are

$$
\mathbf {A} (k) = \left[ \begin{array}{l l} 0. 8 & 1. 0 \\ 0. 0 & 0. 6 \end{array} \right]; \quad \mathbf {B} (k) = \left[ \begin{array}{l} 1. 0 \\ 0. 5 \end{array} \right]; \mathbf {C} = \left[ \begin{array}{l l} 1 & 0 \\ 0 & 1 \end{array} \right]

\mathbf {F} \left(k _ {f}\right) = \left[ \begin{array}{l l} 1 & 0 \\ 0 & 0 \end{array} \right]; \quad \mathbf {Q} (k) = \left[ \begin{array}{l l} 1 & 0 \\ 0 & 0 \end{array} \right]; \quad \mathbf {R} = 0. 0 1. \tag {5.5.26}
$$

Now let us use the procedure given in Table 5.5. Note that one has to try various values of the matrix $\mathbf{R}$ in order to get a better tracking of the states.

The various solutions obtained using MATLAB $^{©}$ Version 6. Figure 5.13 shows Riccati functions $p_{11}(k), p_{12}(k)$ , and $p_{22}(k)$ ; Figure 5.14 shows vector coefficients $g_{1}(k)$ and $g_{2}(k)$ ; Figure 5.6 gives the optimal states and Figure 5.6 gives optimal control.

The MATLAB $^{©}$ program used is given in Appendix C.

Table 5.5 Procedure Summary of Discrete-Time Linear Quadratic Tracking System
