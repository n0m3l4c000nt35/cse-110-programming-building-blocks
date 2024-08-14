1. [amusement_park_rides.py](./amusement_park_rides.py)
2. [qualifying_for_a_loan.py](./qualifying_for_a_loan.py)

## [amusement_park_rides.py](./amusement_park_rides.py)

### Overview

For this assignment, you'll work as a team to write a program for a fictitious amusement park ride.

### THE SCENARIO: RIDER REQUIREMENTS

The local amusement park has just installed a new ride. Because of its speed and extreme twists and turns, it has very strict requirements for the riders, especially as it pertains to children or other shorter riders.

To help the ride attendants follow the rules, you've been asked to write an app to help them know if the riders are acceptable for the car.

The basic rules are as follows:

No one under 36 inches may ever ride, either by themselves or with another rider.

Normally, two riders sit in the car together. A single rider can only ride if they are at least 18 years old and are at least 62 inches tall.

If there are two riders and one of them is at least 18 years old, they may ride together.

### Assignment

Implement the ride requirements defined above. Your program should prompt for the riders' ages and heights, and then display a message indicating whether they can ride or not.

### CORE REQUIREMENTS

Prompt the user for the age and height of the first person. Then, ask whether there is a second rider, and if so, ask for their age and height.

Handle the case of a single rider.

Finish implementing the basic rules.

An example run of the program may look as follows:

```
What is the age of the first rider? 12
What is the height of the first rider? 46
Is there a second rider (yes/no)? no
Sorry, you may not ride.
```

Another example may look as follows:

```
What is the age of the first rider? 82
What is the height of the first rider? 75
Is there a second rider (yes/no)? yes
What is the age of the second rider? 14
What is the height of the second rider? 35
Sorry, you may not ride.
```

And a final example:

```
What is the age of the first rider? 82
What is the height of the first rider? 75
Is there a second rider (yes/no)? yes
What is the age of the second rider? 14
What is the height of the second rider? 36
Welcome to the ride. Please be safe and have fun!
```

### STRETCH CHALLENGE

In addition to the basic rules, the amusement park has added the following. Please implement each one for the stretch challenges:

If there are two riders, but neither one is at least 18 years old, they may still ride as long as they are both at least 12 years old and at least 52 inches tall.

If a person is age 12–17, ask if that person has a golden passport. If they do, they should be treated as if they were 18 years old for the sake of all rules. (Don't forget to apply this to the single rider case.)

If there are two riders, but neither one is at least 18 years old, they may still ride if one rider is at least 16 years old and the other is at least 14. (Keep in mind that the first rider may be the younger of the two or they may be the older of the two.)

Whew! That's complicated! Now you see why they need an app.

## [qualifying_for_a_loan.py](./qualifying_for_a_loan.py)

### Overview

For this assignment, you will implement a simplistic system to determine if a user can qualify for a loan.

### The Problem: Qualifying for a loan

When loaning money to someone, you want to have some level of confidence that they will be able to repay the loan.

There are different characteristics you might base this decision on, or different questions you might ask someone. And depending on their answers to those questions, you might ask other questions. For example, consider the following possible questions:

Does the person have a job, and if so, how long have they worked there, and how much money do they make?

Is there good collateral for the loan? (for example, is the loan against a car or home that is worth at least the amount of the loan?)

Does the person have a good credit score or history of paying back loans?

How much other debt does the person have?

How much money does the person have?

Will the person have a down payment, and if so, what percentage of the loan does it amount to?

### Assignment

Write a program to determine whether to loan money based on the following rules.

First, ask for a rating from 1–10 on the following:

How large is the loan?

How good is your credit history?

How high is your income?

How large is your down payment?

Then, you will create a boolean variable for whether you should loan the money that will be set to either True or False. Set up a series of if statements to decide if your decision to loan is "yes" or "no" according to the following rules:

First, check if the loan size is at least 5. If it is, use the following rules:

If the credit history and income are both at least 7, then the decision is "yes"

If either the credit history or income is at least 7, then check if the down payment is at least 5, if it is, the decision is "yes", if not, the decision is "no"

Otherwise (if neither the credit history nor income is at least 7), the decision is "no"

Otherwise (if the loan is not 5 or greater), use these rules:

If the credit is less than 4, then the decision is "no"

Otherwise, check the following:

If either the income or the down payment is at least 7, the decision is "yes"

If both the income and the down payment are at least 4, then the answer is "yes"

Otherwise, the decision is "no"

Finally, display the decision to the user.

Testing Procedure
Verify that your program works correctly by following each step in this testing procedure:

Test your program with these values and ensure you arrive at the decision indicated:

Loan size: 8, Credit: 7, Income: 8, Down Payment: 1, Decision: "yes"

Loan size: 5, Credit: 2, Income: 7, Down Payment: 5, Decision: "yes"

Loan size: 8, Credit: 2, Income: 8, Down Payment: 3, Decision: "no"

Loan size: 2, Credit: 4, Income: 1, Down Payment: 7, Decision: "yes"

Loan size: 4, Credit: 5, Income: 5, Down Payment: 3, Decision: "no"
