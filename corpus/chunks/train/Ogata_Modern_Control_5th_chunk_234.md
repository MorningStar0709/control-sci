# MATLAB Program 5–17

$$
\begin{array}{l} t = 0: 0. 0 5: 1 0; \\ A = [ 0 1 0; 0 0 1; - 1 0 - 1 7 - 8 ]; \\ \mathrm{B} = [ 0; 0; 0 ]; \\ C = [ 1 \quad 0 \quad 0 ]; \\ D = [ 0 ]; \\ y = \text { initial } (A, B, C, D, [ 2; 1; 0. 5 ], t); \\ \operatorname{plot} (t, y) \\ \mathrm{grid} \\ \text { title } (^ {\prime} \text { Response   to   Initial   Condition } ^ {\prime}) \\ \text { xlabel('t   (sec)') } \\ \text { ylabel } (^ {\prime} \text { Output   y } ^ {\prime}) \\ \end{array}
$$

Figure 5–34 Response y(t) to initial condition.   
![](image/43a9b89a09d8f03aa42b5c445f80c2adeee92c887340361f850724344d644733.jpg)

<details>
<summary>line</summary>

| t (sec) | Output y |
| --- | --- |
| 0 | 2.0 |
| 1 | 2.2 |
| 2 | 1.0 |
| 3 | 0.4 |
| 4 | 0.1 |
| 5 | 0.05 |
| 6 | 0.02 |
| 7 | 0.01 |
| 8 | 0.005 |
| 9 | 0.002 |
| 10 | 0.001 |
</details>

The most important problem in linear control systems concerns stability. That is, under what conditions will a system become unstable? If it is unstable, how should we stabilize the system? In Section 5–4 it was stated that a control system is stable if and only if all closed-loop poles lie in the left-half s plane. Most linear closed-loop systems have closed-loop transfer functions of the form

$$\frac {C (s)}{R (s)} = \frac {b _ {0} s ^ {m} + b _ {1} s ^ {m - 1} + \cdots + b _ {m - 1} s + b _ {m}}{a _ {0} s ^ {n} + a _ {1} s ^ {n - 1} + \cdots + a _ {n - 1} s + a _ {n}} = \frac {B (s)}{A (s)}$$

where the $\boldsymbol { a } ^ { * } \boldsymbol { \mathrm { s } }$ and $b \mathbf { \bar { s } }$ are constants and $m \leq n .$ A simple criterion, known as Routh’s stability criterion, enables us to determine the number of closed-loop poles that lie in the right-half s plane without having to factor the denominator polynomial. (The polynomial may include parameters that MATLAB cannot handle.)

Routh’s Stability Criterion. Routh’s stability criterion tells us whether or not there are unstable roots in a polynomial equation without actually solving for them. This stability criterion applies to polynomials with only a finite number of terms. When the criterion is applied to a control system, information about absolute stability can be obtained directly from the coefficients of the characteristic equation.

The procedure in Routh’s stability criterion is as follows:

1. Write the polynomial in s in the following form:

$$a _ {0} s ^ {n} + a _ {1} s ^ {n - 1} + \dots + a _ {n - 1} s + a _ {n} = 0 \tag {5-61}$$

where the coefficients are real quantities. We assume that $a _ { n } \neq 0 ;$ that is, any zero root has been removed.
