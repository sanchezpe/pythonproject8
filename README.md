# Programming Assignment #8

## Description
Process bank account data, using a class/objects

## Instructions
1. Write a class definition for a bank account object. The initializer/constructor is provided. You must write a get method for each data member, as well as a set method for each data member. One of each is provided. Finally, you must write a method to withdraw money from a bank account and a method to deposit money into a bank account.

2. Now that you have a class Account, write the main to access/use the class. First create two(2) bank account objects. The account numbers will be ABC123 and DEF456, and they will both be opened with balances of $1000. The code to do this is below:
 
	acct1 = Account("ABC123", 1000)
	acct2 = Account("DEF456", 1000)

	Next, read from a file of unknown length, i.e., use a sentinel-controlled while loop. The data in the file will be bank account transactions. Each transaction will consist of 3 lines (set) of data:
	- bank account id number (which can contain letters and numbers)
	- transaction type (either a D or W, uppercase)
	- transaction amount

	Read the data a “set” at a time. Stop reading when you reach a bank account id number of “ZZZ999”
	Name the data file: pa8.trans
	As you read the data, determine which object should be affected (match the id from the file with the id in the object – use the GetId method). Then apply either the Deposit method or the Withdrawal method to that object.
	Also, as you read the data, print a “neat and tidy” table of the transactions/results (see sample run).

## Sample Run
	Account Transaction Amount Balance
	---------------------------------------------------------
	ABC123 Deposit 1250.00 2250.00
	DEF456 Withdrawal 80.00 920.00
	ABC123 Withdrawal 20.00 2230.00
	DEF456 Deposit 780.00 1700.00
	ABC123 Withdrawal 5000.00 2230.00 <denied>