Because of the cancellation of the $( s + 0 . 5 )$ terms, the compensated system is a third-order system. (Mathematically, this cancellation is exact, but practically such cancellation will not be exact because some approximations are usually involved in deriving the mathematical model of the system and, as a result, the time constants are not precise.) The root-locus plot of the compensated system is shown in Figure $6 { - } 5 6 ( \mathrm { a } )$ .An enlarged view of the root-locus plot near the origin is shown in Figure $6 { - } 5 6 ( \mathrm { b } )$ . Because the angle contribution of the phase lag portion of the lag–lead compensator is quite small, there is only a small change in the location of the dominant closedloop poles from the desired location, $s = - 2 . 5 \pm j 4 . 3 3$ The characteristic equation for the com-. pensated system is

$$s (s + 5. 0 2) (s + 0. 0 1 2 4 7) + 2 5. 0 4 (s + 0. 2) = 0$$

or

$$
\begin{array}{l} s ^ {3} + 5. 0 3 2 5 s ^ {2} + 2 5. 1 0 2 6 s + 5. 0 0 8 \\ = (s + 2. 4 1 2 3 + j 4. 2 7 5 6) (s + 2. 4 1 2 3 - j 4. 2 7 5 6) (s + 0. 2 0 7 8) = 0 \\ \end{array}
$$

Hence the new closed-loop poles are located at

$$s = - 2. 4 1 2 3 \pm j 4. 2 7 5 6$$

The new damping ratio is $\zeta = 0 . 4 9 1$ .Therefore the compensated system meets all the required performance specifications. The third closed-loop pole of the compensated system is located at $s = - 0 . 2 0 7 8$ Since this closed-loop pole is very close to the zero at. $s = - 0 . 2 ,$ the effect of this pole, on the response is small. (Note that, in general, if a pole and a zero lie close to each other on the negative real axis near the origin, then such a pole-zero combination will yield a long tail of small amplitude in the transient response.)

Root-Locus Plot of Compensated System   
![](image/00fbedbffb5bcb8f7a5a92c031be6175802fe3c936157c31fa9e4966ab46cc36.jpg)

<details>
<summary>scatter</summary>

| Real Axis | Imag Axis |
| --- | --- |
| -5 | 0 |
| 0 | 0 |
</details>

Root-Locus Plot of Compensated System near the Origin   
![](image/9b167ab8d5835d7c339b1046d367db6353f583871dec6f2d16d947b82929cb32.jpg)

<details>
<summary>scatter</summary>

| RealAxis | ImagAxis |
| --- | --- |
| -0.2 | 0.0 |
| 0.0 | 0.0 |
</details>

(b)   
Figure 6–56   
(a) Root-locus plot of the compensated system; (b) root-locus plot near the origin.

Unit-Step Responses of Compensated and Uncompensated Systems   
![](image/22ea2ddb4b1c754028b6559dee901c2233c6263ecf58b875760cd1bff9ff77aa.jpg)

<details>
<summary>line</summary>
