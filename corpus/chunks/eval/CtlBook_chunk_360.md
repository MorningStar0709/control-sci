Looking at the printed outputs, we get a report of the best results for each weight vector. From the top, for example is the search that weights only settling time. With the gains $K _ { p } = 7 . 3 , K _ { I } = 2 9 . 9 , K _ { D } = 0 . 5 \bar { 6 }$ , $T _ { S } = 0 . 5 5$ . Exactly at the goal. Overshoot was a bit below the spec (which could be good actually depending on the application). Steady state error is little or none (excellent for most applications). Peak control eort is about 12 - we can match this with motor specications. Finally the gain margin of 80dB is excellent: there seems to be a low chance of component tolerances or plant wear and tear changing the model enough to drive it unstable.

If we try to achieve all our specs, let's look at the Balanced report (Wbal). That one has slower settling, too much overshoot and a worse but still good SSE.

The nal weight result (W\_BH) considers only the $T _ { S } ( 6 0 \% )$ and %OS(40%) specs, and SSE and Gain Margin are solid.

This is a really nice result overall but control eort is about double the Balanced result and we reached a search boundary $( K _ { d m i n } = 0 . 1 1 2 )$ on the balanced weights

As a result, let's do

Search 2:

We will choose gains between the Balanced and W\_BH gains:

$$K _ {p} = 1 0. 0, K _ {i} = 1 5, K _ {d} = 0. 2$$

and reduce the search range to 2.

We are still hitting a search boundary so this time we will take the balanced gains below, and just reduce KD $K _ { D }$

Reporting: Wbal

[Balanced Kp: 11.892 Ki: 12.613 Kd: 0.141

Settling Time: 0.930 Overshoot: 44.141 % SSE: 0.000 Ctl Effort: 9.897 Gain Marg: 13.5 dB ]

![](image/1e16375c6587415ac3e25617eae94d0edaec59ef66862f90c65a98aa40b00c85.jpg)

<details>
<summary>line</summary>

| Time (s) | WTS | WOS | WSSE | WU |
| --- | --- | --- | --- | --- |
| 0.0 | 0.0 | 1.0 | 1.0 | 1.0 |
| 0.2 | 0.6 | 1.0 | 1.0 | 1.0 |
| 0.4 | 1.18 | 1.0 | 1.0 | 1.0 |
| 0.6 | 1.05 | 1.0 | 1.0 | 1.0 |
| 0.8 | 0.95 | 1.0 | 1.0 | 1.0 |
| 1.0 | 0.98 | 1.0 | 1.0 | 1.0 |
</details>

Figure 10.4: Simulation result of nal design.

Search 3:

$$K _ {p} = 1 0. 0, K _ {i} = 1 5, K _ {d} = 0. 0 5$$

This is a pretty good compromise between overshoot close to 20% and $T _ { S }$ close to 0.55. SSE is great, Gain margin is great, and we now now what amount of control eort is to be expected for this performance. The step response we get using the balanced gains is given in Figure 10.4:
