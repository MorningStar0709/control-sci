Observed data:Observed at top of the plot;
Observed data:Observed at bottom of the plot;
Observed data:Observed at top of the plot;
Observed Data for all points in the plot are not explicitly labeled in the code provided in the image.
</details>

EXAMPLE 7–13 Consider the system defined by

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} - 1 & - 1 \\ 6. 5 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c c} 1 & 1 \\ 1 & 0 \end{array} \right] \left[ \begin{array}{c} u _ {1} \\ u _ {2} \end{array} \right]

\left[ \begin{array}{c} y _ {1} \\ y _ {2} \end{array} \right] = \left[ \begin{array}{c c} 1 & 0 \\ 0 & 1 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c c} 0 & 0 \\ 0 & 0 \end{array} \right] \left[ \begin{array}{c} u _ {1} \\ u _ {2} \end{array} \right]
$$

This system involves two inputs and two outputs. There are four sinusoidal output–input relationships: $Y _ { 1 } ( j \omega ) / U _ { 1 } ( j \omega ) , \ \bar { Y } _ { 2 } ( j \omega ) / U _ { 1 } ( j \omega ) , \ \bar { Y _ { 1 } } ( j \omega ) / U _ { 2 } ( j \omega )$ and, $Y _ { 2 } ( j \omega ) / U _ { 2 } ( j \omega )$ Draw Nyquist. plots for the system. (When considering input $u _ { 1 }$ , we assume that input $u _ { 2 }$ is zero, and vice versa.)

The four individual Nyquist plots can be obtained by the use of the command

$$\text { nyquist } (A, B, C, D)$$

MATLAB Program 7–10 produces the four Nyquist plots. They are shown in Figure 7–42.

<table><tr><td>MATLAB Program 7-10</td></tr><tr><td>A = [-1 -1;6.5 0];B = [1 1;1 0];C = [1 0;0 1];D = [0 0;0 0];nyquist(A,B,C,D)</td></tr></table>

Figure 7–42 Nyquist plot of system considered in Example 7–13.   
![](image/4b826ad07a9b6084ed06cb2442e577a9b3a9c15d759fefb9fed755596278a233.jpg)
