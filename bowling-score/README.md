Bowling Score Kata
------------------

# Description
The goal of this kata is to calculate the score of a bowling game based on a series of rolls.

# Rules of Bowling

## Game Structure:

* A bowling game consists of 10 frames.
* In each frame, the player has two opportunities to knock down 10 pins.
* The score for each frame is the total number of pins knocked down, plus bonuses for strikes and spares.

## Strikes:

* A strike occurs when the player knocks down all 10 pins with the first roll of a frame.
* The score for a strike is 10 plus the number of pins knocked down in the next two rolls.
* A strike is represented by an "X".

## Spares:

* A spare occurs when the player knocks down all 10 pins with the two rolls of a frame.
* The score for a spare is 10 plus the number of pins knocked down in the next roll.
* A spare is represented by a "/".

## Open Frames:

* An open frame occurs when the player does not knock down all 10 pins in the two rolls of a frame.
* The score for an open frame is the total number of pins knocked down in that frame.

## Tenth Frame:

* The tenth frame is special. If the player rolls a strike or a spare in the tenth frame, they get extra rolls to complete the frame.
* A strike in the tenth frame gives the player two additional rolls.
* A spare in the tenth frame gives the player one additional roll.

# Expected Output

The expected output of the Bowling Score Kata is the total score of the game after all frames have been played.

# Notation
|  |  |
|--|--------|
| `X` | strike |
| `/` | spare |
| `-` | miss |
| `number` | points |

# Example
Here is an example of a complete game and the expected output:

```
Rolls: X X X X X X X X X XXX
Score: 300
```

In this example, the player rolls 12 strikes in a row, resulting in a perfect game with a score of 300.

# Tests

Here are some test cases to help you verify your implementation:

## Test Case 1: All Strikes

```
Rolls: X X X X X X X X X XXX
Expected Score: 300
```

## Test Case 2: All Spares

```
Rolls: 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/ 5/5
Expected Score: 150
```

## Test Case 3: Mixed Rolls

```
Rolls: 9- 9- 9- 9- 9- 9- 9- 9- 9- 9-
Expected Score: 90
```

## Test Case 4: Random Rolls

```
Rolls: X 7/ 9- X -8 8/ -6 X X X81
Expected Score: 167
```
		
## Test Case 5: Tenth Frame Spare

```
Rolls: 9- 9- 9- 9- 9- 9- 9- 9- 9- 9/5
Expected Score: 95
```
		
## Test Case 6: Tenth Frame Strike

```
Rolls: 9- 9- 9- 9- 9- 9- 9- 9- 9- X53
Expected Score: 103
```
