# Example 17.3 Let

$$g _ {1} = \frac {1 . 2 (s + 3)}{s - 5}, \quad g _ {2} = \frac {s - 1}{s - 2}, \quad g _ {3} = \frac {2 (s - 1) (s - 2)}{(s + 3) (s + 4)}, \quad g _ {4} = \frac {(s - 1) (s + 3)}{(s - 2) (s - 4)}.$$

Figure 17.2 shows the functions, $g _ { 1 } , g _ { 2 } , g _ { 3 }$ , and $g _ { 4 } .$ evaluated on the Nyquist contour Γ. Clearly, we have

$$\operatorname{wno} (g _ {1}) = - 1, \quad \operatorname{wno} (g _ {2}) = 0, \quad \operatorname{wno} (g _ {3}) = 2, \quad \operatorname{wno} (g _ {4}) = - 1$$

and they are consistent with the results computed from using Lemma 17.5.

The ν-gap metric introduced in Vinnicombe [1993a, 1993b] is defined as follows:

![](image/d1ab225fddfbb3ddd095199e98e94b42513f37ae0dc1fd4a28d930524fe9377a.jpg)

<details>
<summary>contour</summary>

| Group | Real Part | Imaginary Part |
| --- | --- | --- |
| g1 | -0.5 | 0.8 |
| g1 | 0.0 | 0.9 |
| g1 | 0.5 | 0.7 |
| g1 | 1.0 | 0.5 |
| g2 | -0.5 | 0.6 |
| g2 | 0.0 | 0.7 |
| g2 | 0.5 | 0.5 |
| g2 | 1.0 | 0.3 |
| g3 | -0.5 | 0.4 |
| g3 | 0.0 | 0.5 |
| g3 | 0.5 | 0.3 |
| g3 | 1.0 | 0.1 |
| g4 | -0.5 | 0.2 |
| g4 | 0.0 | 0.3 |
| g4 | 0.5 | 0.1 |
| g4 | 1.0 | -0.1 |
</details>

Figure 17.2: $g _ { 1 } , g _ { 2 } , g _ { 3 }$ , and $g _ { 4 }$ evaluated on Γ

Definition 17.2 The ν-gap metric is defined as

$$
\delta_ {\nu} (P _ {1}, P _ {2}) = \left\{ \begin{array}{l l} \| \Psi (P _ {1}, P _ {2}) \| _ {\infty}, & \text { if } \det \Theta (j \omega) \neq 0 \forall \omega \\ & \text { and   wno } \det \Theta (s) = 0, \\ 1, & \text { otherwise } \end{array} \right.
w h e r e \Theta (s) := N _ {2} ^ {\sim} N _ {1} + M _ {2} ^ {\sim} M _ {1} a n d \Psi (P _ {1}, P _ {2}) := - \tilde {N} _ {2} M _ {1} + \tilde {M} _ {2} N _ {1}.
$$

Note that it can be shown as in Vinnicombe [1993a] that

$$\delta_ {\nu} (P _ {1}, P _ {2}) = \delta_ {\nu} (P _ {2}, P _ {1}) = \delta_ {\nu} (P _ {1} ^ {T}, P _ {2} ^ {T})$$

and $\delta _ { \nu }$ is indeed a metric (a proof of this fact is quite complex).

Computing $\delta \nu ( P _ { 1 } , P _ { 2 } )$ : Let

$$
P _ {1} = \left[ \begin{array}{c c} A _ {1} & B _ {1} \\ \hline C _ {1} & D _ {1} \end{array} \right], \quad P _ {2} = \left[ \begin{array}{c c} A _ {2} & B _ {2} \\ \hline C _ {2} & D _ {2} \end{array} \right].
$$

1. Let $P _ { i } = N _ { i } M _ { i } ^ { - 1 } , i = 1 .$ , 2 be normalized right coprime factorizations. Then
