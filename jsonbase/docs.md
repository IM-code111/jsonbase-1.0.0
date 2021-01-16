# **jsonbase docs**
## Table of content
- Creating database
- Get database data
    - Writing data
    - Save data to database
    - Swap data value with other data value
- Rename database
- Remove database

## Before started
We need to create our database variable
```py
import jsonbase

database = jsonbase.database('Database')
```
We can start now! 
****

## Creating database
To create a new database we use `create()`
```py
database.create()
```
Now we just create our database

Simple right?
****

## Get database data
Before we writing data in our database

we need to get the data in our database first
```py
data = database.get()
```
Now our data variable have all data in our database

but our database still empty
****

## Writing Data
To write data its actually simple

Let me explain why its actually simple

if you see inside JSON file is actually Python dictionary

then we can get all data inside JSON and put it in variable

after that we can add information into dictionary and save it to JSON file back

Understand?

if you still doesn't understand,dont't worry

I'm sure you will understand after you know how to write data in our database

Ok time to write data in our database

```py
data['Mark Car'] = 'BMW'
data['Dave Car'] = 'Audi'
```
yeah...

just do like that
****

## Save Data To Our Database
To save we can use `save()`
```py
database.save(data)
```
and then we done put our data into our database
****

## Swap Data Value with Other Data Value
Let's say that Dave and Mark swap they car

then we need to swap `Dave Car` and `Mark Car` data value

To do this we can use `swap()`
```py
database.swap('Mark Car', 'Dave Car')
```
Now we just swap two data value
****

## Rename Database
Ok so we name our database `database` right?

So we want rename our database to `Person_car` right?

then we need to click `database.json` then press `f2` and rename it

but how about we want rename in Python way?

We can use `os.rename()`

but how about we only want to use `jsonbase` module?

then we can use `database.rename()`
```py
database.rename('Person_car')
database = jsonbase.database('Person_car')#We need to update the variable or we can't use other jsonbase code
```
Done!
****

## Remove Database
To remove our database using `jsonbase` we use `remove()`
```py
database.remove()
```
Now our database just gone from existent
****

# The End Of Jsonbase Docs