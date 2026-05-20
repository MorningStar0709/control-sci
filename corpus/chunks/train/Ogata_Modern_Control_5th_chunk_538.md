```mermaid
graph LR
    A["R(s)"] --> B["+"]
    B --> C["K/(s(s+1) (s+5))"]
    C --> D["C(s)"]
    D --> E["Feedback"]
    E --> B
```
</details>

A–7–4. Using MATLAB, plot Bode diagrams for the closed-loop system shown in Figure 7–120 for K=1, K=10, and K=20. Plot three magnitude curves in one diagram and three phase-angle curves in another diagram.

Solution. The closed-loop transfer function of the system is given by

$$
\begin{array}{l} \frac {C (s)}{R (s)} = \frac {K}{s (s + 1) (s + 5) + K} \\ = \frac {K}{s ^ {3} + 6 s ^ {2} + 5 s + K} \\ \end{array}
$$

Hence the numerator and denominator of $C ( s ) / R ( s )$ are

$$
\begin{array}{l} \mathrm{num} = [ \mathrm{K} ] \\ \mathrm{den} = [ 1 \quad 6 \quad 5 \quad K ] \\ \end{array}
$$

A possible MATLAB program is shown in MATLAB Program 7–16.The resulting Bode diagrams are shown in Figures 7–121(a) and (b).

MATLAB Program 7–16   
w = logspace(-1,2,200);
for i = 1:3;
    if i = 1; K = 1; [mag, phase, w] = bode([K], [1 6 5 K], w);
    mag1dB = 20*log10(mag); phase1 = phase; end;
    if i = 2; K = 10; [mag, phase, w] = bode([K], [1 6 5 K], w);
    mag2dB = 20*log10(mag); phase2 = phase; end;
    if i = 3; K = 20; [mag, phase, w] = bode([K], [1 6 5 K], w);
    mag3dB = 20*log10(mag); phase3 = phase; end;
end
semilogx(w, mag1dB, '-', w, mag2dB, '-', w, mag3dB, '-')
grid
title('Bode Diagrams of G(s) = K/[s(s + 1)(s + 5)], where K = 1, K = 10, and K = 20')
xlabel('Frequency (rad/sec)')
ylabel('Gain (dB)')
text(1.2,-31,'K = 1')
text(1.1,-8,'K = 10')
text(11,-31,'K = 20')
semilogx(w, phase1, '-', w, phase2, '-', w, phase3, '-'')
grid
xlabel('Frequency (rad/sec)')
ylabel('Phase (deg)')
text(0.2,-90,'K = 1')
text(0.2,-20,'K = 10')
text(1.6,-20,'K = 20')

![](image/c0f49c7039c296b7917ace1c21d5d8e221652159802b3c051cd9518be794eb78.jpg)

<details>
<summary>line</summary>

| Frequency (rad/sec) | Gain (dB) for K=1 | Gain (dB) for K=10 | Gain (dB) for K=20 |
| --- | --- | --- | --- |
| 0.1 | ~0 | ~0 | ~0 |
| 1 | ~-20 | ~10 | ~18 |
| 10 | ~-60 | ~-30 | ~-40 |
| 100 | ~-120 | ~-90 | ~-100 |
</details>

![](image/53937d693d68efcd26bb74ec637abdf18e8f5ce2c320dd0c668b9af8d4b3b184.jpg)

<details>
<summary>line</summary>

| Frequency (rad/sec) | K = 1 | K = 10 | K = 20 |
| --- | --- | --- | --- |
| 0.1 | -30 | -10 | 0 |
| 1 | -150 | -50 | -20 |
| 10 | -250 | -150 | -180 |
| 100 | -280 | -250 | -270 |
</details>

(b)   
Figure 7–121 Bode diagrams: (a) Magnitudeversus-frequency curves; (b) phaseangle-versusfrequency curves.

A–7–5. Prove that the polar plot of the sinusoidal transfer function
