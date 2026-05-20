# 2.5 Response types

A system driven by a PID controller generally has three types of responses: underdamped, overdamped, and critically damped. These are shown in figure 2.9.

For the step responses in figure 2.9, rise time is the time the system takes to initially reach the reference after applying the step input. Settling time is the time the system takes to settle at the reference after the step input is applied.

An underdamped response oscillates around the reference before settling. An overdamped response is slow to rise and does not overshoot the reference. A critically damped response has the shortest rise time without oscillating around the reference (i.e., overshooting then undershooting).

![](image/e3a0906018bb54b81c6fa7fd19e27ae6b249a12673b0c9b403aa9209294d45b9.jpg)

<details>
<summary>line</summary>

| Time (s) | Setpoint | Underdamped | Overdamped | Critically damped |
| --- | --- | --- | --- | --- |
| 0 | 1.0 | 0.0 | 0.0 | 0.0 |
| 1 | 1.0 | 1.1 | 0.4 | 0.8 |
| 2 | 1.0 | 1.0 | 0.7 | 0.95 |
| 3 | 1.0 | 1.0 | 0.85 | 0.98 |
| 4 | 1.0 | 1.0 | 0.9 | 0.99 |
| 5 | 1.0 | 1.0 | 0.95 | 0.995 |
| 6 | 1.0 | 1.0 | 0.98 | 0.998 |
</details>

Figure 2.9: PID controller response types
