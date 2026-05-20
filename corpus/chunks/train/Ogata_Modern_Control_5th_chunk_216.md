![](image/2714822cd9459978d11dcae8015973c354cdfd00bfdae4b588aec67494dd1043.jpg)

<details>
<summary>line</summary>

| Time (sec) | Y1 | Y2 |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 1 | 0.3 | 1.5 |
| 2 | -0.1 | 0.7 |
| 3 | 0.1 | 1.2 |
| 4 | -0.05 | 0.9 |
| 5 | 0.0 | 1.0 |
| 6 | 0.0 | 1.0 |
| 7 | 0.0 | 1.0 |
| 8 | 0.0 | 1.0 |
| 9 | 0.0 | 1.0 |
| 10 | 0.0 | 1.0 |
</details>

Writing Text on the Graphics Screen. To write text on the graphics screen, enter, for example, the following statements:

$$\mathrm {text(3.4, - 0.06 , ^ {\prime} Y1 ^ {\prime})}$$

and

$$\text { text } (3. 4, 1. 4, ^ {\prime} \mathrm{Y2} ^ {\prime})$$

The first statement tells the computer to write ‘Y1’ beginning at the coordinates $x = 3 . 4$ , $y = - 0 . 0 6$ . Similarly, the second statement tells the computer to write $^ { 6 } \mathbf { Y } 2 ^ { , }$ beginning at the coordinates $x = 3 . 4 , y = 1 . 4 .$ . [See MATLAB Program 5–2 and Figure 5–19(a).]

Another way to write a text or texts in the plot is to use the gtext command. The syntax is

$$\mathrm {gtext (^ {\prime} text ^ {\prime})}$$

When gtext is executed, the computer waits until the cursor is positioned (using a mouse) at the desired position in the screen. When the left mouse button is pressed, the text enclosed in simple quotes is written on the plot at the cursor’s position. Any number of gtext commands can be used in a plot. (See, for example, MATLAB Program 5–15.)

MATLAB Description of Standard Second-Order System. As noted earlier, the second-order system

$$G (s) = \frac {\omega_ {n} ^ {2}}{s ^ {2} + 2 \zeta \omega_ {n} s + \omega_ {n} ^ {2}} \tag {5-40}$$

is called the standard second-order system. Given $\omega _ { n }$ and $\zeta ,$ , the command

$$\text { printsys(num,den) } \quad \text { or } \quad \text { printsys(num,den,s) }$$

prints num/den as a ratio of polynomials in s.

Consider, for example, the case where $\omega _ { n } = 5$ radsec and z=0.4. MATLAB Program $5 { - } 3$ generates the standard second-order system, where $\omega _ { n } = 5$ radsec and $\zeta = 0 . 4$ . Note that in MATLAB Program 5–3,“num $0 ^ { \circ }$ is 1.
