# 2.7 The z-Transform

In the analysis of continuous-time systems the Laplace transform plays an important role. The transformation makes it possible to introduce the transfer function and the frequency interpretation of a system. The combination of time-domain and frequency-domain aspects gives an increasing understanding of systems. The discrete-time analogy of the Laplace transform is the z-transform—a convenient tool to study linear difference equations with or without initial conditions.

The z-transform maps a semi-infinite time sequence into a function of a complex variable. Notice the difference in range for the z-transform and the operator calculus. In the operator calculus we consider double-infinite time sequences. The main difference is because the z-transform also takes the initial values into consideration. The variable z is a complex variable and should be distinguished from the operator q.

Table 2.1 Zero-order hold sampling of a continuous-time system, $G(s)$ . The table gives the zero-order-hold equivalent of the continuous-time system, $G(s)$ , preceded by a zero-order hold. The sampled system is described by its pulse-transfer operator. The pulse-transfer operator is given in terms of the coefficients of

$$H (q) = \frac {b _ {1} q ^ {n - 1} + b _ {2} q ^ {n - 2} + \cdots + b _ {n}}{q ^ {n} + a _ {1} q ^ {n - 1} + \cdots + a _ {n}}$$
