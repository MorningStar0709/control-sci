$$
\begin{array}{l} \underline {{G (j \omega)}} = - \omega T \quad (\text { radians }) \\ = - 5 7. 3 \omega T \quad (\text { degrees }) \\ \end{array}
$$

The phase angle varies linearly with the frequency v.The phase-angle characteristic of transport lag is shown in Figure 7–14.

![](image/43bb50a5ca739cb603164602b73cb8df0bd0be945531d1deb2920490b64eb950.jpg)  
Figure 7–14 Phase-angle characteristic of transport lag.

$$G (j \omega) = \frac {e ^ {- j \omega L}}{1 + j \omega T}$$

The log magnitude is

$$
\begin{array}{l} 2 0 \log | G (j \omega) | = 2 0 \log | e ^ {- j \omega L} | + 2 0 \log \left| \frac {1}{1 + j \omega T} \right| \\ = 0 + 2 0 \log \left| \frac {1}{1 + j \omega T} \right| \\ \end{array}
$$

The phase angle of $G ( j \omega )$ is

$$
\begin{array}{l} \underline {{G (j \omega)}} = \underline {{e ^ {- j \omega L}}} + \underline {{\frac {1}{1 + j \omega T}}} \\ = - \omega L - \tan^ {- 1} \omega T \\ \end{array}
$$

The log-magnitude and phase-angle curves for this transfer function with L=0.5 and T=1 are shown in Figure 7–15.

![](image/a417e9369b33a12ea8f3b84ed3515a884476d1b3c12747e034cf367bc51c5158.jpg)  
Figure 7–15   
Bode diagram for the system $e ^ { - \bar { j } \omega L } / ( 1 + j \omega T )$ with L=0.5 and T=1.

Relationship between System Type and Log-Magnitude Curve. Consider the unity-feedback control system. The static position, velocity, and acceleration error constants describe the low-frequency behavior of type 0, type 1, and type 2 systems, respectively. For a given system, only one of the static error constants is finite and significant. (The larger the value of the finite static error constant, the higher the loop gain is as v approaches zero.)

The type of the system determines the slope of the log-magnitude curve at low frequencies. Thus, information concerning the existence and magnitude of the steadystate error of a control system to a given input can be determined from the observation of the low-frequency region of the log-magnitude curve.

Determination of Static Position Error Constants. Consider the unity-feedback control system shown in Figure 7–16. Assume that the open-loop transfer function is given by

$$G (s) = \frac {K \left(T _ {a} s + 1\right) \left(T _ {b} s + 1\right) \cdots \left(T _ {m} s + 1\right)}{s ^ {N} \left(T _ {1} s + 1\right) \left(T _ {2} s + 1\right) \cdots \left(T _ {p} s + 1\right)}$$

or
