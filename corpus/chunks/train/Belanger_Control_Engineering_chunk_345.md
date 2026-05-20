# Proportional-Integral-Derivative Compensation

The proportional-integral-derivative controller is the workhorse of the process industry, where it is often called a "three-term controller." If we cascade a PI controller with a PD controller, we obtain

$$
\begin{array}{l} G _ {c} (s) = k \left(\frac {1}{T _ {1} s} + 1\right) \left(T _ {2} s + 1\right) \\ = k \left(1 + \frac {T _ {2}}{T _ {1}}\right) + \frac {k}{T _ {1} s} + k T _ {2} s \\ = \kappa \left(1 + \frac {1}{T _ {I} s} + T _ {D} s\right) \tag {6.44} \\ \end{array}
$$

where

$$\kappa = k (1 + T _ {2} / T _ {1}) \text { is the proportional gain }T _ {I} = T _ {1} + T _ {2} \text { is the integral, or reset, time }T _ {D} = T _ {1} T _ {2} / (T _ {1} + T _ {2}) \text { is the derivative, or rate, time. }$$

In the form of Equation 6.44, the PID controller is seen to provide separate adjustments of low frequencies (through the integral term), midfrequencies (through the proportional term), and high frequencies (through the derivative term). This accounts for its great flexibility and for its widespread use in practice.
