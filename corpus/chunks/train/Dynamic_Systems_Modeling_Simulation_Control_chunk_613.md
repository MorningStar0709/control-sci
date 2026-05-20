# Gain and Phase Margins Using MATLAB

The MATLAB command margin will compute the gain and phase margins and the corresponding crossover frequencies of an LTI system. Let us demonstrate its use with the previous example where Eq. (10.54) presents the open-loop transfer function

```matlab
>> sysG = tf(1, [1 5 6 0])    % create G(s) = 1/(s³ + 5s² + 6s)
>> Kp = 2;    % P-gain setting
>> [Gm, Pm, Wgm, Wpm] = margin(Kp*sysG)    % compute gain and phase margins 
```

The input to the command margin is the system’s open-loop transfer function KG(s)H(s) and the computed output values are gain margin Gm (as a multiplicative factor), phase margin Pm (in degrees), phase-crossing frequency for measuring the gain margin Wgm (in rad/s), and unity-gain crossover frequency for measuring the phase margin Wpm (in rad/s). Executing these commands yields

$$G m = 1 5. 0 0 0 0\mathrm{Pm} = 7 4. 4 9 2 3 (\text { degrees })\mathrm{Wgm} = 2. 4 4 9 5 (\mathrm{rad/s})\mathrm{Wpm} = 0. 3 2 7 0 (\mathrm{rad/s})$$

which is the same result obtained from the Bode diagram in Fig. 10.53. If we want to compute the gain margin in decibels, we must add the command

$$> > \mathrm {Gm\_dB} = 2 0 * \log 1 0 (\mathrm{Gm})$$

Another way to use the command margin is to execute it without the left-hand side arguments

$$> > \text { margin } (K p * s y s G)$$

% plot Bode diagram and display gain and phase margins

which creates the Bode diagram of LTI system sysG and displays the gain and phase margins on the magnitude and phase plots in a similar manner as in Fig. 10.53. Figure 10.54 shows the result of the margin command. Numerical values for gain and phase margins and their respective crossover frequencies are automatically displayed in the figure title.

![](image/cd8e5c0686e4dfb026173bf1b652ffa098bb909aa65d6f7ee332aa4e0b0b2a7e.jpg)

<details>
<summary>line</summary>

| Frequency (rad/sec) | Magnitude (dB) | Phase (deg) |
| --- | --- | --- |
| 0.01 | ~30 | -90 |
| 0.1 | ~0 | -135 |
| 1 | ~-30 | -180 |
| 10 | ~-60 | -225 |
| 100 | ~-120 | -270 |
</details>

Figure 10.54 Bode diagram created by MATLAB’s margin command for the open-loop transfer function $2 / ( s ^ { 3 } + 5 s ^ { 2 } + 6 s )$ showing gain and phase margins.
