# MATLAB Program 10–23

% ---------- Unit-step response of designed system

$$A = [ 0 \quad 1 \quad 0; 0 \quad 0 \quad 1; 0 \quad - 2 \quad - 3 ];B = [ 0; 0; 1 ]C = [ 1 \quad 0 \quad 0 ];D = [ 0 ];K = [ 1 0 0. 0 0 0 0 5 3. 1 2 0 0 1 1. 6 7 1 1 ];\mathrm{k} 1 = \mathrm{K} (1); \mathrm{k} 2 = \mathrm{K} (2); \mathrm{k} 3 = \mathrm{K} (3);$$

% \*\*\*\*\* Define the state matrix, control matrix, output matrix,

% and direct transmission matrix of the designed systems as AA,

% BB, CC, and DD \*\*\*\*\*

$$A A = A - B ^ {*} K;\mathrm{BB} = \mathrm{B} ^ {*} \mathrm{k} 1;C C = C;D D = D;t = 0: 0. 0 1: 8;[ y, x, t ] = \text { step } (A A, B B, C C, D D, 1, t);\operatorname{plot} (t, x)\mathrm{grid}$$

title('Response Curves x1, x2, x3, versus t')

$$\text { xlabel('t Sec') }\text { ylabel } (^ {\prime} x 1, x 2, x 3 ^ {\prime})\text { text } (2. 6, 1. 3 5, ^ {\prime} x 1 ^ {\prime})\text { text } (1. 2, 1. 5, ^ {\prime} x 2 ^ {\prime})\text { text } (0. 6, 3. 5, ^ {\prime} x 3 ^ {\prime})$$

Figure 10–40

Response curves x versus t, x versus t, and x versus t.

Response Curves x1, x2, x3 versus t   
![](image/7637597308be9c03b31ad8767a90d80c30f57b6abd918006318b9b4c44172606.jpg)

<details>
<summary>line</summary>

| t Sec | x1 | x2 | x3 |
| --- | --- | --- | --- |
| 0 | 0.0 | 0.0 | 5.0 |
| 1 | -2.0 | 1.0 | 1.0 |
| 2 | 0.0 | 1.0 | 1.0 |
| 3 | 0.0 | 1.0 | 1.0 |
| 4 | 0.0 | 1.0 | 1.0 |
| 5 | 0.0 | 1.0 | 1.0 |
| 6 | 0.0 | 1.0 | 1.0 |
| 7 | 0.0 | 1.0 | 1.0 |
| 8 | 0.0 | 1.0 | 1.0 |
</details>
