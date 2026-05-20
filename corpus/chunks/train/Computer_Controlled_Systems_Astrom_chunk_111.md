# System with Internal Time Delay

In the previous derivation it is assumed that the time delay of the system is at the input (or the output) of the system. Many physical systems have the structure shown in Fig. 2.3, that is, the time delay is internal. Let the system be described by the equations

$$S _ {1}: \frac {d x _ {1} (t)}{d t} = A _ {1} x _ {1} (t) + B _ {1} u (t)y _ {1} (t) = C _ {1} x _ {1} (t) + D _ {1} u (t)S _ {2}: \frac {d x _ {2} (t)}{d t} = A _ {2} x _ {2} (t) + B _ {2} u _ {2} (t) \tag {2.13}u _ {2} (t) = y _ {1} (t - \tau)$$

It is assumed that $u(t)$ is piecewise constant over the sampling interval $h$ . We now want to find the recursive equations for $x_{1}(kh)$ and $x_{2}(kh)$ .

Sampling (2.13) when $\tau = 0$ using the sampling period $h$ gives the partitioned system

$$
\binom {x _ {1} (k h + h)} {x _ {2} (k h + h)} = \left( \begin{array}{c c} \Phi_ {1} (h) & 0 \\ \Phi_ {2 1} (h) & \Phi_ {2} (h) \end{array} \right) \binom {x _ {1} (k h)} {x _ {2} (k h)} + \binom {\Gamma_ {1} (h)} {\Gamma_ {2} (h)} u (k h)
$$

We have the following theorem.

![](image/68d6c8f1290093e9dca13c768aadccc36d7ed895688a9536c797a3e446e4b3e9.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    u --> S1
    S1 --> y1
    y1 --> e^(-sτ)
    e^(-sτ) --> u2
    u2 --> S2
    S2 --> y
```
</details>

Figure 2.3 System with inner time delay.

THEOREM 2.1 INNER TIME DELAY Periodic sampling of the system (2.13) with the sampling interval h and with $0 < \tau \leq h$ gives the sampled-data representation

$$x _ {1} (k h + h) = \Phi_ {1} (h) x _ {1} (k h) + \Gamma_ {1} (h) u (k h)x _ {2} (k h + h) = \Phi_ {2 1} ^ {-} x _ {1} (k h - h) + \Phi_ {2} (h) x _ {2} (k h) \tag {2.14}+ \Gamma_ {2} ^ {-} u (k h - h) + \Gamma_ {2} (h - \tau) u (k h)$$

where

$$\Phi_ {i} (t) = e ^ {A _ {i} t} \quad i = 1, 2\Phi_ {2 1} (t) = \int_ {0} ^ {t} e ^ {A _ {2} s} B _ {2} C _ {1} e ^ {A _ {1} (t - s)} d s\Gamma_ {1} (t) = \int_ {0} ^ {t} e ^ {A _ {1} s} B _ {1} d s \tag {2.15}\Gamma_ {2} (t) = \int_ {0} ^ {t} e ^ {A _ {2} s} B _ {2} C _ {1} \Gamma_ {1} (t - s) d s\Phi_ {2 1} ^ {-} = \Phi_ {2 1} (h) \Phi_ {1} (h - \tau)\Gamma_ {2} ^ {-} = \Phi_ {2 1} (h) \Gamma_ {1} (h - \tau) + \Phi_ {2 1} (h - \tau) \Gamma_ {1} (\tau) + \Phi_ {2} (h - \tau) \Gamma_ {2} (\tau)$$

Reference to proof of the theorem is given at the end of the chapter.

Remark. The sampled-data system (2.14) for the time delay $\tau$ is obtained by sampling (2.13) without any time delay for the sampling intervals h, $h - \tau$ , and $\tau$ . This gives $\Phi_{1}$ , $\Phi_{2}$ , $\Phi_{21}$ , $\Gamma_{1}$ , and $\Gamma_{2}$ for the needed sampling intervals. This implies that standard software for sampling systems can be used to obtain (2.14).
