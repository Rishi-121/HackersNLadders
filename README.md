# HackersNLadders

### Hack the Snake and Climb the Ladder

<br/>

[![HackersNLadders | Snake and Hackers Submission](http://img.youtube.com/vi/CDHZYz8FfaM/0.jpg)](http://www.youtube.com/watch?v=CDHZYz8FfaM "HackersNLadders | Snake and Hackers Submission")

<br/>

## Get Started

~~~
$ git clone https://github.com/UltimateRoman/HackersNLadders
$ cd HackersNLadders/game
$ pip install -r requirements.txt
$ python main.py
~~~


## Inspiration

Well all of us must have played Snakes and Ladders at least once in our lives. We decided to recreate it by building an enhanced and more engaging version of this ever-popular board game.

## What it does

Our project takes the idea of the ever-popular board game - Snakes and Ladders and tries to make an aesthetic design of the game using Python GUI. We also built an Arduino-based module as the game-controller, interfaced with the computer through Serial port, and which can serial communicate with the game.

The user can use the push-button on the module to simulate a dice roll which generates a value in the range 1 to 6. This is then sent over to the game with the help of the pyserial library. And the corresponding move played by the user is updated in the game. If the user’s token lands on a snake, the LED on the controller module blinks, or if it lands on a ladder, the buzzer rings to indicate the same.

## How we built it

1. We used the pygame module to build the Snakes and Ladders game - the graphics and the user interface and the working of the dice and the tokens.
2. We made use of an Arduino to build the game-controller module. The LED and Buzzer indicators of Arduino are used to show if the tokens land on a ladder or a snake, which makes the game more engaging for the user.


## Challenges we ran into

1. This was the first hackathon for most of our team members, so lack of familiarity was a major challenge. 
2. We didn’t have much prior experience with Python GUI programming, but we learned it over the weekend and were able to implement it just as we had intended to do.
3. Another challenge was to connect Arduino to the GUI implementation, which was something we never have done before. We had to spend a considerable amount of time in trying to bring about effective communication between the Arduino module and the game. But finally, we were able to optimize it after some trials.

We had also wanted to show animated transitions in the project, but due to lack of time, we were unable to do much about it. Although we did try our very best.


## Accomplishments that we're proud of

1. We take immense pride in having been able to complete and submit the project as a beginner at the hackathon.
2. Building the Python GUI implementation of the board game using the pygame module.
3. Interfacing the Arduino module and the game, which required significant effort from our side.

## What we learned

Since this was our first hackathon, it had been a great learning experience for all of us.

1. We learned to use the pygame module to build the Snakes and Ladders game.
2. We learned about Arduino programming and how to control the pushbutton, LED, and buzzer using the sketch.
3. We also learned about Serial Communication and how to interface the Arduino with the game using the pyserial library.


## What's next for HackersNLadders

We hope to expand the idea of the game in the following ways-

1. Make it online, use Web Sockets so players around the world can play with anyone online.
2. Maintain a leader board and a rating system having a centralized database to store points.
3. Improve upon the UI of the game's GUI.

## Inspiration

Well all of us must have played Snakes and Ladders at least once in our lives. We decided to recreate it by building an enhanced and more engaging version of this ever-popular board game.

## What it does

Our project takes the idea of the ever-popular board game - Snakes and Ladders and tries to make an aesthetic design of the game using Python GUI. We also built an Arduino-based module as the game-controller, interfaced with the computer through Serial port, and which can serial communicate with the game.

The user can use the push-button on the module to simulate a dice roll which generates a value in the range 1 to 6. This is then sent over to the game with the help of the pyserial library. And the corresponding move played by the user is updated in the game. If the user’s token lands on a snake, the LED on the controller module blinks, or if it lands on a ladder, the buzzer rings to indicate the same.

## How we built it

1. We used the pygame module to build the Snakes and Ladders game - the graphics and the user interface and the working of the dice and the tokens.
2. We made use of an Arduino to build the game-controller module. The LED and Buzzer indicators of Arduino are used to show if the tokens land on a ladder or a snake, which makes the game more engaging for the user.


## Challenges we ran into

1. This was the first hackathon for most of our team members, so lack of familiarity was a major challenge. 
2. We didn’t have much prior experience with Python GUI programming, but we learned it over the weekend and were able to implement it just as we had intended to do.
3. Another challenge was to connect Arduino to the GUI implementation, which was something we never have done before. We had to spend a considerable amount of time in trying to bring about effective communication between the Arduino module and the game. But finally, we were able to optimize it after some trials.

We had also wanted to show animated transitions in the project, but due to lack of time, we were unable to do much about it. Although we did try our very best.


## Accomplishments that we're proud of

1. We take immense pride in having been able to complete and submit the project as a beginner at the hackathon.
2. Building the Python GUI implementation of the board game using the pygame module.
3. Interfacing the Arduino module and the game, which required significant effort from our side.

## What we learned

Since this was our first hackathon, it had been a great learning experience for all of us.

1. We learned to use the pygame module to build the Snakes and Ladders game.
2. We learned about Arduino programming and how to control the pushbutton, LED, and buzzer using the sketch.
3. We also learned about Serial Communication and how to interface the Arduino with the game using the pyserial library.


## What's next for HackersNLadders

We hope to expand the idea of the game in the following ways-

1. Make it online, use Web Sockets so players around the world can play with anyone online.
2. Maintain a leader board and a rating system having a centralized database to store points.
3. Improve upon the UI of the game's GUI.

