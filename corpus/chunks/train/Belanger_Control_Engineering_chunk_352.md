# Example 6.15 (dc Servo)

In Example 6.11, a lead-lag compensator was used to achieve a bandwidth of 3 rad/s, with desirable low-frequency properties. Design a 2-DOF system to extend the bandwidth to 10 rad/s, for the set-point response.

Solution The compensator from Example 6.11 is

$$F (s) = G _ {c} (s) = 2. 2 8 \frac {(1 . 1 4 s + 1) (0 . 6 3 0 s + 1)}{(1 . 7 6 s + 1) (0 . 1 7 7 s + 1)}.$$

Figure 6.31 shows the inverse complementary sensitivity $T(j\omega)$ . A rough approximation is given by $s / 4 + 1$ . To obtain a proper compensator, we use a lead:

$$R ^ {\prime} = \frac {(s / 4) + 1}{(s / 4 0) + 1}.$$

The two compensators are:

Forward path: $F = 2.28\frac{(1.14s + 1)(.630s + 1)(.25s + 1)}{(1.76s + 1)(.177s + 1)(.025s + 1)}$

Feedback path: $\frac{1}{R'} = \frac{0.25s + 1}{.25s + 1}$ .

Figure 6.32 shows the responses for the 1-DOF and 2-DOF designs.

![](image/dbf68a767f182638bd2c112c6a3b1e8e88266540f5a35a5c71e5997bb6b27965.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | db |
| --- | --- |
| 10^0 | 0 |
| 10^1 | 13 |
</details>

![](image/0463330fa0ecc81070a79ee3e65697b5a54a8a496d7b1ca91db1d920459709d1.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | deg |
| --- | --- |
| 1 | 20 |
| 10 | 50 |
| 100 | 100 |
| 1000 | 150 |
</details>

Figure 6.31 Inverse of complementary sensitivity

![](image/bd207a4077ba935831f1b8c85a7bf5f4d82bffb95a6bb511eed0971275079a33.jpg)

<details>
<summary>line</summary>

| Frequency (rad/s) | 1-DOF response (db) | 2-DOF response (db) |
| --- | --- | --- |
| 10^0 | ~0 | ~0 |
| 10^1 | ~0 | ~0 |
| 10^2 | ~0 | ~0 |
| 10^3 | ~-2 | ~2 |
| 10^4 | ~-6 | ~2 |
| 10^5 | ~-10 | ~0 |
| 10^6 | ~-14 | ~-4 |
</details>

Figure 6.32 Frequency responses, 1-DOF and 2-DOF designs
