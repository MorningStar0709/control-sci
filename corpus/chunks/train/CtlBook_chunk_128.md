# 5.3.1 Pole Location and Step Response

The location of poles in the complex plane determines the characteristics of the dynamic response to system inputs. One input which we care about a lot is the step function

$$
u (t) = \left\{ \begin{array}{l l} 0 & t <   0 \\ 1 & t > = 0 \end{array} \right.
$$

The Laplace transform of the step input is $\begin{array} { r } { U ( s ) = \frac { 1 } { s } } \end{array}$ .

The response to a step input determines what the system will do when we change our minds about what the output should be. For example, you walk into a room and turn the thermostat from $5 0 ^ { \circ }$ to $6 8 ^ { \circ }$ or you press Resume on your cruise control.

When we take a 2nd order transfer function of the form $\begin{array} { r } { G ( s ) = \frac { M } { ( s + a ) ( s + b ) } } \end{array}$ , and multiply it by the step input, we get the output

$$Y (s) = \frac {1}{s} \frac {M}{(s + a) (s + b)},$$

we can expand it using the partial fraction expansion (Section 1.4) into the form

$$Y (s) = \frac {A _ {0}}{s} + \frac {A _ {1}}{(s + a)} + \frac {A _ {2}}{(s + b)},$$

![](image/049a3ae113216fc20fc108e9d2cd055c80441e7c711ca291170fadd59332bd08.jpg)

<details>
<summary>line</summary>

| Step | Green Line | Blue Line | Red Line |
| --- | --- | --- | --- |
| 0 | 600 | 0 | 0 |
| 10 | 500 | 500 | 100 |
| 20 | 450 | 180 | 150 |
| 30 | 400 | 250 | 200 |
| 40 | 380 | 350 | 250 |
| 50 | 360 | 280 | 280 |
| 60 | 340 | 320 | 290 |
| 70 | 330 | 310 | 295 |
| 80 | 320 | 305 | 300 |
| 90 | 315 | 305 | 305 |
| 100 | 310 | 305 | 310 |
</details>

Figure 5.2: Step response of a typical system $\left( \omega _ { n } = 0 . 4 , \zeta = . 1 2 4 \right)$ with complex conjugate 2nd order poles. The envelopes (red and green) are also shown.

and further, the inverse transform of each term in the partial fraction expansion is

$$y (t) = A _ {0} + A _ {1} e ^ {a t} + A _ {2} e ^ {b t} \quad (t > = 0) \tag {5.1}$$

It can be shown (see Example 1.s5) that for a 2nd order system with a pair of complex conjugate poles, $\{ a , b \} , A _ { 1 } = A _ { 2 } ^ { * } , | A _ { 1 } | = | A _ { 2 } |$ , and that this solution takes the form

$$y (t) = A _ {0} - \left| A _ {1} \right| e ^ {- \zeta \omega_ {n} t} \left(2 \cos \left(\omega_ {d} t + \phi\right)\right) \tag {5.2}$$
