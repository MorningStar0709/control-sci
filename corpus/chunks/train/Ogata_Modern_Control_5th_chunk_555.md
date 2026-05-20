MATLAB Program 7–23 produces the Nyquist plot of G(jv), where v is between 0.5 and 1.15 radsec.The resulting plot is shown in Figure 7–140. Notice that point G(j1.15) lies on the unit circle, and the phase angle of this point is $- 1 2 0 ^ { \circ }$ . Hence, the phase margin is $6 0 ^ { \circ }$ . The fact that point $G ( j 1 . 1 5 )$ is on the unit circle verifies that at $\omega = 1 . 1 5$ radsec the magnitude is equal to 1 or 0 dB. (Thus, $\omega = 1 . 1 5$ is the gain crossover frequency.) Thus, $K = 0 . 1 8 8$ gives the desired phase margin of $6 0 ^ { \circ }$ .

MATLAB Program 7–23   
```matlab
%*****Nyquist plot in rectangular coordinates*****
num = [1.88 0.188];
den = [1 1.5 0.5 0];
w = 0.5:0.01:1.15;
[re,im,w] = nyquist(num,den,w);
%*****Convert rectangular coordinates into polar coordinates
% by defining z, r, theta as follows*****
z = re + i*im;
r = abs(z);
theta = angle(z);
%*****To draw polar plot, enter command 'polar(theta,r)'*****
polar(theta,r)
text(-1,3,'Check of Phase Margin')
text(0.3,-1.7,'Nyquist plot')
text(-2.2,-0.75,'Phase margin')
text(-2.2,-1.1,'is 60 degrees')
text(1.45,-0.7,'Unit circle') 
```

![](image/8e3e813062cbab12d4d835a2e443b174c1913f145267bbefb709a0d27ba9a514.jpg)

<details>
<summary>radar</summary>

Check of Phase Margin
| Angle (degrees) | Value |
| --- | --- |
| 0 | 0.5 |
| 30 | 1.0 |
| 60 | 1.5 |
| 90 | 2.0 |
| 120 | 2.5 |
| 150 | 2.0 |
| 180 | 1.5 |
| 210 | 1.0 |
| 240 | 0.5 |
| 270 | 0.5 |
| 300 | 1.0 |
| 330 | 1.5 |
| Unit circle | 2.0 |
| Nyquist plot | 2.5 |
</details>

Figure 7–140   
Nyquist plot of G(jv) showing that the phase margin is 60°.

Note that in writing ‘text’ in the polar diagram we enter the text command as follows:

$$\operatorname{text} (x, y, ^ {\prime \prime})$$

For example, to write ‘Nyquist plot’ starting at point (0.3, –1.7), enter the command

$$\text { text } (0. 3, - 1. 7, ^ {\prime} \text { Nyquist plot } ^ {\prime})$$

The text is written horizontally on the screen.

A–7–23. If the open-loop transfer function $G ( s )$ involves lightly damped complex-conjugant poles, then more than one M locus may be tangent to the $G ( j \omega )$ locus.

Consider the unity-feedback system whose open-loop transfer function is

$$G (s) = \frac {9}{s (s + 0 . 5) \left(s ^ {2} + 0 . 6 s + 1 0\right)} \tag {7-32}$$
