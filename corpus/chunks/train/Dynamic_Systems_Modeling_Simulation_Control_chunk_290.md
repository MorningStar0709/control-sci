Note that we can use the lsim command to obtain the unit-step response, as shown below:

>> t = 0:0.001:0.5; % define simulation time vector t
>> u = ones (size(t)); % define unit-step input vector u(t) = U(t)
>> [I, t] = lsim(sys, u, t); % obtain unit-step response for current I(t)

Here we must define the input u, which is a vector of unity values with the same dimension as simulation time vector t.

![](image/8cad16dcef5ea5a5772c43409b96782aa62bdb4b6530115d5de44323a16ceb8d.jpg)

<details>
<summary>line</summary>

| Time, s | Current, A |
| --- | --- |
| 0.0 | 0.0 |
| 0.1 | 0.5 |
| 0.2 | 0.6 |
| 0.3 | 0.62 |
| 0.4 | 0.63 |
| 0.5 | 0.63 |
</details>

(a)

![](image/f04b89fcf9909547d1c2dd2f8b6405a8fc8d6db3ec291091fc963e45ad52a25b.jpg)

<details>
<summary>line</summary>

| Time, s | Resistor voltage, V |
| --- | --- |
| 0.0 | 0.0 |
| 0.1 | 0.8 |
| 0.2 | 0.95 |
| 0.3 | 0.98 |
| 0.4 | 0.99 |
| 0.5 | 1.0 |
</details>

(b)   
Figure 6.2 RL circuit unit-step response for Example 6.1: (a) current vs. time and (b) resistor voltage $e _ { O }$ vs. time.
