# Addressing Steady State Error

You're right about the steady state error. This is a common issue when we introduce control effort saturation and must prioritize multiple performance criteria. Let's modify the controller to improve steady state accuracy while maintaining good transient response:

[ Code Version 5 ]

I've created version 5 with the improved steady state error handling. This version includes:

Enhanced anti-windup implementation using back-calculation to better maintain integral action while preventing windup Modified scoring function that heavily penalizes steady state error Increased integral gain range to better eliminate steady state error Detailed performance metrics that report the actual steady state value and error Set point clearly labeled on plots for better visualization of steady state error Shortened time range to 0-4 seconds to better visualize the transient response Added plt.show() at the end to ensure plots are displayed

This version balances all the important control performance criteria:

Good transient response Limited control effort (within ±10 units) Improved steady state accuracy

You can now run this script independently to design a PID controller that addresses the previously observed steady state error while still respecting actuator

limitations.RetryClaude can make mistakes. Please double-check responses.

Thank you! Over and out.

![](image/0014da450b2cff463e947a04f56fb4676ad918b94cedcc566ef0e3793e742cea.jpg)

<details>
<summary>line</summary>

| Time (s) | With Saturation | Without Saturation |
| --- | --- | --- |
| 0.0 | 0.0 | 0.0 |
| 0.5 | 0.9 | 1.1 |
| 1.0 | 1.0 | 0.9 |
| 1.5 | 1.0 | 0.95 |
| 2.0 | 1.0 | 0.98 |
| 2.5 | 1.0 | 0.99 |
| 3.0 | 1.0 | 1.0 |
| 3.5 | 1.0 | 1.0 |
| 4.0 | 1.0 | 1.0 |
</details>

![](image/f6f4fe58430be5bd439d207a67630ca391bbde5141101def49ce65d841ec0f08.jpg)

<details>
<summary>line</summary>

| Time (s) | With Saturation | Without Saturation | Saturation Limit (±10.0) |
| --- | --- | --- | --- |
| 0.0 | 10.0 | 80.0 | 10.0 |
| 0.5 | 0.0 | 0.0 | 10.0 |
| 1.0 | 0.0 | 0.0 | 10.0 |
| 1.5 | 0.0 | 0.0 | 10.0 |
| 2.0 | 0.0 | 0.0 | 10.0 |
| 2.5 | 0.0 | 0.0 | 10.0 |
| 3.0 | 0.0 | 0.0 | 10.0 |
| 3.5 | 0.0 | 0.0 | 10.0 |
| 4.0 | 0.0 | 0.0 | 10.0 |
</details>

Sp25 HW 9.7 Claude Solution Controller V05

![](image/75cf83bf611c03a91221628c0e866342ddb0db69c3fbdef27b9af577d3b567e8.jpg)

<details>
<summary>line</summary>
