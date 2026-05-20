# EXAMPLE PROBLEMS AND SOLUTIONS

A–6–1. Sketch the root loci for the system shown in Figure 6–64(a). (The gain K is assumed to be positive.) Observe that for small or large values of K the system is overdamped and for medium values of K it is underdamped.

Solution. The procedure for plotting the root loci is as follows:

1. Locate the open-loop poles and zeros on the complex plane. Root loci exist on the negative real axis between 0 and –1 and between –2 and –3.   
2. The number of open-loop poles and that of finite zeros are the same. This means that there are no asymptotes in the complex region of the s plane.   
3. Determine the breakaway and break-in points. The characteristic equation for the system is

$$1 + \frac {K (s + 2) (s + 3)}{s (s + 1)} = 0$$

or

$$K = - \frac {s (s + 1)}{(s + 2) (s + 3)}$$

![](image/3c430605355ea0ad234a6e6a5eda94297fa5145d4269e672af7c129d30893563.jpg)  
Figure 6–64   
(a) Control system; (b) root-locus plot.

The breakaway and break-in points are determined from

$$
\begin{array}{l} \frac {d K}{d s} = - \frac {(2 s + 1) (s + 2) (s + 3) - s (s + 1) (2 s + 5)}{\left[ (s + 2) (s + 3) \right] ^ {2}} \\ = - \frac {4 (s + 0 . 6 3 4) (s + 2 . 3 6 6)}{\left[ (s + 2) (s + 3) \right] ^ {2}} \\ = 0 \\ \end{array}
$$

as follows:

$$s = - 0. 6 3 4, \quad s = - 2. 3 6 6$$

Notice that both points are on root loci. Therefore, they are actual breakaway or break-in points. At point $s = - 0 . 6 3 4$ , the value of K is

$$K = - \frac {(- 0 . 6 3 4) (0 . 3 6 6)}{(1 . 3 6 6) (2 . 3 6 6)} = 0. 0 7 1 8$$

Similarly, at s=–2.366,

$$K = - \frac {(- 2 . 3 6 6) (- 1 . 3 6 6)}{(- 0 . 3 6 6) (0 . 6 3 4)} = 1 4$$

(Because point s=–0.634 lies between two poles, it is a breakaway point, and because point $s = - 2 . 3 6 6$ lies between two zeros, it is a break-in point.)

4. Determine a sufficient number of points that satisfy the angle condition. (It can be found that the root loci involve a circle with center at –1.5 that passes through the breakaway and break-in points.) The root-locus plot for this system is shown in Figure 6–64(b).

Note that this system is stable for any positive value of K since all the root loci lie in the lefthalf s plane.

Small values of $\zeta \left( 0 < K < 0 . 0 7 1 8 \right)$ correspond to an overdamped system. Medium values of K $( 0 . 0 7 1 8 < K < 1 4 )$ correspond to an underdamped system. Finally, large values of $K \left( 1 4 < K \right)$ correspond to an overdamped system. With a large value of K, the steady state can be reached in much shorter time than with a small value of K.
