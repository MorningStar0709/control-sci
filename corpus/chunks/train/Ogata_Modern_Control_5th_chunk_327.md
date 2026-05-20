# 6–6 LEAD COMPENSATION

In Section 6–5 we presented an introduction to compensation of control systems and discussed preliminary materials for the root-locus approach to control-systems design and compensation. In this section we shall present control-systems design by use of the lead compensation technique. In carrying out a control-system design, we place a compensator in series with the unalterable transfer function G(s) to obtain desirable behavior. The main problem then involves the judicious choice of the pole(s) and zero(s) of the compensator $G _ { c } ( s )$ to have the dominant closed-loop poles at the desired location in the s plane so that the performance specifications will be met.

Lead Compensators and Lag Compensators. There are many ways to realize lead compensators and lag compensators, such as electronic networks using operational amplifiers, electrical RC networks, and mechanical spring-dashpot systems.

Figure 6–36 shows an electronic circuit using operational amplifiers. The transfer function for this circuit was obtained in Chapter 3 as follows [see Equation (3–36)]:

$$
\begin{array}{l} \frac {E _ {o} (s)}{E _ {i} (s)} = \frac {R _ {2} R _ {4}}{R _ {1} R _ {3}} \frac {R _ {1} C _ {1} s + 1}{R _ {2} C _ {2} s + 1} = \frac {R _ {4} C _ {1}}{R _ {3} C _ {2}} \frac {s + \frac {1}{R _ {1} C _ {1}}}{s + \frac {1}{R _ {2} C _ {2}}} \\ = K _ {c} \alpha \frac {T s + 1}{\alpha T s + 1} = K _ {c} \frac {s + \frac {1}{T}}{s + \frac {1}{\alpha T}} \tag {6-18} \\ \end{array}
$$

where

$$T = R _ {1} C _ {1}, \quad \alpha T = R _ {2} C _ {2}, \quad K _ {c} = \frac {R _ {4} C _ {1}}{R _ {3} C _ {2}}$$

Figure 6–36 Electronic circuit that is a lead network if $R _ { 1 } C _ { 1 } > R _ { 2 } C _ { 2 }$ and a lag network if $R _ { 1 } C _ { 1 } < R _ { 2 } C _ { 2 } ~$ .   
![](image/1fda00e63d401c83287693daf9672a6ae2007e55ba57187e52746568d8606f89.jpg)

<details>
<summary>text_image</summary>

C1
R1
Ei(s)
C2
R2
+
-
E(s)
R3
R4
+
-
Eo(s)
</details>

Figure 6–37

Pole-zero configurations: (a) lead network; (b) lag network.

![](image/9f801f14cc148f2ba82e90d73fb6240bebece10c98263b25526439244a7679ef.jpg)

<details>
<summary>text_image</summary>

jω
-1/R₂C₂ -1/R₁C₁ 0 σ
</details>

(a)

![](image/270620aaab56f9b37c288aa6d129b95b4ca8cafb97419c6d72c93a2f9397cfff.jpg)

<details>
<summary>text_image</summary>

jω
-1/R₁C₁ -1/R₂C₂ 0 σ
</details>

(b)

Notice that
