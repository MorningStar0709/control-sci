# Computational Delay

Because A-D and D-A conversions and computations take time, there will always be a delay when a control law is implemented using a computer. The delay, which is called the computational delay, depends on how the control algorithm is implemented. There are basically two different ways to do this (see Fig. 9.2). In case A, the measured variables read at time $t_k$ may be used to compute the control signal to be applied at time $t_{k+1}$ . Another possibility, case B, is to read the measured variables at time $t_{k}$ and to make the D-A conversion as soon as possible.

![](image/6080ee5cb6a381f979f8634c72246fccb525df2e4cf4a24f0315bad035ba5172.jpg)

<details>
<summary>line</summary>

| Time Point | Measured Variable | Control Variable |
| --- | --- | --- |
| t_{k-1} | y(t_{k-1}) | u |
| t_k | y(t_k) | u(t_k) |
| t_{k+1} | y(t_{k+1}) | u(t_{k+1}) |
</details>

![](image/c1d2ff088137d894bf6bbec8dc22902dbb2da41f6d5610ba06595c7ef33ea81c.jpg)

<details>
<summary>line</summary>

| Time Point | Measured Variable | Control Variable |
| --- | --- | --- |
| t_{k-1} | y(t_{k-1}) | u(t_{k-1}) |
| t_k | y(t_k) | u(t_k) |
| t_{k+1} | y(t_{k+1}) | u(t_k) |
</details>

Figure 9.2 Two ways of synchronizing inputs and outputs. In case A the signals measured at time $t_{k}$ are used to compute the control signal to be applied at time $t_{k+1}$ . In case B the control signals are changed as soon as they are computed.

The disadvantage of case A is that the control actions are delayed unnecessarily; the disadvantage of case B is that the delay will be variable, depending on the programming. In both cases it is necessary to take the computational delay into account when computing the control law. This is easily done by including a time delay of h (case A) or $\tau$ (case B) in the process model. A good rule is to read the inputs before the outputs are set out. If this is not done, there is always the risk of electrical cross-coupling.

In case B it is desirable to make the computational delay as small as possible. This can be done by making as few operations as possible between the A-D and D-A conversions. Consider the program in Listing 9.1. Because the control signal u is available after executing the second line of code, the D-A conversion can be done before the state is updated. The delay may be reduced further by calculating the product C\*x after the D-A conversion. The algorithm in Listing 9.1 is then modified to Listing 9.2.

To judge the consequences of computational delays, it is also useful to know the sensitivity of the closed-loop system to a time delay. This may be evaluated from a root locus with respect to a time delay. A simpler way is to evaluate how much the closed-loop poles change when a time delay of one sampling period is introduced.

Listing 9.2 Computer code skeleton that implements the control algorithm (9.2). This code has a smaller computational delay than the code in Listing 9.1.   
```txt
Procedure Regulate
begin
1 Adin y uc
2 u:=u1+D*y+Dc*uc
3 Daout u
4 x:=F*x+G*y+Gc*uc
5 u1:=C*x
end 
```
