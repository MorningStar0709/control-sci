![](image/02cbf4b6c0b4b3cf3d2d5c144d6003db6d02e06a2ff506c102f7b766bfe43f26.jpg)

<details>
<summary>line</summary>

| x | v(t) | y(t) |
| --- | --- | --- |
| 0 | 0.0 | 0.5 |
| 100 | 0.5 | 0.5 |
| 200 | 0.5 | 0.5 |
| 300 | 0.5 | 0.5 |
| 400 | 0.5 | 0.5 |
| 500 | 0.5 | 0.5 |
</details>

![](image/d3a2c457e37d6b852a6a7857f698e309d61dcd0c5f236a62f5491e8521dd53bc.jpg)

<details>
<summary>line</summary>

| t | u(t)/2 | v(t) |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 100 | 0.5 | 1.0 |
| 200 | 0.5 | 1.0 |
| 300 | 0.5 | 1.0 |
| 400 | 0.5 | 1.0 |
| 500 | 0.5 | 1.0 |
</details>

![](image/fe4eb9b289661ea5c28a0a1c9ff949b7cbd06e6ad554229c617869a106ec9a26.jpg)

<details>
<summary>line</summary>

| t | v(t) | y(t) |
| --- | --- | --- |
| 0 | 0 | 0 |
| 100 | 0.5 | 1 |
| 200 | 1 | 1 |
| 300 | 1 | 1 |
| 400 | 1 | 1 |
| 500 | 1 | 1 |
</details>

![](image/e7c1e79efce274d731b22003233f3637b7ca8cf2a7df4f4b5bda62d2d07d7f4c.jpg)

<details>
<summary>line</summary>

| t | v₁(t) | u(t)/2 |
| --- | --- | --- |
| 0 | 0 | 0 |
| 100 | 0.5 | 0.4 |
| 200 | 1 | 0.5 |
| 300 | 1 | 0.5 |
| 400 | 1 | 0.5 |
| 500 | 1 | 0.5 |
</details>

图6.3.2

在这两种仿真结果的过渡过程时间基本上是时滞时间的五倍以上.

下面图6.3.3和图6.3.4分别显示的是控制器参数不变,对象时间常数上浮30%和下浮30%时的情形.

![](image/334a7ee956a598e740730f12d2db446485b6584360a3e81bdec489784a2cd267.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 0.0 |
| 100 | 1.0 |
| 500 | 0.5 |
| 1000 | 0.5 |
</details>

![](image/c10959eaf2a332739bf3c9706843e9e5abc154214dc4e59c3884423201fe7bba.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 0.0 |
| 100 | 0.5 |
| 200 | 0.8 |
| 300 | 0.9 |
| 400 | 0.95 |
| 500 | 0.9 |
| 600 | 0.85 |
| 700 | 0.8 |
| 800 | 0.75 |
| 900 | 0.7 |
| 1000 | 0.65 |
</details>

![](image/a868192652f30bd8743b27537d93fa90f940ee511cb28b828af8d11eda88632b.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 0.0 |
| 100 | 0.5 |
| 200 | 1.0 |
| 300 | 1.0 |
| 400 | 1.0 |
| 500 | 1.0 |
| 600 | 1.0 |
| 700 | 1.0 |
| 800 | 1.0 |
| 900 | 1.0 |
| 1000 | 1.0 |
</details>

![](image/cb139223f7647bbd383e47af237ee499a6d941c88b0e477dfc1f2b6ba62e94c6.jpg)

<details>
<summary>line</summary>

| x | y1 | y2 |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 500 | 1.0 | 0.4 |
| 1000 | 1.0 | 0.4 |
</details>

图6.3.3

(3) 输出预估法. 我们先看看著名的 Smith 预估法的实质. Smith 预估法的基本框图为图 6.3.5.

![](image/ad4c777a6595d06293930181bf3644fc359a5adeac74e37126b2b53d5476d34c.jpg)

<details>
<summary>line</summary>

| x | y |
| --- | --- |
| 0 | 0.0 |
| 500 | 0.5 |
| 1000 | 0.5 |
</details>
