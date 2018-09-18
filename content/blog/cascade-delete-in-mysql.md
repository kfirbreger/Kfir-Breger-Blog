Title:Cascade delete in MySQL
Date: 2008-04-25 20:03:00
Tags: programming, work

Now that I am actually getting payed to program instead of paying to program,
I find myself in greater need of practical information. Putting some of it on
my blog will help me keep all the knowledge in one place. To start off, I'll
mention Cascading delete in SQL. In the database schema there are 3 tables
used to store different objects. As there is a many to many relationship
between the the objects, there are relation tables.

![Basic database layout](/images/db-layout.png)

Using cascading delete I can define that if an object is removed from its
table, all relation tables entries with that object id are also removed. Quite
handy. the way this achieves is MySQL is through the use of foreign keys. If I
define in the table members the unique id of a user as a foreign key I can
also define tell the RDMS to delete the entries in members where that foreign
key exist. Here is an example of the definitions:

  

` CREATE TABLE members (

usr_id VARCHAR(30) NOT NULL,

grp_id VARCHAR(30) NOT NULL,

FOREIGN KEY usr_id REFERENCE user (usr_id) ON DELETE CASCADE,

FOREIGN KEY grp_id REFERENCE group (grp_id) ON DELETE CASCADE); `

  

As you can see the table is created normally by defining the fields, then the
foreign keys are named. The REFERENCE shows to which column in what table they
refer to.

