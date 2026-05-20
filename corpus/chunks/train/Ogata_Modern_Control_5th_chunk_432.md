# MATLAB Program 7–3

$$
\begin{array}{l} \text {num = [9 1.8 9];} \\ \text {den = [1 1.2 9 0];} \\ \text {w = logspace(-2,3,100);} \\ \text {bode(num,den,w)} \\ \text {title('Bode Diagram of G(s) = 9(s^2 + 0.2s + 1)/[s(s^2 + 1.2s + 9)]')} \end{array}
$$

Figure 7–23 Bode diagram of $G ( s ) = \frac { \bar { 9 ( } s ^ { 2 } + 0 . 2 s + 1 ) } { s { \left( s ^ { 2 } + 1 . 2 s + 9 \right) } } .$   
![](image/7324085ae2a0a631d1652fdaab2a31116e05391914b0b3c0a7284d162ed6b7df.jpg)

<details>
<summary>line</summary>

| Frequency (rad/sec) | Phase (deg) | Magnitude (dB) |
| --- | --- | --- |
| 0.01 | -100 | 40 |
| 0.1 | -100 | 20 |
| 1 | 60 | -20 |
| 10 | -80 | 0 |
| 100 | -100 | -20 |
| 1000 | -100 | -40 |
</details>

Obtaining Bode Diagrams of Systems Defined in State Space. Consider the system defined by

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} \mathbf {u}\mathbf {y} = \mathbf {C x} + \mathbf {D u}$$

where state vector (n-vector)x =

output vector (m-vector)y =

control vector (r-vector)u =

state matrix (n\*n matrix)A =

control matrix (n\*r matrix)B =

output matrix (m\*n matrix)C =

direct transmission matrix (m\*r matrix)D =

A Bode diagram for this system may be obtained by entering the command

$$\mathrm{bode} (\mathrm{A}, \mathrm{B}, \mathrm{C}, \mathrm{D})$$

or others listed earlier in this section.

The command bode(A,B,C,D) produces a series of Bode plots, one for each input of the system, with the frequency range automatically determined. (More points are used when the response is changing rapidly.)

The command bode(A,B,C,D,iu), where iu is the ith input of the system, produces the Bode diagrams from the input iu to all the outputs $\left( y _ { 1 } , y _ { 2 } , \ldots , y _ { m } \right)$ of the system, with a frequency range automatically determined. (The scalar iu is an index into the inputs of the system and specifies which input is to be used for plotting Bode diagrams). If the control vector u has three inputs such that

$$
\mathbf {u} = \left[ \begin{array}{c} u _ {1} \\ u _ {2} \\ u _ {3} \end{array} \right]
$$

then iu must be set to either 1, 2, or 3.

If the system has only one input u, then either of the following commands may be used:

$$\operatorname{bode} (A, B, C, D)$$

or

$$\operatorname{bode} (A, B, C, D, 1)$$

EXAMPLE 7–7 Consider the following system:
