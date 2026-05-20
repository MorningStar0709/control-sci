A–8–9. The basic idea of the I-PD control is to avoid large control signals (which will cause a saturation phenomenon) within the system. By bringing the proportional and derivative control actions to the feedback path, it is possible to choose larger values for $K _ { p }$ and $T _ { d }$ than those possible by the PID control scheme.

Compare, qualitatively, the responses of the PID-controlled system and I-PD-controlled system to the disturbance input and to the reference input.

Solution. Consider first the response of the I-PD-controlled system to the disturbance input. Since, in the I-PD control of a plant, it is possible to select larger values for $K _ { p }$ and $T _ { d }$ than those of the PID-controlled case, the I-PD-controlled system will attenuate the effect of disturbance faster than the PID-controlled case.

Next, consider the response of the I-PD-controlled system to a reference input. Since the I-PD-controlled system is equivalent to the PID-controlled system with input filter (refer to Problem A–8–8), the PID-controlled system will have faster responses than the corresponding I-PD-controlled system, provided a saturation phenomenon does not occur in the PID-controlled system.

A–8–10. In some cases it is desirable to provide an input filter as shown in Figure 8–61(a). Notice that the input filter $G _ { f } ( s )$ is outside the loop. Therefore, it does not affect the stability of the closedloop portion of the system.An advantage of having the input filter is that the zeros of the closed-loop transfer function can be modified (canceled or replaced by other zeros) so that the closedloop response is acceptable.

Show that the configuration in Figure 8–61(a) can be modified to that shown in Figure 8–61(b), where $G _ { d } ( s ) = \bigl [ G _ { f } ( s ) \ : \bar { - } \ : 1 \bigr ] G _ { c } ( s )$ The compensation structure shown in Figure 8–61(b) is some-. times called command compensation.

Solution. For the system of Figure 8–61(a), we have

$$\frac {C (s)}{R (s)} = G _ {f} (s) \frac {G _ {c} (s) G _ {p} (s)}{1 + G _ {c} (s) G _ {p} (s)} \tag {8-15}$$

For the system of Figure 8–61(b), we have

$$U (s) = G _ {d} (s) R (s) + G _ {c} (s) E (s)E (s) = R (s) - C (s)C (s) = G _ {p} (s) U (s)$$

Thus

$$C (s) = G _ {p} (s) \left\{G _ {d} (s) R (s) + G _ {c} (s) [ R (s) - C (s) ] \right\}$$

or

$$\frac {C (s)}{R (s)} = \frac {\left[ G _ {d} (s) + G _ {c} (s) \right] G _ {p} (s)}{1 + G _ {c} (s) G _ {p} (s)} \tag {8-16}$$
