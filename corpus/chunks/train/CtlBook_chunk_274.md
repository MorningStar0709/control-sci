# Example 8.2 cont.

First we generate a conventional step response a from input (road displacement x1) to car body displacement (x2)

![](image/09ce6cf4b4dee00ff7fa416efc0ca08cf9af842def8401307a88a4e116581b9f.jpg)

<details>
<summary>line</summary>

| Time [s] | Amplitude |
| --- | --- |
| 0.00 | 0.0 |
| 0.25 | 0.6 |
| 0.50 | 1.0 |
| 0.75 | 1.3 |
| 1.00 | 1.4 |
| 1.25 | 1.3 |
| 1.50 | 1.2 |
| 1.75 | 1.0 |
| 2.00 | 0.9 |
</details>

Step response of the car suspension system (overshoot indicates shocks probably worn out. Time for new ones!.)

Then, we can visualize all four state variables as they respond to a step input at x1.

Let's visualize the step response in state space instead of the time domain. We'll choose a plane which is a subspace of state space: [x3, x˙ 3]. We add the following lines to the script:

```txt
