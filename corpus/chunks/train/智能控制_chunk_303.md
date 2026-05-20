| time(s) | position tracking1 | position tracking2 |
| --- | --- | --- |
| 0 | 0.0 | 0.0 |
| 2 | 0.4 | 0.3 |
| 4 | -0.3 | -0.4 |
| 6 | 0.3 | 0.3 |
| 8 | 0.4 | 0.3 |
| 10 | -0.2 | -0.1 |
</details>

图5-24 双关节位置跟踪  
![](image/5beedd51e76fdc9645f15ffd8c299896296ae344e4dc28da35a19a180ee6b2ee.jpg)

<details>
<summary>line</summary>

| time(s) | F/Fc (Top Plot) | F/Fc (Bottom Plot) |
| --- | --- | --- |
| 0 | ~50 | ~40 |
| 1 | ~0 | ~10 |
| 2 | ~-10 | ~-10 |
| 3 | ~-10 | ~-10 |
| 4 | ~-10 | ~-10 |
| 5 | ~10 | ~10 |
| 6 | ~10 | ~10 |
| 7 | ~10 | ~10 |
| 8 | ~-10 | ~-10 |
| 9 | ~-10 | ~-10 |
| 10 | ~-10 | ~-10 |
</details>

图5-25 双关节摩擦及其补偿

![](image/fbbbf4eba66621858348e9876804b441198a9a925d22cf762020bf86f820ff9b.jpg)

<details>
<summary>line</summary>

| time(s) | Control input of Link 1 | Control input of Link 2 |
| --- | --- | --- |
| 0 | ~50 | ~30 |
| 1 | ~0 | ~10 |
| 2 | ~-5 | ~-10 |
| 3 | ~-5 | ~-10 |
| 4 | ~-5 | ~-10 |
| 5 | ~10 | ~10 |
| 6 | ~10 | ~10 |
| 7 | ~10 | ~10 |
| 8 | ~-5 | ~-10 |
| 9 | ~-5 | ~-10 |
| 10 | ~-5 | ~-10 |
</details>

图5-26 双关节控制输入

基于摩擦模糊补偿的机械手控制程序有:①Simulink 主程序,chap5\_6sim.mdl;②控制器 S 函数,chap5\_6ctrl.m;③被控对象 S 函数,chap5\_6plant.m;④作图程序,chap5\_6plot.m;⑤隶属函数设计程序 chap5\_6mf.m。程序见附录。
