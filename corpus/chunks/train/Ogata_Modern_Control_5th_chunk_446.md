# EXAMPLE 7–12 Consider the system defined by

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ - 2 5 & - 4 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c} 0 \\ 2 5 \end{array} \right] u

y = \left[ \begin{array}{l l} 1 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + [ 0 ] u
$$

Draw a Nyquist plot.

This system has a single input u and a single output y. A Nyquist plot may be obtained by entering the command

$$\text { nyquist } (A, B, C, D)$$

or

$$\text { nyquist } (A, B, C, D, 1)$$

MATLAB Program 7–9 will provide the Nyquist plot. (Note that we obtain the identical result by using either of these two commands.) Figure 7–41 shows the Nyquist plot produced by MATLAB Program 7–9.

<table><tr><td>MATLAB Program 7-9</td></tr><tr><td>A = [0 1;-25 -4];B = [0;25];C = [1 0];D = [0];nyquist(A,B,C,D)gridtitle(&#x27;Nyquist Plot&#x27;)</td></tr></table>

Figure 7–41 Nyquist plot of system considered in Example 7–12.   
![](image/e311e2e057c873f77fb78c9a2cd9566108a0e06e473b1e3da6b6de1b7c9d71dd.jpg)

<details>
<summary>other</summary>
