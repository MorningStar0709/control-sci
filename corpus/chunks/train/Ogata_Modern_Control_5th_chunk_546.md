Locate on the polar locus frequency points where $\omega = \ 0 . 2 , 0 . 3 , 0 . 5 , 1 , 2 , 6 , 1 0 .$ , and 20 radsec. Also, find the magnitudes and phase angles of $G ( j \omega )$ at the specified frequency points.

Solution. In MATLAB Program 7–19 we used the frequency vector w, which consists of three frequency subvectors: w1, w2, and w3. Instead of such a w, we may simply use the frequency vector $\mathsf { w } = \mathsf { l o g s c a l e } ( \mathsf { d } _ { 1 } , \mathsf { d } _ { 2 } , \mathsf { n } )$ . MATLAB Program 7–19 uses the following frequency vector:

$$w = \text { logscale } (- 1, 2, 1 0 0)$$

This MATLAB program plots the polar locus and locates the specified frequency points on the polar locus, as shown in Figure 7–129.

```matlab
MATLAB Program 7-19
num = [20 20 10];
den = [1 11 10 0];
ww = logspace(-1,2,100);
nyquist(num,den,ww)
v = [-2 3 -5 0]; axis(v);
grid
hold
Current plot held
w = [0.2 0.3 0.5 1 2 6 10 20];
[re,im,w] = nyquist(num,den,w);
plot(re,im,'o')
text(1.1,-4.8,'w = 0.2')
text(1.1,-3.1,'0.3')
text(1.25,-1.7,'0.5')
text(1.37,-0.4,'1')
text(1.8,-0.3,'2')
text(1.4,-1.1,'6')
text(0.77,-0.8,'10')
text(0.037,-0.8,'20')
% ---- To get the values of magnitude and phase (in degrees) of G(jw)
% at the specified w values, enter the command [mag,phase,w]
% = bode(num,den,w) ----
[mag,phase,w] = bode(num,den,w);
% ---- The following table shows the specified frequency values w and
% the corresponding values of magnitude and phase (in degrees) ----
[w mag phase]
ans =
0.2000 4.9176 -78.9571
0.3000 3.2426 -72.2244
0.5000 1.9975 -55.9925
1.0000 1.5733 -24.1455
2.0000 1.7678 -14.4898
6.0000 1.6918 -31.0946
10.0000 1.4072 -45.0285
20.0000 0.8933 -63.4385 
```

Figure 7–129 Polar plot of G(jv) given in Problem A–7–13.   
![](image/6f5226d59aeb3d2d06658287a5f3de600c05192a2ab92fc5fe70f7d4efed0bb4.jpg)

<details>
<summary>other</summary>

Nyquist Diagram
| Point | Real Axis | Imaginary Axis |
| --- | --- | --- |
| 1 | 1.5 | -0.7 |
| 2 | 1.6 | -0.4 |
| 3 | 1.0 | -3.0 |
| 4 | 1.0 | -1.0 |
| 5 | 1.0 | -1.8 |
| 6 | 1.4 | -0.9 |
| 7 | 1.0 | -1.0 |
| 8 | 0.5 | -0.8 |
| 9 | 0.3 | -3.0 |
| 10 | 0.3 | -1.0 |
| 11 | 0.3 | -1.0 |
| 12 | 0.3 | -1.0 |
| 13 | 0.3 | -1.0 |
| 14 | 0.3 | -1.0 |
| 15 | 0.3 | -1.0 |
| 16 | 0.3 | -1.0 |
| 17 | 0.3 | -1.0 |
| 18 | 0.3 | -1.0 |
| 19 | 0.3 | -1.0 |
| 20 | 0.3 | -0.8 |
w = 0.2
</details>

A–7–14. Consider a unity-feedback, positive-feedback system with the following open-loop transfer function:

$$G (s) = \frac {s ^ {2} + 4 s + 6}{s ^ {2} + 5 s + 4}$$

Draw a Nyquist plot.
