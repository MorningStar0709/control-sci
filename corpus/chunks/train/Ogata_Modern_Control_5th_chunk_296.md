Referring to Figure 6–9, if we choose a test point and move it in the very vicinity of the complex open-loop pole at $s = - p _ { 1 }$ , we find that the sum of the angular contributions from the pole at $s = p _ { 2 }$ and zero at $s = - z _ { 1 }$ to the test point can be considered remaining the same. If the test point is to be on the root locus, then the sum of $\phi _ { 1 } ^ { \prime } , - \theta _ { 1 }$ , and $- \theta _ { 2 } ^ { \prime }$ must be $\pm 1 8 0 ^ { \circ } ( 2 k + 1 )$ where), $k = 0 , 1 , 2 , \ldots$ . Thus, in the example,

$$\phi_ {1} ^ {\prime} - \left(\theta_ {1} + \theta_ {2} ^ {\prime}\right) = \pm 1 8 0 ^ {\circ} (2 k + 1)$$

or

$$\theta_ {1} = 1 8 0 ^ {\circ} - \theta_ {2} ^ {\prime} + \phi_ {1} ^ {\prime} = 1 8 0 ^ {\circ} - \theta_ {2} + \phi_ {1}$$

The angle of departure is then

$$\theta_ {1} = 1 8 0 ^ {\circ} - \theta_ {2} + \phi_ {1} = 1 8 0 ^ {\circ} - 9 0 ^ {\circ} + 5 5 ^ {\circ} = 1 4 5 ^ {\circ}$$

![](image/0a1db288f717e3ecb98746b75800ac1ef758f741b4c13b52479185b30b08e0c1.jpg)

<details>
<summary>text_image</summary>

jω
s
θ₁
-p₁
φ₁
-z₁
φ′₁
0
σ
θ₂
-ρ₂
θ′₂
</details>

Figure 6–9   
Determination of the angle of departure.

Since the root locus is symmetric about the real axis, the angle of departure from the pole at $s = - p _ { 2 } \mathrm { i s } - 1 4 5 ^ { \circ }$ .

3. Determine the break-in point. A break-in point exists where a pair of root-locus branches coalesces as K is increased. For this problem, the break-in point can be found as follows: Since

$$K = - \frac {s ^ {2} + 2 s + 3}{s + 2}$$

we have

$$\frac {d K}{d s} = - \frac {(2 s + 2) (s + 2) - (s ^ {2} + 2 s + 3)}{(s + 2) ^ {2}} = 0$$

which gives

$$s ^ {2} + 4 s + 1 = 0$$

or

$$s = - 3. 7 3 2 0 \quad \text { or } \quad s = - 0. 2 6 8 0$$

Notice that point s=–3.7320 is on the root locus. Hence this point is an actual break-in point. (Note that at point s=–3.7320 the corresponding gain value is $K = 5 . 4 6 4 1 . )$ ) Since point $s = - 0 . 2 6 8 0$ is not on the root locus, it cannot be a break-in point. (For point $s = - 0 . 2 6 8 0$ , the corresponding gain value is $K = - 1 . 4 6 4 1 . )$

4. Sketch a root-locus plot, based on the information obtained in the foregoing steps. To determine accurate root loci, several points must be found by trial and error between the breakin point and the complex open-loop poles. (To facilitate sketching the root-locus plot, we should find the direction in which the test point should be moved by mentally summing up the changes on the angles of the poles and zeros.) Figure 6–10 shows a complete root-locus plot for the system considered.
