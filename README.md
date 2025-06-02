 Online Bus Booking System (my first big project)
------



<h1 align="center">🚌 Online Bus Booking System — My Diwali Code Saga ✨🚌</h1>
 <img src="https://cdn.dribbble.com/userupload/24649847/file/original-0660a8b2abd28d54531190326b3e0841.gif" width="960" alt="Anime" />
<p align="center">
  " During my Diwali holidays ✨, I took on my first-ever large-scale boss-level project for my 3rd semester — an online bus ticket booking system! Packed with interactive GUI battles, visually appealing moves, and real-world logic techniques like fare calculation jutsu, seat assignment strategies, and travel schedule summoning — it was my own little software saga!"
</p>

-------
🧩 What’s Inside the System?

Prepare yourself—this app isn’t just about buses. It’s packed with real-world logic, visual flair, and interactive modules that bring the whole ticket-booking experience to life.

 🎯 Core Features

 👥 Passenger can : 
- 🔍 Search for buses by route and journey date
- 🪑 Book seats and get instant fare details
- 📱 Retrieve booking using mobile number

 
 🔐 Admin can : 
- ➕ Add new bus operators, buses, and routes
- 📅 Schedule buses to run on specific dates
- 🗃️ SQLite database with live updates
- 🖼️ User-friendly GUI for all operations

--------------------------------------------

⚙️ Tech Stack / Weaponry Used

| Element         | Description                                               |
| --------------- | --------------------------------------------------------- |
| 🐍 Python       | The heart of the beast (3.x)                              |
| 🪟 Tkinter      | GUI engine that powers all the interaction                |
| 🗃️ SQLite       | Local database storing buses, operators, routes, bookings |
| 🧙‍♀️ OOP          | Code organized into a modular class structure             |
| 🖼️ PNG Sprites  | Used for interface banners and navigation icons           |

-----
🧱 Database Schema (Summary)

| Table             | Description                        | Key Columns                                                  |
| ----------------- | ---------------------------------- | ------------------------------------------------------------ |
| `operator`        | Bus operator info                  | `opr_id (PK)`, `name`, `phone`, `email`                      |
| `bus`             | Details of buses                   | `bus_id (PK)`, `type`, `fare`, `op_id (FK)`, `route_id (FK)` |
| `route`           | Route and station mapping          | `r_id (PK)`, `s_name`, `s_id`                                |
| `running`         | Bus availability on specific dates | `b_id (FK)`, `run_date`, `seat_avail`                        |
| `booking_history` | Passenger ticket bookings          | `booking_ref (PK)`, `name`, `phone`, `bid (FK)`              |

🔐 Foreign keys ensure relational integrity across bus, operator, route, and booking_history.

-------------------------------------------------------------------------------------------------------------------------------------------------------
## 📂 Project Structure

OnlineBusBookingSystem/

├── online_bus_booking.py # Main Python application

├── online_bus_booking.db # SQLite DB (auto-created)

├── starbus.png # Banner image for GUI

├── home.png # Home icon for navigation

└── README.md # This file

----


🛡️ How To Run

bash```
     
     python your_filename.py
``
Make sure to keep starbus.png and home.png in the same directory! They power the visuals.

----

📅 Input Format Guidelines
| Field        | Format           |
| ------------ | ---------------- |
| Phone Number | 10-digit numeric |
| Journey Date | YYYY-MM-DD       |
| Bus ID       | Max 5 characters |
| Email        | Valid email only |


This wasn’t just an assignment — it was a software saga(special emotion )

Made by : PriiiAiVerse
