# Example 11.5

Convert the continuous time system G(s) to discrete time.

$$G (s) = \frac {2 0 (s + 1)}{(s + 0 . 0 1) (s + 0 . 2) (s + 1 0)}$$

We have very limited computing power available due to a low target for system cost. Compute two versions of a discrete time system, for two sample times:

$$T _ {1} = 2 \times \text { thehighestpoleorzero }.T _ {1} = 4 \times \text { thehighestpoleorzero }.$$

Code for this is given in Listing 11.1. Output is

ECE 447 Example: Conversion to Discrete Time:   
```txt
Continuous Time System: <TransferFunction>: sys[12]
Inputs (1): ['u[0]']
Outputs (1): ['y[0]']

20 s + 20
s^3 + 10.21 s^2 + 2.102 s + 0.02

Discrete Time System (20Hz): <TransferFunction>: sys[12]$sampled
Inputs (1): ['u[0]']
Outputs (1): ['y[0]']

0.0102 z^3 + 0.01069 z^2 - 0.009202 z - 0.009699
z^3 - 2.59 z^2 + 2.183 z - 0.5937
dt = 0.05

Discrete Time System (40Hz): <TransferFunction>: sys[12]$sampled
Inputs (1): ['u[0]']
Outputs (1): ['y[0]']

0.002805 z^3 + 0.002874 z^2 - 0.002667 z - 0.002736
z^3 - 2.773 z^2 + 2.546 z - 0.7737
dt = 0.025 
```
