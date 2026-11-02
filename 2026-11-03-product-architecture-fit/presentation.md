---
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('./images/background.jpg')
footer: 
color: #000
breaks: off

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

.emphasis {
    font-weight: bold;
}

.deemphasis {
    color: gray;
}
</style>
<div class='title-page'>

# Cool
## Beans

</div>


---


# Neat
## Nifty

- lots
- of
- stuff


---

# Cool

 - <span class='emphasis'>First point</span>
 - <span class='deemphasis'>Second point</span>
 - <span class='deemphasis'>Third point</span>

---


# Cool Cats

- the first
- the second
- the third


---


# Eat My Shorts

- now
- later
- or never


---

# Cool

 - First point
 - <span class='emphasis'>Second point</span>
 - <span class='deemphasis'>Third point</span>

---

# Cool

 - First point
 - Second point
 - <span class='emphasis'>Third point</span>

---


# Closing Slide
## Final Remarks

- neat
