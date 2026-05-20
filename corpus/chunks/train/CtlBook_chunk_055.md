# Example 2.1

Convert the tire, wheel, and suspension elements of a typical car to a linear mass-spring-damper model.

![](image/0498495399db2066ce7f8009c0f03e8afd926c0527f9cc0288a7a0161611689b.jpg)

<details>
<summary>text_image</summary>

Mv
Mass of Car
4
Suspension
Mw
Wheel Mass
Tire
</details>

In this conversion we have used lots of knowledge about cars including the following facts:

 Tires are elastic and lled with a low mass material (air) and thus could plausibly be approximated by a spring.   
 The weight of the wheel and tire can be combined into a mass.   
 The suspension spring goes between the suspension beam and the car's body.   
 Cars have four wheels so the mass of the body should be approximated by 1/4 of the car's total mass.   
 The shock absorber is a damper which connects between the suspension arm and the car body (in parallel with the spring)   
 The suspension arm is long enough compared to the tire's motion such that we can approximate the tire's motion as a straight vertical line.

None of this knowlege is required to excel at control systems design with one exception, The control system designer must have enough knowlege of the application system or access to enough model validation data to make sure that the simplied model is good enough for all application requirements. To the extent that these facts are true, our model is accurate, and to the extent that this model is an oversimplication, our model will not work.

It can scarcely be denied that the supreme goal of all theory is to make the irreducible basic elements as simple and as few as possible without having to surrender the adequate representation of a single datum of experience.

Albert Einstein
