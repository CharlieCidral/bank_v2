# bank_v2
Learning functions in python with Dio, but with some increments.

### SIGN PAGE

![image](https://github.com/CharlieCidral/bank_v2/assets/69029099/ffd51162-1e48-4c56-9eb2-1090efbf896d)


### MENU

![image](https://github.com/CharlieCidral/bank_v2/assets/69029099/9204dbc1-6360-4555-bd4d-ee876d434c3f)



### Proposed challenge

Separate existing withdrawal, deposit, and withdrawal functions into functions. Create two new functions: register user (customer) and register bank account.

### Challenge

We need to make our code more modularized, for that we are going to create functions for the existing operations: withdraw, deposit and view history. Furthermore, for version 2 of our system we need to create two new functions: create user (bank customer) and create current account (link with user).

### Separation into Functions

We must create roles for all system operations. To control everything that is controlled in this module, each function will have a rule when passing arguments. O
return and the way they will be called, can be defined by you in the way you see fit. (Exercise the arguments by position and named arguments)

### Withdraw

The looting function must receive the arguments only by name (keyword only). Suggested arguments: balance, value, statement, limit, number of withdrawals, limit_withdrawals. Return suggestion: balance and statement.

### Deposit

The function must receive arguments by position only (positional only). Suggested arguments: balance, value, statement. Return suggestion: balance and statement.

### Extract

The extra function must take arguments by position and name (positional only and keyword only). Positional arguments: balance, named arguments: extract.

### New functions

we need to create two new functions: create user and create checking account. Feel free to add more functions, for example: list accounts.

### Create User (Customer)

The program must store users in a list, a user is composed of: name, date of birth, CPF and address. The address is a string with the format: street, neighborhood number - city/state abbreviation. Only the CPF numbers should be stored. We cannot register 2 users with the same CPF. (Data structure to store key/value)

### Create checking account

The program must store accounts in a list, an account is composed of: agency, account number and user. The account number is sequential, starting at 1. The branch number is fixed: "0001". A user can have more than one account, but an account belongs to only one user.

### Tip

To link a user to an account, filter a list of users by searching for the CPF number entered for each user in the list.

