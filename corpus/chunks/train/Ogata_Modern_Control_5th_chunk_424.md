Figure 7–12 Pole–zero configurations of a minimum-phase system $G _ { 1 } ( s )$ and nonminimum-phase system $G _ { 2 } ( s )$ .   
![](image/0438c04d1efa7eefbdcc25a5612b58a335c2f08900b418e992e9714a813b7236.jpg)

<details>
<summary>text_image</summary>

jω
-1/T -1/T₁ 0 σ
</details>

$$G _ {1} (s) = \frac {1 + T s}{1 + T _ {1} s}$$

![](image/3dd254f892b080bda8e7e005f31e4c4ebcd60f5c7bae0d7e2b132d9ef98b39d9.jpg)

<details>
<summary>text_image</summary>

jω
-1/T₁ 0 1/T σ
</details>

$$G _ {2} (s) = \frac {1 - T s}{1 + T _ {1} s}$$

The pole–zero configurations of these systems are shown in Figure 7–12. The two sinusoidal transfer functions have the same magnitude characteristics, but they have different phase-angle characteristics, as shown in Figure 7–13. These two systems differ from each other by the factor

$$G (j \omega) = \frac {1 - j \omega T}{1 + j \omega T}$$

The magnitude of the factor $( 1 - j \omega T ) / ( 1 + j \omega T )$ is always unity. But the phase angle equals $- 2 \tan ^ { - 1 } \omega T$ and varies from $0 ^ { \circ } \mathrm { t o } - 1 8 0 ^ { \circ }$ as v is increased from zero to infinity.

As stated earlier, for a minimum-phase system, the magnitude and phase-angle characteristics are uniquely related. This means that if the magnitude curve of a system is specified over the entire frequency range from zero to infinity, then the phase-angle curve is uniquely determined, and vice versa. This, however, does not hold for a nonminimum-phase system.

Nonminimum-phase situations may arise in two different ways. One is simply when a system includes a nonminimum-phase element or elements. The other situation may arise in the case where a minor loop is unstable.
