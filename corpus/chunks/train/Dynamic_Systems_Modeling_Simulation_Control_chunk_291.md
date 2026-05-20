# Example 6.2

Figure 6.3 shows a three-way spool valve used to meter flow in a hydraulic system, and Eq. (6.8) is the mathematical model of the valve. Use MATLAB to obtain the response of the system if the applied force f (t) is a pulse function that steps up from zero to 12 N at time $t = 0 . 0 2$ s and steps down to zero at $t = 0 . 0 6 \mathrm { s }$ . The spool valve is initially at rest.

$$0. 0 4 \ddot {y} + 1 6 \dot {y} + 7 0 0 0 y = f (t) \tag {6.8}$$

Equation (6.8) is the governing mathematical model of the spool valve, which consists of a single mass $( m = 0 . 0 4 \mathrm { k g } )$ , a linear friction force (viscous friction coefficient $b = 1 6 \mathrm { N - s / m } )$ , and a linear spring force (spring constant $k = 7 0 0 0 \mathrm { N } / \mathrm { m } )$ . Variable y(t) is the displacement of the spool valve (in m), and f (t) is the force from an electromagnetic actuator that can push on the valve. We assume that there is no hydraulic fluid pressure imbalance on the valve, and that flow forces are neglected; hence, the actuator force f (t) is the sole applied force acting on the valve mass. The system is initially at rest $( \dot { y } _ { 0 } = y _ { 0 } = 0 )$ at time t = 0, and the force steps from zero to 12 N at time $t = 0 . 0 2 { \mathrm { s } }$ .

We derive the system transfer function from the I/O equation (6.8) by using the D operator to replace the derivative terms, that is, $\ddot { y } = D ^ { 2 } y$ and $\dot { y } = D y$ , which yields

$$(0. 0 4 D ^ {2} + 1 6 D + 7 0 0 0) y = f (t) \tag {6.9}$$

Next, form the ratio of output to input, $y ( t ) / f ( t )$ , and replace D with the Laplace variable s to derive the transfer function

$$\frac {1}{0 . 0 4 s ^ {2} + 1 6 s + 7 0 0 0} = \frac {Y (s)}{F (s)} \tag {6.10}$$

Equation (6.10) is the transfer function that represents the spool-valve system. Because we have an arbitrary input (a pulse), we must use the lsim command. The following MATLAB commands will produce the pulse response:

>> sys = tf(1, [0.04 16 7000]); % create transfer function object sys
>> t = 0:0.0001:0.1; % define simulation time vector $0 \leq t \leq 0.1$ s
>> f(1:200) = 0; % define zero input for $0 \leq t < 0.02$ s
>> f(201:601) = 12; % define 12-N input force for $0.02 \leq t \leq 0.06$ s
>> f(602:1001) = 0; % define zero input for t > 0.06 s
>> [y,t] = lsim(sys,f,t); % obtain pulse response for valve position y(t)

![](image/ca79e98be3edbc9878ea484e8e2b9f4fa8ca1535e1c39e4512f41499423a4fc0.jpg)

<details>
<summary>text_image</summary>
