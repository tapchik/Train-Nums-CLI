# Train Nums

**Train Nums** is a program that generates math problems for user, accepts answers and stores statistics.

User communicates with program through input. You can enter answer to math problem when prompted or **commands**:

- "skip" - skip difficult problems;
- "settings" - change max sum;
- "status" - show settings and your statistics;
- "delete progress" - clear your statistics and start fresh;
- "turn on/off addition";
- "turn on/off subtraction";
- "help" - show this list of commands again;
- "exit" - quit Train Nums.

**Settings** include data about math problems generation, which prevents user from having to manually apply preferred generation settings every time.

**Statistics￼** include 3 data points:

- number of solved math problems
- number of incorrect answers
- number of skipped math problems

Settings and statistics are locally stored in **TrNuSettings.json** file. Program doesn’t keep any other information about user.

> Note: It is important to enter ‘exit’ command because it automatically saves user settings and statistics. Quitting program in any other way will lead to losing progress. 
