# 17.3.3 MPC implementation guidance

Since we only need a rough approximation of the optimal trajectory at each timestep, there’s several ways to trade off accuracy for faster solves.

1. Make the optimization problem’s sample period much longer than the feedback controller’s sample period (reduces problem size for a given prediction horizon)   
2. Set a larger solver error tolerance (may reduce solver iterations)   
3. Use a solver that produces inexact solutions quickly (e.g., projected conjugate gradient method)

The prediction horizon should be long enough to capture relevant dynamics or future events. Longer prediction horizons yield more robustness but slower solves.

Warm starting the current timestep’s solve with the optimal trajectory from the previous timestep can drastically speed up convergence.

Set a solver timeout, because applying the control input from a partially optimized trajectory is better than overrunning the scheduled controller period.

Time-domain responses   
![](image/6f743ce7ebca4972c1ab4352e2771ebc582826368772474fc5abccf3e3ef7f75.jpg)

<details>
<summary>line</summary>

| Time | Reference | State |
|------|-----------|-------|
| 0    | 900       | 0     |
| 1    | 900       | 900   |
| 2    | 900       | 900   |
| 3    | 900       | 900   |
| 4    | 900       | 900   |
| 5    | 900       | 900   |
| 6    | 0         | 0     |
| 7    | 0         | 0     |
| 8    | 0         | 0     |
| 9    | 0         | 0     |
| 10   | 0         | 0     |
</details>

![](image/1b01815b606f4e475af7a5cf6074cd30e02ce24b402aeea76a5c6597b6d17ef9.jpg)

<details>
<summary>line</summary>

| Time (s) | Voltage (V) |
| -------- | ----------- |
| 0        | 0           |
| 0.5      | 12          |
| 1        | 12          |
| 1.5      | 4           |
| 2        | 4           |
| 3        | 4           |
| 4        | 4           |
| 5        | 4           |
| 5.5      | -12         |
| 6        | 0           |
| 7        | 0           |
| 8        | 0           |
| 9        | 0           |
| 10       | 0           |
</details>

Figure 17.4: Flywheel MPC response
