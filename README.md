# erlang-B-simulation

This project simulates an **Erlang B** system (also known as an **M/M/c/c queue**) using Python. It models a system with c servers, exponential interarrival and service times, and **no queue**, meaning that jobs are **blocked and lost** when all servers are busy

The simulation estimates the **blocking probability** under various arrival and service rates and compares it to the **theoretical** Erlang B formula, and optionally uses **Erlang-2 distributed service times** for added realism.

Developed as part of **Simulation & Stochastic Modeling** coursework at **Rollins College**


## 📚 What is an Erlang B system?

In the Erlang B (or M/M/c/c) model:
- **M (Markovian arrivals):** Interarrival times follow an exponential distribution
- **M (Markovian service):** Service times are also exponential
- **c servers:** There are c identical servers
- **No queue:** If alls ervers are busy, incoming jobs are blocked and immediately lost
- **Used in:** Telephony, call centers, network design, healthcare systems, and more


## 🧠 What this simulation does

- Simulates arrivals and service completions in an M/M/c/c system
- Tracks whether each arriving job is accepted or blocked
- Computes: blocking probability, server utilization, number of jobs accepted vs. blocked
- Compares with theoretical **Erlang B formula**
- Optionally simulates **Erlang-2 service times** using a subclass
- Includes a tool to find the **minimum number of servers** needed to achieve a given blocking threshold


## ⚙️ Requirements

- Python 3.7 or higher
- No external libraries needed (uses only standard Python modules)


## 🛠️ How to run the simulation

1. Clone the repository


<pre> git clone https://github.com/stellafruijtier/erlang-B-simulation.git
cd erlang-B-simulation </pre>

2. Run the simulation

<pre> python3 mmcc.py </pre>

This will automatically:
- Calculate required servers for target blocking thresholds using the **Erlang B formula**
- Run discrete-event simulations with **exponential service times**
- Run the same simulations using **Erlang-2 service times**
- Compare **theoretical vs. simulated blocking probabilities**
- Print all results to the console


## 🧩 Available Parameters

| Parameter   | Description                                | Default |
|------------|--------------------------------------------|---------|
| `--lambda`  | Arrival rate (calls/jobs per unit time)    | 6.0     |
| `--mu`      | Service rate (jobs served per server)      | 1.0     |
| `--servers` | Number of available servers (`c`)          | 5       |
| `--time`    | Total simulation time (virtual time units) | 100000  |
| `--seed`    | Random seed for reproducibility            | None    |




