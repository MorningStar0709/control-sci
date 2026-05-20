# Example 6.1

Figure 6.1 shows the simple series RL circuit from Example 5.16. Use MATLAB to determine the current I(t) and the resistor voltage $e _ { O } ( t )$ if the voltage input $e _ { \mathrm { i n } } ( t )$ is a 1-V step function applied at time t = 0. The current is initially zero, and $L = 0 . 1$ H and $R = 1 . 6 \Omega$ .

The mathematical model of the RL circuit is

$$L \dot {I} + R I = e _ {\text { in }} (t) \tag {6.5}$$

A transfer function is probably the easiest way to represent this simple first-order model. However, the reader should note that transfer functions assume zero initial conditions, which may not apply to all problems (fortunately, the initial current is zero in this case). Using the D operator to replace the derivative term, that is, ̇I = DI, Eq. (6.5) becomes

$$(L D + R) I = e _ {\text { in }} (t) \tag {6.6}$$

Next, form the ratio of current to input voltage, $I ( t ) / e _ { \mathrm { i n } } ( t )$ , replace D with the Laplace variable s, and substitute the numerical values for L and R to derive the transfer function

$$\frac {1}{0 . 1 s + 1 . 6} = \frac {I (s)}{E _ {\mathrm{in}} (s)} \tag {6.7}$$

![](image/16129b6c4829b3d1b777afa08d2d5ef24b52650b0cba4e58d22acc9ca5aabd1e.jpg)

<details>
<summary>text_image</summary>

L
+
e_in(t)
-
I
R
e_O
</details>

Figure 6.1 Series RL circuit for Example 6.1.

Because the voltage input $e _ { \mathrm { i n } } ( t )$ is a constant with unity magnitude, we can use the step command to obtain the unit-step response. The following MATLAB commands obtain the responses for current I(t) and resistor voltage $e _ { O } ( t ) = R I ( t )$

>> sys = tf(1, [0.1 1.6]); % create transfer function object sys
>> t = 0:0.001:0.5; % define simulation time vector t
>> [I,t] = step(sys,t); % obtain unit-step response for current I(t)
>> e_O = 1.6*I; % compute resistor voltage $e_{o}(t) = RI(t)$

Plots of the desired variables can be created using MATLAB’s plot command along with the desired plotting options; the commands for plotting current vs. time are

>> plot(t, I)    % plot current vs. time
>> grid    % add grid lines to plot
>> xlabel('Time, s')    % add x-axis label
>> ylabel('Current, A')    % add y-axis label

A similar set of commands plot resistor voltage $e _ { O } ( t )$ . Figure 6.2 presents plots of current I(t) and resistor voltage $e _ { O } ( t )$ vs. time. Note that both responses exhibit an exponential rise from a zero initial condition to a constant value, which is a characteristic of a first-order system response that we investigate in Chapter 7.
