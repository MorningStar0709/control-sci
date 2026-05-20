| Type | Real Axis | Imaginary Axis |
| --- | --- | --- |
| sys[22] | 0.4 | 0.98 |
| sys[22] | 0.8 | 0.94 |
| sys[22] | 1.2 | 0.87 |
| sys[22] | 1.6 | 0.64 |
| sys[22] | 2.0 | 0.47 |
| sys[22] | 2.4 | 0.4 |
| sys[22] | 2.8 | 0.4 |
| sys[22] | 3.2 | 0.4 |
| sys[22] | 3.6 | 0.4 |
| sys[22] | 4.0 | 0.4 |
| sys[22] | 4.4 | 0.4 |
| sys[22] | 4.8 | 0.4 |
| sys[22] | 5.2 | 0.4 |
| sys[22] | 5.6 | 0.4 |
| sys[22] | 6.0 | 0.4 |
| sys[22] | 6.4 | 0.4 |
| sys[22] | 6.8 | 0.4 |
| sys[22] | 7.2 | 0.4 |
| sys[22] | 7.6 | 0.4 |
| sys[22] | 8.0 | 0.4 |
| sys[22] | 8.4 | 0.4 |
| sys[22] | 8.8 | 0.4 |
| sys[22] | 9.2 | 0.4 |
| sys[22] | 9.6 | 0.4 |
| sys[22] | 10.0 | 0.4 |
| sys[22] | 10.4 | 0.4 |
| sys[22] | 10.8 | 0.4 |
| sys[22] | 11.2 | 0.4 |
| sys[22] | 11.6 | 0.4 |
| sys[22] | 12.0 | 0.4 |
| sys[22] | 12.4 | 0.4 |
| sys[22] | 12.8 | 0.4 |
| sys[22] | 13.2 | 0.4 |
| sys[22] | 13.6 | 0.4 |
| sys[22] | 14.0 | 0.4 |
| sys[22] | 14.4 | 0.4 |
| sys[22] | 14.8 | 0.4 |
| sys[22] | 15.2 | 0.4 |
| sys[22] | 15.6 | 0.4 |
| sys[22] | 16.0 | 0.4 |
| sys[22] | 16.4 | 0.4 |
| sys[22] | 16.8 | 0.4 |
| sys[22] | 17.2 | 0.4 |
| sys[22] | 17.6 | 0.4 |
| sys[22] | 18.0 | 0.4 |
| sys[22] | 18.4 | 0.4 |
| sys[22] | 18.8 | 0.4 |
| sys[22] | 19.2 | 0.4 |
| sys[22] | 19.6 | 0.4 |
| sys[22] | 20.0 | 0.4 |
| sys[22] | - | - |
| sys[22] | - | - |
| sys[22] | - | - |
| sys[22] | - | - |
| sys[22] | - | - |
| sys[22] | - | - |
| sys[22] | - | - |
| sys[22] | - | - |
|
| sys[22] | - | - |
| --- | --- | --- |
| sys[22] | - | - |
| sys[22] | - | - |
| sys[22] | - | - |
| sys[22] | - | - |
| sys[22] | - | - |
| sys[22] | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS | - | - |
| SYS        *Target Pole*1
    *Settling Time =8 sec
    *Damping =3763
</details>

It's very cool that Claude.ai moved the PID controller zeros to about $- 1 . 5 \pm 1 . 2 j$ which indeed moved the RL in the right direction. And, since it has magnied the axes enough, We can see that the RL goes pretty close.

Clicking the RL nearest to the target gives a gain of $\mathrm { K = 0 . 5 1 2 }$ . The RL looks non-smooth in a couple of spots. This can be xed by giving control.RootLocus a custom gain vector, but let's skip that. (At this point, Claude gives a warning: Tip: Long chats cause you to reach your usage limits faster, and it never did get around to xing the extra stu in the legend.)
