$$
\begin{array}{l} \dot {\mathbf {x}} = \left[ \begin{array}{c c c c c} 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 1 \\ 0 & - 4 & 0 & 5 & 0 \end{array} \right] \mathbf {x} + \left[ \begin{array}{l} 2. 0 6 2 5 \\ 0. 1 2 5 0 \\ 2. 2 5 0 0 \\ 0. 5 0 0 0 \\ 3. 0 0 0 0 \end{array} \right] u \\ y = \left[ \begin{array}{l l l l l} 0 & . 6 6 6 7 & -. 6 6 6 7 & -. 6 6 6 7 & 1. 1 6 6 7 \end{array} \right] \mathbf {x} \\ \end{array}
$$

and express it in terms of the canonical decomposition.

M

3.44 Express in terms of the canonical decomposition the following Jordan form realizations:

$$
\begin{array}{l} \dot {\mathbf {x}} = \left[ \begin{array}{c c c c c} 1 & 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & - 1 & 1 \\ 0 & 0 & 0 & 0 & - 1 \end{array} \right] \mathbf {x} + \left[ \begin{array}{l} 1 \\ 0 \\ 1 \\ 0 \\ 1 \end{array} \right] u \\ y = \left[ \begin{array}{c c c c c} 0 & 1 & 1 & 1 & 0 \end{array} \right] \mathbf {x}. \\ \end{array}
$$

M

3.45 Compute the transfer function $y / u$ for the system of Problem 3.43, cancelling common factors. What can be concluded from pole-zero cancellations about the controllability and/or observability of the system modes?

M

3.46 Drum speed control It is sometimes possible to convert a multi-input, multi-output problem to a number of independent SISO problems. Consider the system of Problem 2.6 (Chapter 2). Define two new inputs: a common-mode input, $u_{c} = (u_{1} + u_{2}) / 2$ , and a differential-mode input, $u_{d} = (u_{1} - u_{2}) / 2$ . Clearly, $u_{1} = u_{c} + u_{d}$ and $u_{2} = u_{c} - u_{d}$ .

a. Redefine the $B$ matrix using the new inputs.   
b. Define the two outputs $y_{1} = \omega_{0}$ and $y_{2} = \omega_{1} - \omega_{2}$ . Calculate the transfer function between the vector input $\begin{bmatrix} u_{c}\\ u_{d}\end{bmatrix}$ and the vector output $\begin{bmatrix} y_{1}\\ y_{2}\end{bmatrix}$ and show that it is diagonal (within numerical accuracy).   
c. Assess the controllability of the system from $u_{c}$ , then from $u_{d}$ , and relate the results to part (b).

3.47 Blending tank For the linearized system of Problem 2.13 (Chapter 2):

a. Calculate the transformation matrix $T$ relating the state vectors

$$
\left[ \begin{array}{c} \Delta \ell \\ \Delta V _ {A} \end{array} \right] \quad \text { to } \quad \left[ \begin{array}{c} \Delta \ell \\ \Delta C s \end{array} \right],
$$

i.e., such that
