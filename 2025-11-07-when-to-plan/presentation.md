---
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('./images/background-blur.jpg')
color: #000
footer: Speeding up and Slowing Down
breaks: 'off'
---

<style>
.row {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
}

</style>

# Speeding up and slowing down

## Heuristics for when to plan less and more

---

![bg](./images/straight-road-1.JPG)

---

![bg](./images/straight-road-2.JPG)

---

![bg](./images/straight-road-3.JPG)

---

![bg](./images/windy-road.jpg)

---

![bg](./images/elk-near-road.jpg)

---

![bg](./images/elk-near-road-zoomed-in.jpg)

---

![bg](./images/wet-road.jpg)

---

# Speed by default
# Slow for hazards

![bg right ](./images/straight-road-3.jpg)

---

# When to slow down?

![bg right ](./images/wet-road.jpg)

---

# Exercise
## Choose a platter and eat what's on it

<br/>
<br/>
<br/>

<div class="row">
<img width="400px" src="./images/platter.jpg"/>
<img width="400px" src="./images/platter.jpg"/>
<img width="400px" src="./images/platter.jpg"/>
</div>

---

# Algorithm 1: Look Inside

<br/>

<div class="row">
<img width="400px" src="./images/dirt.jpg"/>
<img width="400px" src="./images/dirt.jpg"/>
<img width="400px" src="./images/cake.jpg"/>
</div>

---

# Challenge
## What if it takes some effort to investigate each option?

<div class="row">
<img width="400px" src="./images/bead-door.jpg"/>
<img width="400px" src="./images/bead-door.jpg"/>
<img width="400px" src="./images/bead-door.jpg"/>
</div>

---

# Algorithm 2
### Explore Everything

- Easy to go through a bead door
- Explore until we find good food

![bg right 70%](./images/tall-bead-door.jpg)

---

# Challenge
## What if exploring one prevents exploring another?

![](./images/airport-security-doors-preview.jpg)

---

![bg](./images/airport-security-doors.jpg)

---

# Algorithm 3
### Research

- Smell when the doors open
- Ask a passerby to check for you
- Send one person of your group through

![bg right 70%](./images/one-airpot-security-door.jpg)

---

<br/>
<br/>
<div class="row">

<img width="200px" src="./images/tall-bead-door.jpg"/>

<ul>
<li>Algorithm 1: Look inside each
<li>Algorithm 2: Explore everything
<li>Algorithm 3: Research
</ul>

<img width="200px" src="./images/one-airpot-security-door.jpg"/>

</div>

---

## Explore everything

Works well when it's cheap to explore

![bg left 70%](./images/tall-bead-door.jpg)

---

## Research

Works well when exploring is expensive

![bg right 70%](./images/one-airpot-security-door.jpg)

---

## Bead Door Examples

- Choosing a library to transform data
- Class structure and naming
- UI layout

![bg left 70%](./images/tall-bead-door.jpg)

---

## One-way Door Examples

- Moving customer data into a new database
- Choosing a translation strategy and using it throughout the UI
- Setting a pattern and using it throughout the code

![bg right 70%](./images/one-airpot-security-door.jpg)

---

## The Planning Tradeoff

The higher the cost to explore, the bigger the budget for research

---

## Hack: make 1-way-doors 2-way

- Reduce the scope of the experiment
- Make it easy to reverse

---

## Examples: de-risking decisions

- Prove the database with sample data
- Prove the translation strategy with a small part of the UI
- Prove a pattern in a narrow scope

---

# Alex's suggestion

1. **Default to fast**: assume bead door
2. **Assess how reversible** is the decision you're about to make?
   -  And act accordingly

---

# Alex's suggestion
## When you identify a hard-to-reverse decision 

In this case, "try the first idea" won't make you faster

1. If possible, **reframe** the decision as a reversible bead door decision
2. Otherwise, take time to **plan and research** before acting

---

# Things to say in the mob

![bg](./images/straight-road-3.jpg)

---

# Things to say in the mob

- *probing*: "If we do X, can we change our mind?"
- *gas pedal*: "This looks reversible, can we **try something?**"
- *pump the breaks*: "This seems like a significant decision, **can we write a plan?**" (Consider writing an ADR.)
- *pump the breaks*: "Before we commit, could we run a **reversible experiment?**"
