# Exercise A.47: Let’s make a deal!

Consider the following contest of the American television game show of the 1960s, Let’s Make a Deal. In the show’s grand finale, a contestant is presented with three doors. Behind one of the doors is a valuable prize such as an all-expenses-paid vacation to Hawaii or a new car. Behind the other two doors are goats and donkeys. The contestant selects a door, say door number one. The game show host, Monty Hall, then says,

“Before I show you what is behind your door, let’s reveal what is behind door number three!” Monty always chooses a door that has one of the booby prizes behind it. As the goat or donkey is revealed, the audience howls with laughter. Then Monty asks innocently,

“Before I show you what is behind your door, I will allow you one chance to change your mind. Do you want to change doors?” While the contestant considers this option, the audience starts screaming out things like,

“Stay with your door! No, switch, switch!” Finally the contestant chooses again, and then Monty shows them what is behind their chosen door.

Let’s analyze this contest to see how to maximize the chance of winning. Define

$$p (i, j, y), \quad i, j, y = 1, 2, 3$$

to be the probability that you chose door i, the prize is behind door j and Monty showed you door y (named after the data!) after your initial guess. Then you would want to

$$\max _ {j} p (j | i, y)$$

for your optimal choice after Monty shows you a door.

(a) Calculate this conditional density and give the probability that the prize is behind door i, your original choice, and door $j \neq i$ .

(b) You will need to specify a model of Monty’s behavior. Please state the one that is appropriate to Let’s Make a Deal.

(c) For what other model of Monty’s behavior is the answer that it doesn’t matter if you switch doors. Why is this a poor model for the game show?
