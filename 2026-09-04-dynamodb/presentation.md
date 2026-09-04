---
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('./images/background.jpg')
footer: 
color: #000
breaks: 'off'
---
<style>
:root {
  font-family: 'Baskerville', serif;
}
.space-above {
    margin-top: 24px;
}

.row {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
}

.row > * {
    margin-top: auto;
    margin-bottom: auto;
}

.title-page {
    font-size: 2em;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    height: 50%;
    margin-bottom: 300px;
}
.picture-frame {
    border: 2px solid black;
    border-radius: 4px;
}

.columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
}

h1 + h2 {
    font-weight: normal;
    font-style: italic;
    font-size: 22pt;
}

.title-page h1 + h2 {
    font-size: 0.8em;
}

</style>

<div class="title-page">
<h1>Dynamo DB</h1>
<h2>The Right Write &amp;<br> In The Weeds With The Reads</h2>
</div>

---

# Dynamo DB
## The Right Write & In The Weeds With The Reads

1. PutItem vs UpdateItem
2. TransactWriteItems
3. GetItem vs BatchGetItem
4. Query vs Scan
5. DDB Philosophy

---

# PutItem vs UpdateItem

- **PutItem** replaces all the attributes
- **UpdateItem** changes individual attributes
 
---

<div class="columns">
<div>

# PutItem
- Create or Replace
- Terser syntax: save a dictionary

</div>
<div>

# UpdateItem
- Create or Update
- Verbose syntax: write an update expression for each field
- Supports update operations like
  - add/subtract from number
  - add value to a set
  - remove value from a set

</div>
</div>

---

# Dynamo DB
## The Right Write & In The Weeds With The Reads

1. ✅ PutItem vs UpdateItem: *PUT replaces, UPDATE merges*
2. TransactWriteItems
3. GetItem vs BatchGetItem
4. Query vs Scan
5. DDB Philosophy

---

# TransactWriteItems

- Do a set of operations all at once
- Supported operations:
  - Put
  - Update
  - Delete
  - ConditionCheck

---

## TransactWriteItems: ConditionCheck
- Express an assumption about an item
  - an item that you're not changing
- E.g.
  - "this item must exists"
  - "this item must have an attribute with a value above 42"

---

## TransactWriteItems: Why???
### Permission Check
- "write X, only if the user has a permission record Y"
- this is faster than doing a read followed by a write
 
---

## TransactWriteItems: Why???
### Race-condition protection
- "read X, write Y"
  - what if X has been changed after the read?
- a ConditionCheck protects us
- "only write Y if X looks like it did when I read it"

---

## Aside: UpdateItem ConditionExpression

- You can also use condition expressions with UpdateItem
- This expresses an assumption about the item you're changing
- Whereas TransactWriteItem ConditionExpression is about an item you're not changing

---

# Dynamo DB
## The Right Write & In The Weeds With The Reads

1. ✅ PutItem vs UpdateItem: *PUT replaces, UPDATE merges*
2. ✅ TransactWriteItems: *Make several changes at once*
3. GetItem vs BatchGetItem
4. Query vs Scan
5. DDB Philosophy

---

# GetItem vs BatchGetItem

- ddb reads are very fast
- the slowest part is the network hop to ddb and back
- multiple reads == more network hops

---

# BatchGetItem

- read up to 100 items (up to 16MB)
- can read from multiple tables at once
- provide the table name and keys
- one network hop, many reads

---

# Dynamo DB
## The Right Write & In The Weeds With The Reads

1. ✅ PutItem vs UpdateItem: *PUT replaces, UPDATE merges*
2. ✅ TransactWriteItems: *Make several changes at once*
3. ✅ GetItem vs BatchGetItem: *We can read multiple items at once*
4. Query vs Scan
5. DDB Philosophy

---

# Query vs Scan

- Scan is slow
- In my 5 years using ddb, I've never seen a good use in prod for Scan
- If you're using Scan, your indexes are probably not right

---

# Why is it called a "sort key"?

Because the data is physically arranged on disk in the sort order so lookup is efficient

---

# Why can't we suffix match with SKs?

With a prefix match, ddb can do a binary search to efficiently find your results

A suffix match requires a scan.

---

<div class="columns">
<div>

### Query
- Use sort key with a prefix match
- Fast binary search on disk to read your items

</div>
<div>

### Scan + FilterExpression
- Slow and resource intensive
- Ddb has to look at all the items
- Filter expression is evaluated after reading the data from disk

</div>
</div>

---

<div class="columns">
<div>

### Query
- Response time is a function of how many items you're reading

</div>
<div>

### Scan + FilterExpression
- Response time is a function of the number of items in the partition

</div>
</div>

---

# Dynamo DB
## The Right Write & In The Weeds With The Reads

1. ✅ PutItem vs UpdateItem: *PUT replaces, UPDATE merges*
2. ✅ TransactWriteItems: *Make several changes at once*
3. ✅ GetItem vs BatchGetItem: *We can read multiple items at once*
4. ✅ Query vs Scan: *Design your indices so you can use Query*
5. DDB Philosophy

---

## Bonus Thought: DynamoDB Philosophy

- ddb doesn't let you do things that are slow
- if you're thinking "why can't I just ____?"
  - probably because ddb can't do it fast

---

## DynamoDB Philosophy
### Denormalized Data

- Denormalized data is read-optimized
- You do more work when you write
  - Redundant writes with `TransactWriteItems`
- You do less work when you read
  - Constant-time item reads with `GetItem` and `BatchGetItem`
  - Linear-time item lists with `Query`

---

# Dynamo DB
## The Right Write & In The Weeds With The Reads

1. ✅ PutItem vs UpdateItem: *PUT replaces, UPDATE merges*
2. ✅ TransactWriteItems: *Make several changes at once*
3. ✅ GetItem vs BatchGetItem: *We can read multiple items at once*
4. ✅ Query vs Scan: *Design your indices so you can use Query*
5. ✅ DDB Philosophy: *Denormalized == read-optimized*

