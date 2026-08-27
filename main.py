from bakery import assert_equal
from drafter import *
from dataclasses import dataclass



hide_debug_information()
set_website_title("Drafter Calculator")
set_website_framed(False)
set_website_style("xp")

@dataclass
class State:
    display: str  = "0"
    stored_value: int = 0
    operation: str = ""
    error: str = ""
    
@route
def index(state: State) -> Page:
    return Page(state, [
    TextBox("answer", state.display) if not state.error else TextBox("answer", state.error),
    "\n",
    Button(" 7 ", "seven"),
    Button(" 8 ", "eight"), 
    Button(" 9 ", "nine"),
    Button(" ÷ ", "divide"),
    "\n",
    Button(" 4 ", "four"),
    Button(" 5 ", "five"),
    Button(" 6 ", "six"),
    Button(" × ", "multiply"),
    "\n",
    Button(" 1 ", "one"),
    Button(" 2 ", "two"),
    Button(" 3 ", "three"),
    Button(" - ", "subtract"),
    "\n",
    Button(" 0 ", "zero"),
    Button(" C ", "clear"),
    Button(" = ", "equals"),
    Button(" + ", "add"),
])


@route
def zero(state: State) -> Page:
    if state.display == "0":
        state.display = "0"
    else:
        state.display += "0"
    return index(state)

@route
def one(state: State) -> Page:
    if state.display == "0":
        state.display = "1"
    else:
        state.display += "1"
    return index(state)

@route
def two(state: State) -> Page:
    if state.display == "0":
        state.display = "2"
    else:
        state.display += "2"
    return index(state)

@route
def three(state: State) -> Page:
    if state.display == "0":
        state.display = "3"
    else:
        state.display += "3"
    return index(state)

@route
def four(state: State) -> Page:
    if state.display == "0":
        state.display = "4"
    else:
        state.display += "4"
    return index(state)

@route
def five(state: State) -> Page:
    if state.display == "0":
        state.display = "5"
    else:
        state.display += "5"
    return index(state)

@route
def six(state: State) -> Page:
    if state.display == "0":
        state.display = "6"
    else:
        state.display += "6"
    return index(state)

@route
def seven(state: State) -> Page:
    if state.display == "0":
        state.display = "7"
    else:
        state.display += "7"
    return index(state)

@route
def eight(state: State) -> Page:
    if state.display == "0":
        state.display = "8"
    else:
        state.display += "8"
    return index(state)

@route
def nine(state: State) -> Page:
    if state.display == "0":
        state.display = "9"
    else:
        state.display += "9"
    return index(state)


@route
def add(state: State) -> Page:
    state.operation = "+"
    state.stored_value = int(state.display)
    state.display = "0"
    return index(state)

@route
def subtract(state: State) -> Page:
    state.operation = "-"
    state.stored_value = int(state.display)
    state.display = "0"
    return index(state)

@route
def multiply(state: State) -> Page:
    state.operation = "×"
    state.stored_value = int(state.display)
    state.display = "0"
    return index(state)

@route
def divide(state: State) -> Page:
    if state.display == "0":
        state.error = "Error"
    else:
        state.operation = "÷"
        state.stored_value = int(state.display)
        state.display = "0"
    return index(state)

@route
def equals(state: State) -> Page:
    if state.operation == "+":
        state.display = str(state.stored_value + int(state.display))
    elif state.operation == "-":
        state.display = str(state.stored_value - int(state.display))
    elif state.operation == "÷":
        state.display = str(f"{state.stored_value / int(state.display):.2f}")
    elif state.operation == "×":
        state.display = str(state.stored_value * int(state.display))
    else:
        state.error = "Error"
    state.stored_value = 0
    state.operation = ""
    return index(state)

@route
def clear(state: State) -> Page:
    state.display = "0"
    state.operation = ""
    state.error = ""
    return index(state)

start_server(State())
