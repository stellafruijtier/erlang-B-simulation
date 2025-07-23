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

<pre>
git clone https://github.com/stellafruijtier/erlang-B-simulation.git
cd erlang-B-simulation 
</pre>

2. Run the simulation

<pre> 
python3 mmcc.py 
</pre>

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



## 📈 Sample Output

<pre>
=== Part 1: Erlang-B Formula Calculations ===
For offered load E = 10.0:
  Servers needed for <10.0% blocking: 13 (actual blocking: 9.8071%)
  Servers needed for <1.0% blocking: 18 (actual blocking: 0.9846%)
  Servers needed for <0.1% blocking: 21 (actual blocking: 0.0969%)

=== Part 2: Simulation Verification ===

With 13 servers (target <10.0% blocking):
  Simulated blocking: 9.7420%
  Individual trial results: ['9.7000%', '9.7600%', '9.7500%', '9.7600%', '9.7400%']
  Erlang-B prediction: 9.8071%

With 18 servers (target <1.0% blocking):
  Simulated blocking: 0.9760%
  Individual trial results: ['0.9800%', '0.9700%', '0.9700%', '0.9800%', '0.9800%']
  Erlang-B prediction: 0.9846%

With 21 servers (target <0.1% blocking):
  Simulated blocking: 0.0900%
  Individual trial results: ['0.0900%', '0.1000%', '0.0900%', '0.0900%', '0.0900%']
  Erlang-B prediction: 0.0969%

=== Part 3: Erlang-2 Service Times ===

Finding servers needed for <1% blocking with Erlang-2 service times...
Servers needed for <1% blocking with Erlang-2 service: 19
  (Compared to 18 servers for exponential service times)
</pre>


## 📦 Project Structure

- `mmcc.py` : Main simulation scirpt - M/M/c/c and Erlang-2 service model
- `READ.md` : Project overview and usage instructions


## 🧪 Key Concepts Reinforced

- Discrete-event simulation and event-driven logic
- Poisson arrvials and exponential/Erlang service distribution
- Blocking systems with no queue
- Comparison of empirical vs. theoretical performance metrics
- Binary search to find capacity targets


## 📖 Acknowledgments

This project was inspired by assignments and materials from Dan Myers, whose examples and explanations in simulation modeling helped guide this work for the **Simulation & Stochastic Modeling** class at Rollins College.
