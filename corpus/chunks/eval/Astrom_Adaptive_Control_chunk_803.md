# Michie's Boxes

This system grew out of early work on artificial intelligence (see Michie and Chambers, 1968) and attempts to balance an inverted pendulum (see Fig. 13.8). The system has four state variables, $\varphi$ , $\dot{\varphi}$ , $x$ , and $\dot{x}$ , which are quantized in a crude way, with five levels for the position variables $x$ and $\varphi$ and three levels for the velocity variables $\dot{x}$ and $\dot{\varphi}$ . The state space can thus be described by 225 discrete states. The control variable is quantized into two levels: force left ( $L$ ) or force right ( $R$ ). The control law can be represented by a binary table with 225 entries. In the experiment the table was initialized with randomly chosen $L$ 's and $R$ 's in the table. A simple scoring method was used to update the table entries as a result of experimental runs. Scoring was based on how long the pendulum stayed upright and the number of times the pendulum was in a discrete state. The system was able to balance the pendulum for about 25 minutes after a 60-hour training period. The table that defines the control action can be expressed in logic as:

If cart is far left and cart is hardly moving and pendulum is hardly leaning and pendulum is swinging to right then apply force right.

For this reason the control law is also called linguistic control. When the logic is replaced by fuzzy logic, it is also called fuzzy control.

The training algorithm that is used in Michie's Boxes is similar to that used in programs for playing checkers and chess, but the pendulum problem is simpler than game playing. Training can be shortened by using a teacher, that is, by applying a scoring algorithm to an experiment in which the pendulum is balanced by an expert. A learning system of this type is obviously closely related to a model-reference adaptive system. The reference model can be viewed as a teacher.

![](image/51dbc61752e89e665a3943db772e6bcd9304161fb135695ef2389f01c57d353f.jpg)

<details>
<summary>text_image</summary>

x
φ
</details>

Figure 13.8 An inverted pendulum.
