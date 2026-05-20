Period of oscillation: Tperiod $T _ { \mathrm { p e r i o d } } = { \frac { 2 \pi } { \omega _ { n } { \sqrt { 1 - \zeta ^ { 2 } } } } } = 0 . 3 5 7 4 { \mathrm { s } }$

Number of cycles to steady state: $N _ { \mathrm { c y c l e s } } = { \frac { 2 { \sqrt { 1 - \zeta ^ { 2 } } } } { \pi \zeta } } = 2 . 8$ ???? cycles

The steady-state value is also needed for an accurate sketch of the step response. Using the modeling equation (7.81) with the steady-state condition $\ddot { \theta } = \dot { \theta } = 0 .$ , the steady-state angular displacement is $\dot { \theta _ { \mathrm { s s } } } = 2 . 5 \mathrm { N - m } / 6 5 \mathrm { N - m } / \mathrm { r a d } = 0 . 0 3 \dot { 8 } 5$ rad (or 2.20∘). The peak value of the transient response is

$$\theta_ {\max} = \theta_ {\mathrm{ss}} (1 + M _ {\mathrm{os}}) = 0. 0 5 7 3 \text { rad (or } 3. 2 8 ^ {\circ})$$

![](image/f607f62dfdb7ecfbb83d704560a77815d43ffbbaaedf7ab0a476f6a18557853a.jpg)

<details>
<summary>line</summary>

| Time, s | Angular displacement, θ(t), rad |
| --- | --- |
| 0.0 | 0.0 |
| 0.2 | 0.0573 |
| 0.4 | 0.03 |
| 0.6 | 0.043 |
| 0.8 | 0.037 |
| 1.0 | 0.039 |
| 1.2 | 0.0385 |
| 1.4 | 0.0385 |
| 1.6 | 0.0385 |
| 1.8 | 0.0385 |
| 2.0 | 0.0385 |
</details>

Figure 7.21 Step response of the underdamped, second-order mechanical system for Example 7.8.

Figure 7.21 shows the step response of the rotational mechanical system that can be obtained by using the following MATLAB commands:

>> sys = tf(1, [0.2 1.6 65]); % define LTI system, Eq. (7.81)
>> t = 0:0.001:2; % define time vector t
>> Tin = 2.5*ones(size(t)); % define input torque vector $T_{\mathrm{in}}(t)$ >> [theta,t] = lsim(sys,Tin,t); % obtain step response $\theta(t)$ using lsim

The important response characteristics are labeled on Fig. 7.21. The reader should be able to make an accurate sketch of the complete response from the performance criteria computed in this example.
