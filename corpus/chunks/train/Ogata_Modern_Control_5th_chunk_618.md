Because the transfer function of the PD controller involves one zero, but no pole, it is not possible to electrically realize it by passive RLC elements only. Realization of the PD controller using op amps, resistors, and capacitors is possible, but because the PD controller is a high-pass filter, as mentioned earlier, the differentiation process involved may cause serious noise problems in some cases.There is, however, no problem if the PD controller is realized by use of the hydraulic or pneumatic elements.

The PD control, as in the case of the lead compensator, improves the transient-response characteristics, improves system stability, and increases the system bandwidth, which implies fast rise time.

The PID controller is a combination of the PI and PD controllers. It is a lag–lead compensator. Note that the PI control action and PD control action occur in different frequency regions. The PI control action occurs at the low-frequency region and PD control action occurs at the highfrequency region. The PID control may be used when the system requires improvements in both transient and steady-state performances.

A–8–2. Show that the transfer function $U ( s ) / E ( s )$ of the PID controller shown in Figure 8–44 is

$$\frac {U (s)}{E (s)} = K _ {0} \frac {T _ {1} + T _ {2}}{T _ {1}} \left[ 1 + \frac {1}{(T _ {1} + T _ {2}) s} + \frac {T _ {1} T _ {2} s}{T _ {1} + T _ {2}} \right]$$

Assume that the gain K is very large compared with unity, or $K \geqslant 1$

![](image/2107817cd9202883cad1a3f851b7d484824d4b1fb655ec57907f2845e00970e1.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    E["s"] --> |+| Sum
    Sum --> K
    K --> U["s"]
    U["s"] --> |1/K₀| Sum
    U["s"] --> |1/(1 + T₁s)| Sum
    Sum --> |−| Sum
    Sum --> |1/(1 + T₂s)| Sum
```
</details>

Figure 8–44 PID controller.

Solution

$$
\begin{array}{l} \frac {U (s)}{E (s)} = \frac {K}{1 + K \left(\frac {1}{K _ {0}} \frac {T _ {1} s}{1 + T _ {1} s} \frac {1}{1 + T _ {2} s}\right)} \\ \div \frac {K}{K \left(\frac {1}{K _ {0}} \frac {T _ {1} s}{1 + T _ {1} s} \frac {1}{1 + T _ {2} s}\right)} \\ = \frac {K _ {0} (1 + T _ {1} s) (1 + T _ {2} s)}{T _ {1} s} \\ = K _ {0} \left(1 + \frac {1}{T _ {1} s}\right) \left(1 + T _ {2} s\right) \\ = K _ {0} \left(1 + \frac {1}{T _ {1} s} + T _ {2} s + \frac {T _ {2}}{T _ {1}}\right) \\ = K _ {0} \frac {T _ {1} + T _ {2}}{T _ {1}} \left[ 1 + \frac {1}{\left(T _ {1} + T _ {2}\right) s} + \frac {T _ {1} T _ {2} s}{T _ {1} + T _ {2}} \right] \\ \end{array}
$$
