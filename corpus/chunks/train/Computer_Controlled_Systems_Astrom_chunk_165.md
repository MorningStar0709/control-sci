# Stability Tests

It follows from Theorem 3.1 that a straightforward way to test the stability of a given system is to calculate the eigenvalues of the matrix $\Phi$ . There are good numerical algorithms for doing this. Well-established methods are available, for instance, in the package LAPACK, which is easily accessible in most computing centers. The routines are also included in packages like MATLAB®. The eigenvalues of a matrix then can be calculated with a single command.

![](image/63596498789b582c9098356e56fef9382a45b9ce45c7670bb15dfb80d452d8f1.jpg)

<details>
<summary>line</summary>

| Time | Input | Output |
| --- | --- | --- |
| 0 | 0.5 | 0.0 |
| 5 | -0.5 | -1.0 |
| 10 | 0.5 | 1.0 |
| 15 | -0.5 | -2.0 |
| 20 | 0.5 | 3.0 |
| 25 | -0.5 | -4.0 |
| 30 | 0.5 | 5.0 |
</details>

Figure 3.1 Input and output of the system in Example 3.1 when $\omega = 1$ , h = 0.5, and the initial state is zero.

It is, however, also important to have algebraic or graphical methods for investigating stability. These methods make it possible to understand how parameters in the system or the controller will influence the stability. The following are some of the ways of determining the stability of a discrete-time system:

- Direct numerical or algebraic computation of the eigenvalues of $\Phi$   
• Methods based on properties of characteristic polynomials   
• The root locus method   
• The Nyquist criterion   
- Lyapunov's method

Explicit calculation of the eigenvalues of a matrix cannot be done conveniently by hand for systems of order higher than 2. In some cases it is easy to calculate the characteristic equation

$$A (z) = a _ {0} z ^ {n} + a _ {1} z ^ {n - 1} + \dots + a _ {n} = 0 \tag {3.4}$$

and investigate its roots. Recall from Sec. 2.6 that the characteristic polynomial is the denominator polynomial of the pulse-transfer function. Stability tests can be obtained by investigating conditions for the zeros of a polynomial to be inside the unit disc.
