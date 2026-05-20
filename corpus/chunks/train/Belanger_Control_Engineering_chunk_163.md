# Problems

3.1 An LTI system with two states and one output has the following zero-input responses:

$$
y (t) = e ^ {- t} -. 5 e ^ {- 2 t} \quad \text { if } \quad \mathbf {x} (0) = \left[ \begin{array}{c} 1 \\ . 5 \end{array} \right]

y (t) = -. 5 e ^ {- t} - e ^ {- 2 t} \quad \text { if } \quad \mathbf {x} (0) = \left[ \begin{array}{c} - 1 \\ 1 \end{array} \right].
$$

Using linearity properties, calculate $y(t)$ if $\mathbf{x}(0) = [ \begin{array}{c} 2 \\ .5 \end{array} ]$ .

3.2 The response of an LTI second-order system to a unit step is

$$
y (t) = . 5 -. 5 e ^ {- t} + e ^ {- 2 t} \quad \text { if } \quad \mathbf {x} (0) = \left[ \begin{array}{l} 1 \\ 1 \end{array} \right]
$$

and

$$
y (t) = . 5 - e ^ {- t} + 1. 5 e ^ {- 2 t} \quad \text { if } \quad \mathbf {x} (0) = \left[ \begin{array}{c} 2 \\ 2 \end{array} \right].
$$

Calculate the zero-state response to a unit step.

3.3 One algorithm for the computation of $e^A$ is the Padé formula, where $e^A$ is approximated by

$$\phi = \left(I - \frac {1}{2} A + \frac {1}{1 2} A ^ {2}\right) ^ {- 1} \left(I + \frac {1}{2} A + \frac {1}{1 2} A ^ {2}\right).$$

Assume a series expansion for $\phi$ , i.e.,

$$\phi = I + c _ {1} A + c _ {2} A ^ {2} + \dots$$

and calculate the coefficients of the series by matching coefficients on both sides of

$$\left(I - \frac {1}{2} A + \frac {1}{1 2} A ^ {2}\right) \phi = I + \frac {1}{2} A + \frac {1}{1 2} A ^ {2}.$$

For what power of $A$ does the series for $\phi$ begin to deviate from the exponential series?

3.4 Using Laplace transforms, compute $e^{At}$ for $A = \begin{bmatrix} 0 & 1 \\ -1 & -2 \end{bmatrix}$ .   
3.5 Repeat Problem 3.4 for $A = \begin{bmatrix} -1 & -2 \\ 2 & -1 \end{bmatrix}$ .

M 3.6 a. Compute $e^{At}$ for

$$
A = \left[ \begin{array}{c c c} - 1 & 1 & 0 \\ 0 & - 1 & - 1 \\ 0 & 1 & - 1 \end{array} \right]
$$

by Laplace transforms.

b. Evaluate the result of part (a) for $t = 1,2,4$ .   
c. Verify your answers to part (b) by numerical computation of $e^{A t}$ (MATLAB expm).   
d. Verify numerically that $e^{A2} = (e^A)^2$ and $e^{A.4} = (e^{A.2})^2$ .

M 3.7 For the system

$$
\dot {\mathbf {x}} = \left[ \begin{array}{c c} 0 & 1 \\ - 3 & - 4 \end{array} \right] \mathbf {x}
$$

a. Plot $x_{1}(t)$ and $x_{2}(t)$ vs. $t$ , if $\mathbf{x}(0) = [1]$ .   
b. Plot $x_{2}(t)$ vs. $x_{1}(t)$ for the same $\mathbf{x}(0)$ .   
c. Calculate the eigenvalues and eigenvectors of the matrix, and repeat parts (a) and (b) using each eigenvector as an initial state.

M 3.8 Repeat Problem 3.7 for the system
