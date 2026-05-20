Note also that if the command used does not include “t” explicitly, the time vector is automatically determined. If the command includes the user-supplied time vector “t”, as do the commands given by Equations (5–41) and (5–43)], this vector specifies the times at which the impulse response is to be computed.

If MATLAB is invoked with the left-hand argument [y,x,t], such as in the case of $[ \boldsymbol { \gamma } , \boldsymbol { \mu } , \boldsymbol { \mu } ] = \mathop { \mathrm { i m p u } } | \mathrm { s e } ( \mathsf { A } , \mathsf { B } , \mathsf { C } , \mathsf { D } )$ , the command returns the output and state responses of the system and the time vector t. No plot is drawn on the screen. The matrices y and x contain the output and state responses of the system evaluated at the time points t. (y has as many columns as outputs and one row for each element in t. x has as many columns as state variables and one row for each element in t.) To plot the response curve, we must include a plot command, such as plot(t,y).

EXAMPLE 5–5 Obtain the unit-impulse response of the following system:

$$\frac {C (s)}{R (s)} = G (s) = \frac {1}{s ^ {2} + 0 . 2 s + 1}$$

MATLAB Program 5–8 will produce the unit-impulse response. The resulting plot is shown in Figure 5–24.

<table><tr><td>MATLAB Program 5-8</td></tr><tr><td>num = [1];den = [1 0.2 1];impulse(num,den);gridtitle(&#x27;Unit-Impulse Response of G(s) = 1/(s^2 + 0.2s + 1)&#x27;)</td></tr></table>

![](image/dba93ba998f161cab681625d186f9842ea0fc436c0a43e3bc63ab77f21ceac18.jpg)

<details>
<summary>line</summary>

| Time (sec) | Amplitude |
| --- | --- |
| 0 | 0.0 |
| 5 | -0.6 |
| 10 | 0.4 |
| 15 | -0.3 |
| 20 | 0.2 |
| 25 | -0.1 |
| 30 | 0.05 |
| 35 | -0.05 |
| 40 | 0.02 |
| 45 | 0.01 |
| 50 | 0.0 |
</details>

Figure 5–24 Unit-impulseresponse curve.

Alternative Approach to Obtain Impulse Response. Note that when the initial conditions are zero, the unit-impulse response of $G ( s )$ is the same as the unit-step response of $s G ( s )$ .

Consider the unit-impulse response of the system considered in Example 5–5. Since $R ( s ) = 1$ for the unit-impulse input, we have

$$
\begin{array}{l} \frac {C (s)}{R (s)} = C (s) = G (s) = \frac {1}{s ^ {2} + 0 . 2 s + 1} \\ = \frac {s}{s ^ {2} + 0 . 2 s + 1} \frac {1}{s} \\ \end{array}
$$

We can thus convert the unit-impulse response of $G ( s )$ to the unit-step response of $s G ( s )$ .

If we enter the following num and den into MATLAB,
