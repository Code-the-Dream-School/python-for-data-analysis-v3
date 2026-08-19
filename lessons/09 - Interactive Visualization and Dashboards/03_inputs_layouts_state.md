# 9.3 Inputs, Layout, and State

**Objective**: By the end of this module, you will be able to:

* Collect user input with Streamlit widgets.
* Arrange content with columns, expanders, and a sidebar.
* Filter a DataFrame from widget values.
* Explain why buttons in Streamlit are "stateless."

---

An app that only displays content is a web page. Adding **widgets** — controls the user can change — is what makes it interactive. The key skill in this module is using a widget's value to filter a DataFrame, which is what turns a page into a dashboard.

## Input Widgets

Each widget function draws a control and **returns its current value**. You store that value in a variable and use it like any other:

```python
import streamlit as st

name = st.text_input("Your name", "Amara")            # returns the entered text
age = st.number_input("Age", min_value=0, max_value=120, value=25)  # returns the number
score = st.slider("Score", 0, 100, 50)                # returns the slider value
option = st.selectbox("Choose one", ["A", "B", "C"])  # returns the selected option
choices = st.multiselect("Choose several", ["X", "Y", "Z"])  # returns a list
show_details = st.checkbox("Show details")            # returns True or False
```

Because the script reruns on every interaction (Module 9.2), each variable simply holds whatever the widget currently shows.

## Buttons Are Stateless

A button is different from the other widgets. `st.button` returns `True` only on the single rerun that happens right after it is clicked, and `False` on every other run. It does not "stay pressed." You use it with an `if`:

```python
if st.button("Run"):
    st.write("The button was clicked.")
```

This follows directly from the rerun model: the button reports "was I just clicked on this run?" rather than holding a lasting state.

---

## Layout: Columns, Expanders, and the Sidebar

By default, content stacks top to bottom in the order of your code. Three tools arrange it.

**Columns** place content side by side. `st.columns(2)` returns two column objects, and you add content to each with a `with` block:

```python
col1, col2 = st.columns(2)

with col1:
    st.header("Left")
    st.write("Content in the left column")

with col2:
    st.header("Right")
    st.write("Content in the right column")
```

**Expanders** hide content until the user clicks to open them:

```python
with st.expander("Show more"):
    st.write("This is hidden until expanded.")
```

**The sidebar** is a panel on the left, good for filters. Put a widget in it with `st.sidebar`:

```python
region = st.sidebar.selectbox("Region", ["East", "West"])
```

---

## Filtering a DataFrame from a Widget

This is where it becomes a dashboard. Use a widget's value to select rows of a DataFrame, then display the result:

```python
import pandas as pd

df = pd.DataFrame({
    "Product": ["A", "B", "C", "D"],
    "Sales": [120, 340, 210, 150],
})

product = st.selectbox("Choose a product", df["Product"].unique())
filtered = df[df["Product"] == product]

st.dataframe(filtered)
```

Trace what happens when the user picks a different product: the script reruns, `product` receives the new selection, `filtered` is recomputed for that product, and `st.dataframe` displays the new rows. You did not write any update logic — the rerun model does it. A widget value driving a filter, recomputed on every rerun, is the core pattern of every Streamlit dashboard.

---

### AI Prompt: Predict-then-Check

Buttons behave differently from other widgets because of the rerun model. Study this without running it:

```python
import streamlit as st

st.title("Counter App")
if st.button("Click to add 1"):
    st.write("You clicked the button!")
st.write("Current status: waiting...")
```

1. Predict what happens to the "You clicked the button!" message after you click the button and then interact with something else (or refresh).
2. Explain to an AI chatbot why that message stays or disappears, based on how Streamlit reruns the script and how a button reports its state.
3. Ask: "Is my understanding of Streamlit's stateless buttons and rerunning correct?"

> **Example prompt:** "Looking at this Streamlit code: [paste code]. I predict that after I click the button and then interact again, the 'You clicked the button!' text will [stay/disappear] because [your reasoning about rerunning and stateless buttons]. Am I correct?"

---

## Check for Understanding

**1. What does a widget function like `st.slider(...)` return?**

* A) Nothing
* B) The current value of the control
* C) The whole app
* D) A True/False for whether it changed

<details>
<summary>Answer</summary>

B) A widget returns its current value, which you store in a variable and use in the rest of the script.

</details>

**2. Why do you use `st.button` inside an `if` statement?**

* A) Because buttons cannot be used otherwise
* B) Because a button returns `True` only on the rerun right after it is clicked, and `False` otherwise
* C) Because it is faster
* D) Because buttons must be in the sidebar

<details>
<summary>Answer</summary>

B) A button reports whether it was just clicked on this run, so you check it with `if`. It does not hold a pressed state between reruns.

</details>

**3. A user changes a `selectbox` that a DataFrame filter depends on. What updates the displayed table?**

* A) You must write code to refresh the table
* B) The whole script reruns, the filter recomputes with the new value, and the table is redisplayed
* C) Only the selectbox changes
* D) Nothing updates until you restart the app

<details>
<summary>Answer</summary>

B) The rerun recomputes the filter and redisplays the table automatically — no manual update code is needed.

</details>

---

## Further Reading

* [Streamlit: Input widgets](https://docs.streamlit.io/develop/api-reference/widgets)
* [Streamlit: Layouts and containers](https://docs.streamlit.io/develop/api-reference/layout)
