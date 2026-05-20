# MATLAB Problems

3.20 Consider again the RC circuit in Problem 3.14. Plot the energy stored by the capacitor vs. time during the discharge phase $t \geq 0$ .   
3.21 A series RL circuit is driven by a constant 2-V voltage source (see Fig. 3.7 in Example 3.1). The system parameters are $L { = } 0 . 0 8 \mathrm { H }$ and $R = 4 \Omega$ . As we see in Chapter 7, the resulting current response for this system is

$$I _ {L} (t) = 0. 5 \left(1 - e ^ {- 5 0 t}\right) \mathrm{A}$$

Use MATLAB to compute the energy stored by the inductor for time $0 \leq t \leq 0 . 2 \mathrm { s }$ . Plot stored energy vs. time.

3.22 In Problem 3.11 the following empirical relationship relating inductor current $I _ { L }$ and magnetic flux linkage ?? was used

$$I _ {L} (\lambda) = 9 7. 3 \lambda^ {3} + 4. 2 \lambda (\mathrm{amps,A})$$

a. Use MATLAB to plot current $I _ { L }$ as a function of flux linkage ?? for the range $- 0 . 4 \leq \lambda \leq 0 . 4 \mathrm { W b }$   
b. Use the data from part (a) to plot flux linkage ?? as a function of current $I _ { L }$ .   
c. Write an M-file that uses the plot data from part (b) to estimate the inductance L and plot inductance as a function of flux linkage ?? [Hint: recall that inductance is $L = d \lambda / d I _ { L } ]$ ].
