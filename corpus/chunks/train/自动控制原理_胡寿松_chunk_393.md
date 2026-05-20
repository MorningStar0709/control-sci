# (2) D/A 转换器

D/A 转换器是把离散的数字信号转换为连续模拟信号的装置。D/A 转换也经历了两个过程：一是解码过程，把离散数字信号转换为离散的模拟信号，如图7-8(a)所示；二是复现过程，因为离散的模拟信号无法直接控制连续的被控对象，需要经过保持器将离散模拟信号复现为连续的模拟信号，如图7-8(b)所示。

![](image/607bde61290cbd25aafba377215f928127f72d00a2aea76c0636af3ee1f7d996.jpg)

<details>
<summary>line</summary>

| t | e(t) |
| --- | --- |
| 0 | e(t) |
| t* | 0 |
</details>

(a)

![](image/4f19a70cf416549032fc16758d5dcd73e0318536b9397e3285d5f65e7ccf22af.jpg)

<details>
<summary>bar_line</summary>

| Time (t) | e*(t) |
| --- | --- |
| 0 | 10 |
| T | 8 |
| 2T | 6 |
| 3T | 4 |
| 4T | 2 |
| 5T | 1 |
| 6T | 0 |
</details>

(b)

![](image/b8c4d2478074f082f022efe0719f4420eaa214bb4ef8341ed9f83c7cefff6746.jpg)

<details>
<summary>line</summary>

| t | q |
| --- | --- |
| 0 | 5q |
| T | 5q |
| 2T | 4q |
| 3T | 3q |
| 4T | 2q |
| 5T | 1q |
| 6T | 0 |
</details>

(c)   
图 7-7 A/D 转换过程

![](image/3b75f8ac106719f41229bf257062ef1e3ecb2a0f5a1210dcf9f9f98353aadc2b.jpg)

<details>
<summary>scatter</summary>

| t | u*(t) |
| --- | --- |
| 0 | 0 |
| T | q |
| 2T | 2q |
| 3T | 3q |
| 4T | 3q |
| 5T | 4q |
| 6T | 4q |
| 7T | 5q |
</details>

(a)

![](image/d184750f68f9f59b088793e5088541bada62f9f89d403eed8c1eaf2848dfe6e4.jpg)

<details>
<summary>line</summary>

| Time | u_H(t) |
| --- | --- |
| T | 0 |
| 2T | 2q |
| 3T | 3q |
| 4T | 3q |
| 5T | 4q |
| 6T | 4q |
| 7T | 5q |
| End | q |
</details>

(b)   
图 7-8 D/A 转换过程

计算机的输出寄存器和解码网络起到了信号保持器的作用。显然，在图7-8(b)中经保持后的 $u_{h}(t)$ 只是一个阶梯信号，但是当采样频率足够高时， $u_{h}(t)$ 将趋近于连续信号。
