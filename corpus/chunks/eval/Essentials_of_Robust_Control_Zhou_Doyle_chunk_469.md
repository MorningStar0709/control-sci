$$\delta_ {\nu} (P _ {1}, P _ {2}) = \| \Psi (P _ {1}, P _ {2}) \| _ {\infty} = \sup _ {\omega} \frac {| P _ {1} - P _ {2} |}{\sqrt {1 + | P _ {1} | ^ {2}} \sqrt {1 + | P _ {2} | ^ {2}}} = \sup _ {\omega} \frac {| \omega |}{\sqrt {1 0 \omega^ {2} + 4}} = \frac {1}{\sqrt {1 0}}.$$

This implies that any controller K that stabilizes $P _ { 1 }$ and achieves only $b _ { P _ { 1 } , K } > 1 / \sqrt { 1 0 }$ will actually stabilize $P _ { 2 } .$ This result is clearly less conservative than that of using the gap metric. Furthermore, there exists a controller such that $b _ { P _ { 1 } , K } = 1 / \sqrt { 1 0 }$ that destabilizes $P _ { 2 }$ . Such a controller is $K = - 1 / 2$ , which results in a closed-loop system with $P _ { 2 }$ illposed.

Example 17.7 Consider the following example taken from Vinnicombe [1993b]:

$$P _ {1} = \frac {1 0 0}{2 s + 1}, \quad P _ {2} = \frac {1 0 0}{2 s - 1}, \quad P _ {3} = \frac {1 0 0}{(s + 1) ^ {2}}.$$

$P _ { 1 }$ and $P _ { 2 }$ have very different open-loop characteristics—one is stable, the other unstable. However, it is easy to show that

$$\delta_ {\nu} (P _ {1}, P _ {2}) = \delta_ {g} (P _ {1}, P _ {2}) = 0. 0 2, \quad \delta_ {\nu} (P _ {1}, P _ {3}) = \delta_ {g} (P _ {1}, P _ {3}) = 0. 8 9 8 8,\delta_ {\nu} (P _ {2}, P _ {3}) = \delta_ {g} (P _ {2}, P _ {3}) = 0. 8 9 4 1,$$

which show that $P _ { 1 }$ and $P _ { 2 }$ are very close while $P _ { 1 }$ and $P _ { 3 }$ (or $P _ { 2 }$ and $P _ { 3 } )$ are quite far away. It is not surprising that any reasonable controller for $P _ { 1 }$ will do well for $P _ { 2 }$ but not necessarily for $P _ { 3 }$ . The closed-loop step responses under unity feedback,

$$K _ {1} = 1,$$

are shown in Figure 17.5.

![](image/6453581404a208627e823f7d781238ea6d116685ae757df3a1c23f38c1519d36.jpg)

<details>
<summary>line</summary>

| x | P1 | P2 | P3 |
| --- | --- | --- | --- |
| 0.0 | 0.0 | 0.0 | 0.0 |
| 0.1 | 1.0 | 1.0 | 1.0 |
| 0.2 | 1.0 | 1.0 | 1.4 |
| 0.3 | 1.0 | 1.0 | 1.7 |
| 0.4 | 1.0 | 1.0 | 1.4 |
| 0.5 | 1.0 | 1.0 | 0.8 |
| 0.6 | 1.0 | 1.0 | 0.4 |
| 0.7 | 1.0 | 1.0 | 0.6 |
| 0.8 | 1.0 | 1.0 | 1.0 |
| 0.9 | 1.0 | 1.0 | 1.4 |
| 1.0 | 1.0 | 1.0 | 1.4 |
</details>

Figure 17.5: Closed-loop step responses with $K _ { 1 } = 1$

The corresponding stability margins for the closed-loop systems with $P _ { 1 }$ and $P _ { 2 }$ are

$$b _ {P _ {1}, K _ {1}} = 0. 7 0 7 1, \quad \text { and } \quad b _ {P _ {2}, K _ {1}} = 0. 7,$$

respectively, which are very close to their maximally possible margins,

$$b _ {\mathrm{obt}} (P _ {1}) = 0. 7 1 0 6, \quad \text { and } \quad b _ {\mathrm{obt}} (P _ {2}) = 0. 7 0 3 6$$
