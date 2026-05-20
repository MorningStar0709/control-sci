# Example 18.1 Let

$$G (s) = \frac {s ^ {2} + 2 s + 1}{s ^ {3} + s ^ {2} + 2 s + 1}.$$

![](image/04ddd6c06087c7d0944456369cabb9000fba75469d134204b4ae0fe2d520a810.jpg)

<details>
<summary>line</summary>

| x | Nyquist diagram 1/G | disk centered at (0,0) | disk centered at (0,-0.2j) | disk centered at (0,-j) |
| --- | --- | --- | --- | --- |
| -1.5 | 1.0 | - | - | - |
| -1.0 | 0.5 | - | - | - |
| -0.5 | 0.0 | 0.3 | - | - |
| 0.0 | -0.5 | 0.2 | - | - |
| 0.5 | -0.8 | 0.1 | - | - |
| 1.0 | -1.0 | - | - | - |
| 1.5 | -1.5 | - | - | - |
</details>

Figure 18.3: Computing the real stability margin by covering with disks

We are interested in finding the largest k such that $1 + \Delta G ( s )$ has no zero in the right-half plane for all $\Delta \in [ - k , k ]$ . Of course, the largest k can be found very easily by using well-known stability test, which gives

$$k _ {\max} = \left(\sup _ {\omega} \mu_ {\boldsymbol {\Delta}} (G (j \omega))\right) ^ {- 1} = \left(\sup _ {\omega} \max _ {\phi \in [ - 1, 1 ]} \rho_ {R} (\phi G (j \omega))\right) ^ {- 1}= \left(\sup _ {\omega} \left\{| G (j \omega) |: \Im G (j \omega) = 0 \right\}\right) ^ {- 1} = \inf _ {\omega} \left\{\frac {1}{| G (j \omega) |}: \Im G (j \omega) = 0 \right\} = 0. 5.$$

Now we use the complex covering idea to find the best possible k. Note that we only need to find the smallest $| \Delta |$ so that $1 + \Delta G ( j \omega _ { 0 } ) = 0$ for some ω0 or, equivalently, $\Delta + 1 / G ( j \omega _ { 0 } ) = 0$ . The frequency response of $1 / G$ and the disks covering an interval $[ - k , k ]$ are shown in Figure 18.3. It is clear that a centered disk would give $k =$ $1 / \left. G \right. _ { \infty } = 0 . 2 9 7 0$ and an off-axis disk centered at $( 0 , - 0 . 2 j )$ would give $k = 0 . 3 9 8 4$ while an off-axis disk centered at $( 0 , - j )$ would give the exactly value $k = 0 . 5$ .

The following alternative characterization of the upper bound is useful in the mixed µ synthesis.

Theorem 18.4 Given $\beta > 0$ , there exist $D \in \mathcal { D }$ and $G \in { \mathcal { G } }$ such that

$$M ^ {*} D M + j (G M - M ^ {*} G) - \beta^ {2} D \leq 0$$

if and only if there are $D _ { 1 } \in \mathcal { D }$ and $G _ { 1 } \in \mathcal G$ such that

$$\overline {{\sigma}} \left(\left(\frac {D _ {1} M D _ {1} ^ {- 1}}{\beta} - j G _ {1}\right) (I + G _ {1} ^ {2}) ^ {- \frac {1}{2}}\right) \leq 1.$$

Proof. Let $D = D _ { 1 } ^ { 2 }$ and $G = \beta D _ { 1 } G _ { 1 } D _ { 1 }$ . Then
