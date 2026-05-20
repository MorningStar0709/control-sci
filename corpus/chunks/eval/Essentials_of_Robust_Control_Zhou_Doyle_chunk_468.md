| Frequency ω | b_P0,K(ω) | ψ(P0(jω),P1(jω)) |
| --- | --- | --- |
| Low | Low | Low |
| Peak | High | High |
| High | Medium | Low |
</details>

Figure 17.4: K stabilizes both $P _ { 0 }$ and $P _ { 1 }$ since $b _ { P _ { 0 } , K } ( \omega ) > \psi ( P _ { 0 } , P _ { 1 } )$ for all $\omega$

The following theorem is one of the main results on the ν-gap metric.

Theorem 17.9 Let $P _ { 0 }$ be a nominal plant and $\beta \leq \alpha < b _ { \mathrm { o b t } } ( P _ { 0 } )$ .

(i) For a given controller K,

$$\arcsin b _ {P, K} > \arcsin \alpha - \arcsin \beta$$

for all P satisfying $\delta _ { \nu } ( P _ { 0 } , P ) \le \beta$ if and only $i f b _ { P _ { 0 } , K } > \alpha$

(ii) For a given plant P ,

$$\arcsin b _ {P, K} > \arcsin \alpha - \arcsin \beta$$

for all K satisfying $b _ { P _ { 0 } , K } > \alpha$ if and only $i f \delta _ { \nu } ( P _ { 0 } , P ) \leq \beta$ .

Proof. The sufficiency follows essentially from Theorem 17.8. The necessity proof is harder, see Vinnicombe [1993a, 1993b] for details. ✷

The preceding theorem shows that any plant at a distance less than $\beta$ from the nominal will be stabilized by any controller stabilizing the nominal with a stability margin of $\beta .$ Furthermore, any plant at a distance greater than $\beta$ from the nominal will be destabilized by some controller that stabilizes the nominal with a stability margin of at least β.

Similarly, one can consider the system robust performance with simultaneous perturbations on the plant and controller.

Theorem 17.10 Suppose the feedback system with the pair $( P _ { 0 } , K _ { 0 } )$ is stable. Then

$$\arcsin b _ {P, K} \geq \arcsin b _ {P _ {0}, K _ {0}} - \arcsin \delta_ {\nu} (P _ {0}, P) - \arcsin \delta_ {\nu} (K _ {0}, K)$$

for any P and K.

Proof. Use the fact that $b _ { P , K } = b _ { K , P }$ and apply Theorem 17.8 to get

$$\arcsin b _ {P, K} \geq \arcsin b _ {P _ {0}, K} - \arcsin \delta_ {\nu} (P _ {0}, P).$$

Dually, we have

$$\arcsin b _ {P _ {0}, K} \geq \arcsin b _ {P _ {0}, K _ {0}} - \arcsin \delta_ {\nu} (K _ {0}, K).$$

Hence the result follows.

![](image/af154093dc7cd9a7d5a8a1d3e3d6564a53a1943267ba79a5e07a9725b1948ff4.jpg)

Example 17.6 Consider again the following example, studied in Vinnicombe [1993b], with

$$P _ {1} = \frac {s - 1}{s + 1}, \quad P _ {2} = \frac {2 s - 1}{s + 1}$$

and note that

$$1 + P _ {2} ^ {\sim} P _ {1} = 1 + \frac {- 2 s - 1}{- s + 1} \frac {s - 1}{s + 1} = \frac {3 s + 2}{s + 1}.$$

Then

$$1 + P _ {2} ^ {\sim} (j \omega) P _ {1} (j \omega) \neq 0, \quad \forall \omega , \quad \text { wno } \det (I + P _ {2} ^ {\sim} P _ {1}) + \eta (P _ {1}) - \eta (P _ {2}) = 0$$

and
