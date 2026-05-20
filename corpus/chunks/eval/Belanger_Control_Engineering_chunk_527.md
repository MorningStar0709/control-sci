# 9.2.1 The Impulse Samples

Figure 9.2 shows the sample-and-hold operation. The signal $y(t)$ is sampled at $t = kT_s$ , $k = 0, 1, 2, \ldots$ , and a new signal $y'(t)$ is constructed simply by holding the value until the next sampling time. We may give this operation a mathematical expression through (i) multiplication of $y(t)$ by the periodic train of impulses of unit area, $p(t)$ , shown in Figure 9.3a, and (ii) passing the resulting signal through a linear, time-invariant (LTI) system whose impulse response is shown in Figure 9.3b. The process is illustrated in Figure 9.4. Multiplication by the impulse train yields

![](image/c8a3ebbefef2acba5e6f0e429ff8ed8c24996c7bdce0844a2b1a0dc50974c811.jpg)

<details>
<summary>line</summary>

| t | y'(t) |
| --- | --- |
| 0 | 1 |
| Ts | 0.5 |
| 2Ts | 0.5 |
| 3Ts | 1 |
| 4Ts | 2 |
| 5Ts | 4 |
| 6Ts | 5 |
| 7Ts | 4 |
| 8T | 3 |
</details>

Figure 9.2 Illustration of a sample-and-hold operation

![](image/1ffb3107dc91b101da2d6e612535c73413e917d71e49988b979f9c7fb0a8b237.jpg)

<details>
<summary>text_image</summary>

1
0 Ts 2Ts 3Ts 4Ts 5Ts 6Ts 7Ts t
</details>

Figure 9.3a A periodic string of unit impulses

![](image/2bd8034d348f7281e8532f19ba719a9c5091cff0144acf3657bc99bcb9c2f1ec.jpg)

<details>
<summary>line</summary>

| t | h(t) |
| --- | --- |
| 0 | 1 |
| Ts | 1 |
| Ts + t | 0 |
</details>

Figure 9.3b Impulse response of a zero-order hold

$$y ^ {*} (t) = \sum_ {k = 0} ^ {\infty} y (k T _ {s}) u _ {0} (t - k T _ {s}) \tag {9.1}$$

and passage through the LTI system gives

$$y ^ {\prime} (t) = \sum_ {k = 0} ^ {\infty} y (k T _ {s}) h (t - k T _ {s}). \tag {9.2}$$

Henceforth, we shall refer to sampling as multiplication by a periodic train of unit impulses. Figure 9.5 shows the symbol used to represent this operation, with $T_{s}$ as the sampling period. This is never implemented in reality; it is just a convenient mathematical representation of the process. Formally, we may write the

![](image/159f66375c976f342d2d507c16481a00de207ca95a41fe47efeef0321960c3de.jpg)

<details>
<summary>line</summary>

| t | y(t) | y*(t) |
| --- | --- | --- |
| 0 | 1.0 | 1.0 |
| Ts | 0.5 | 0.5 |
| 2Ts | 0.25 | 0.25 |
| 3Ts | 0.25 | 0.25 |
| 4Ts | 0.5 | 0.5 |
| 5Ts | 0.75 | 0.75 |
| 6Ts | 1.0 | 1.0 |
</details>

Figure 9.4 Multiplication by a periodic string of unit impulses and passing through a zero-order hold

![](image/9ebdd67d86e891400f8ba21dcd6976be469691ce982add45594fb9e6520cde04.jpg)

<details>
<summary>text_image</summary>
