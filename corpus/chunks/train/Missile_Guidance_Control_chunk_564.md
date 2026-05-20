Cross-Range Errors: Assume that the thrust cut-off point is displaced by an amount δχ perpendicular to the intended (or nominal) plane of the trajectory. From Figure 6.14, we can determine by spherical trigonometry the cross-range error δC at the impact point or target as follows [2]:

$$\cos \delta C = \sin^ {2} \psi + \cos^ {2} \psi \cos \delta \chi , \tag {6.116a}$$

where ψ is the free-flight range angle. For small angles (i.e., δχ and δC),

$$\delta C \approx \delta \chi \cos \psi . \tag {6.116b}$$

From Figure 6.14 one can see that the cross-range error is zero when the free-flight range approaches 90◦.

The propagation of navigation errors (e.g., initial alignment, initial position, and initial velocity) has a considerable effect on cross-range and down-range errors. These effects are illustrated in Figure 6.15.

Figure 6.16 illustrates the effect of initial velocity error on the cross-range and down-range errors, while Figure 6.17 illustrates the effects of position errors.

In Figure 6.17 we note that because the North Pole is not, in general, normal to the launch position, longitude must be propagated in two ways. During free-fall, the sensitivity matrices are analytic functions of the cut-off and impact conditions. Thus, the down-range and cross-range errors, in terms of the sensitivity matrices, are as follows:

![](image/afccb0e8a66c8827a4db5c03fb28dffc300b9eb03ae1cf21ce47a91bcc283a80.jpg)

<details>
<summary>text_image</summary>

Nominal
δC
A
B
90° - ψ
ψ
δχ
Actual
O
</details>

Fig. 6.14. Lateral displacement of burnout point.

![](image/7668699d1ab1cf6a8111e24f601d4748acdc65ec48824e2445ac771ab7471fc1.jpg)

<details>
<summary>text_image</summary>

Nominal
Actual
CR
δB
Re
φ
0
δCR = δB · Re sin φ
</details>

(a) Initial alignment

![](image/9e283a827e1308decad63dacdb60ef8c942546798c761f5823ce9cbfd32624f5.jpg)

<details>
<summary>text_image</summary>

Nominal
Actual
δCR
δR
δCR = δR
0
</details>

Cross range

![](image/f543eb3406b1290164ac14d71cbd294b90c611441584eacbef72dcf799250854.jpg)

<details>
<summary>text_image</summary>

δR
Nominal
Actual
δCR
0
δDR = δR
</details>

Down range   
(b) Initial position   
Fig. 6.15. Effect of initial alignment and position on cross-range and down-range errors.
