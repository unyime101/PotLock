# 💰 PotLock: Automated Finances Management System

**PotLock** is a personal finance management system built to **automate and simplify savings**. It allows users to manage an active balance while creating "pots" — locked savings targets — that fill automatically based on user-defined rules.

This idea originated from my own need for better savings management while receiving regular income. I’m developing it with the intention to help myself and others build healthier saving habits.

---

## 🚀 Technologies Used

- 🐍 Python  
- 🛢️ MySQL  

---

## 🎯 Key Features

- ✅ User registration and login  
- ✅ View active balance and deposit into account  
- ✅ Withdraw from account  
- ✅ Create and manage savings “Pots”  
- ✅ Track progress toward saving goals  
- ✅ View all pots (active and live)  
- ✅ Edit user details  
- 🔒 Pots are locked until:
  - A **target amount** is reached **or**  
  - A specified **end date** passes

---

### 💡 How Pots Work

Each pot has a **weighting** – a percentage of every deposit that will be redirected into it.

Example:
> User deposits £50  
> A pot has a weighting of 10%  
> £5 goes into the pot  
> £45 remains in the active balance  

When a pot becomes **full**, it is marked as “live” — signaling that the user can now make the intended purchase (house, car, etc.).

> Once a pot becomes live, its previous weighting is redistributed to the remaining pots to speed up their growth.

---

## 📌 Current Progress

| Feature                     | Status        | Notes                                                                 |
|-----------------------------|---------------|-----------------------------------------------------------------------|
| User Authentication         | ✅ Completed   | Login and signup fully implemented                                   |
| Account Overview            | ✅ Completed   | Deposit flow and balance display working                            |
| Pot Creation                | ✅ Completed   | Pot creation implemented                                              |
| Pot Verification            | ✅ Completed   | Pot constraints and full pot logic added                             |
| Pot Deposit Logic           | ✅ Completed   | Deposits now respect pot weightings                                  |
| Pot Redistribution Logic    | 🚧 In Progress | Working on redistributing weights once pots become “live”            |

---

## 🔄 Development Note

I have become **very comfortable using Python and MySQL**, and I’ve learned a lot through this project. For now, I will be **taking a break from PotLock** to focus on **further strengthening my Python knowledge** through new projects and challenges.

I fully intend to **return to PotLock** later with fresh ideas and better tooling — especially in areas like deployment and scalability.

---

## 🌱 Potential Future Enhancements

- 🖼️ Create a better UI/UX interface  
- ☸️ Deploy the backend using Kubernetes  
- 🐳 Containerize with Docker  
- 📈 Add financial reports/analytics views  
- 🧠 Incorporate budgeting and forecasting logic  

---

## 👨‍💻 About the Developer

I'm a final-year **Computer Science student** aspiring to become a **Site Reliability Engineer (SRE)** and DevOps professional. I'm passionate about building meaningful tools, learning by doing, and improving systems with smart automation.
