A–7–24. Consider the system shown in Figure 7–144(a). Design a compensator such that the closed-loop system will satisfy the requirements that the static velocity error constant $= 2 0 \sec ^ { - 1 }$ , phase margin $= 5 0 ^ { \circ }$ , and gain margin G 10 dB.

Solution. To satisfy the requirements, we shall try a lead compensator $G _ { c } ( s )$ of the form

$$G _ {c} (s) = K _ {c} \alpha \frac {T s + 1}{\alpha T s + 1}= K _ {c} \frac {s + \frac {1}{T}}{s + \frac {1}{\alpha T}}$$

(If the lead compensator does not work, then we need to employ a compensator of different form.) The compensated system is shown in Figure 7–144(b).

Define

$$G _ {1} (s) = K G (s) = \frac {1 0 K}{s (s + 1)}$$

where $K = K _ { c } \alpha$ . The first step in the design is to adjust the gain K to meet the steady-state performance specification or to provide the required static velocity error constant. Since the static velocity error constant $K _ { v }$ is given as $2 0 \mathrm { s e c } ^ { - 1 }$ , we have

$$
\begin{array}{l} K _ {v} = \lim _ {s \rightarrow 0} s G _ {c} (s) G (s) \\ = \lim _ {s \rightarrow 0} s \frac {T s + 1}{\alpha T s + 1} G _ {1} (s) \\ = \lim _ {s \rightarrow 0} \frac {s 1 0 K}{s (s + 1)} \\ = 1 0 K = 2 0 \\ \end{array}
$$

or

$$K = 2$$

With K=2, the compensated system will satisfy the steady-state requirement.

We shall next plot the Bode diagram of

$$G _ {1} (s) = \frac {2 0}{s (s + 1)}$$

Figure 7–144

(a) Control system; (b) compensated system.

![](image/00ebf94b32e9fadf5ebb48ccf0a0a7fb6e21bc9b50b9f04660b58d8447ff273f.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["+"] --> B["10/(s(s+1))"]
    B --> C["G(s)"]
    C --> D["Feedback"]
    D --> A
```
</details>

(a)

![](image/0cc46851b29e57d1d88d0cb31ac1c86f268e0b035155229db59a8e8168ba7ac1.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["+"] --> B["Gc(s)"]
    B --> C["10/(s(s+1))"]
    C --> D["G(s)"]
    D --> E["Feedback"]
    E --> A
```
</details>

(b)

MATLAB Program 7–24 produces the Bode diagram shown in Figure 7–145. From this plot, the phase margin is found to be 14°. The gain margin is ±q dB.
