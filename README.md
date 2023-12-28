**#GUI version of Rock Paper Scissors game**
Tkinter is used to make beautiful GUIs to make the game more appealing to play ( buttons are used to display available options for users, and results are displayed in a beautiful window).

The user is provided with buttons to enter their choice: Rock, Paper, or Scissors.

Under a  method named “choiceToNumber,” a dictionary was used to convert the user's choices to numbers:, “Rock” is converted to “1,” “Paper” is converted to “2” and “Scissors” is converted to 3. 

The computer's choice is generated randomly between 1 and 3.

A function called “result” was used to compare the user's choice and the computer's choice using numerical values.

Rules: Rock beats Scissors, Scissors beats paper, and Paper beats Rock.

 Condition (1) if the user’s choice is equal to the computer's choice, draw is printed.
 Condition (2) if (user’s choice - computer’s choice) % 3 = results in “1,” the user wins else the computer wins. 
 
User’s score or computer’s score is incremented depending on who wins.

(user’s choice - computer’s choice) % 3  helps to make the correct comparison between computer’s and user’s choice to determine the winner according to the rules without comparing strings, which can make the code unnecessarily long.

The result is printed to indicate whether the user wins, computer wins, or if it's a tie.

A video of the game: Watch Video
**Note**
 Author of project: Samuel Apoya.
