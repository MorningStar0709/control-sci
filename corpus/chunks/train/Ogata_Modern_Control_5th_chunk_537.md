$$
\begin{array}{l} \mathbf {C} (s \mathbf {I} - \mathbf {A}) ^ {- 1} \mathbf {B} + \mathbf {D} = \left[ \begin{array}{c c} 1 & 0 \\ 0 & 1 \end{array} \right] \left[ \begin{array}{c c} s & - 1 \\ 2 5 & s + 4 \end{array} \right] ^ {- 1} \left[ \begin{array}{c c} 1 & 1 \\ 0 & 1 \end{array} \right] \\ = \frac {1}{s ^ {2} + 4 s + 2 5} \left[ \begin{array}{c c} s + 4 & 1 \\ - 2 5 & s \end{array} \right] \left[ \begin{array}{c c} 1 & 1 \\ 0 & 1 \end{array} \right] \\ = \left[ \begin{array}{c c} \frac {s + 4}{s ^ {2} + 4 s + 2 5} & \frac {s + 5}{s ^ {2} + 4 s + 2 5} \\ \frac {- 2 5}{s ^ {2} + 4 s + 2 5} & \frac {s - 2 5}{s ^ {2} + 4 s + 2 5} \end{array} \right] \\ \end{array}
$$

Hence

$$
\left[ \begin{array}{c} Y _ {1} (s) \\ Y _ {2} (s) \end{array} \right] = \left[ \begin{array}{c c} \frac {s + 4}{s ^ {2} + 4 s + 2 5} & \frac {s + 5}{s ^ {2} + 4 s + 2 5} \\ \frac {- 2 5}{s ^ {2} + 4 s + 2 5} & \frac {s - 2 5}{s ^ {2} + 4 s + 2 5} \end{array} \right] \left[ \begin{array}{c} U _ {1} (s) \\ U _ {2} (s) \end{array} \right]
$$

Assuming that $U _ { 2 } ( j \omega ) = 0 $ , we find $Y _ { 1 } ( j \omega ) / U _ { 1 } ( j \omega )$ and $Y _ { 2 } ( j \omega ) / U _ { 1 } ( j \omega )$ as follows:

$$\frac {Y _ {1} (j \omega)}{U _ {1} (j \omega)} = \frac {j \omega + 4}{(j \omega) ^ {2} + 4 j \omega + 2 5}\frac {Y _ {2} (j \omega)}{U _ {1} (j \omega)} = \frac {- 2 5}{(j \omega) ^ {2} + 4 j \omega + 2 5}$$

Similarly, assuming that $U _ { 1 } ( j \omega ) = 0$ , we find $Y _ { 1 } ( j \omega ) / U _ { 2 } ( j \omega )$ and $Y _ { 2 } ( j \omega ) / U _ { 2 } ( j \omega )$ as follows:

$$\frac {Y _ {1} (j \omega)}{U _ {2} (j \omega)} = \frac {j \omega + 5}{(j \omega) ^ {2} + 4 j \omega + 2 5}\frac {Y _ {2} (j \omega)}{U _ {2} (j \omega)} = \frac {j \omega - 2 5}{(j \omega) ^ {2} + 4 j \omega + 2 5}$$

Notice that $Y _ { 2 } ( j \omega ) / U _ { 2 } ( j \omega )$ is a nonminimum-phase transfer function.

A–7–3. Referring to Problem A–7–2, plot Bode diagrams for the system, using MATLAB.

Solution. MATLAB Program 7–15 produces Bode diagrams for the system. There are four sets of Bode diagrams: two for input 1 and two for input 2. These Bode diagrams are shown in Figure 7–119.

<table><tr><td>MATLAB Program 7-15</td></tr><tr><td>A = [0 1;-25 -4];B = [1 1;0 1];C = [1 0;0 1];D = [0 0;0 0];bode(A,B,C,D)</td></tr></table>

![](image/911e39b5b40045031ea235825856a6fce53a3b8fa362ae4c9d8c17561c3df447.jpg)  
Figure 7–119   
Bode diagrams.

Figure 7–120   
Closed-loop system.   
![](image/b7d2a3bdbd6646d949fd9e158faa5f36bd655dc1aee4d6e51fdcf78cbb31a657.jpg)

<details>
<summary>flowchart</summary>
