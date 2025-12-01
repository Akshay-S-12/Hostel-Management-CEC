
# Hostel Management System - College of Engineering Cherthala (CEC)

## Overview
The **Hostel Management System** is a web-based application developed specifically for **College of Engineering Cherthala (CEC)** to streamline and automate hostel operations. This system was created  to overcome the inefficiencies and manual processes of the existing hostel management methods. It provides a user-friendly platform for both students and administrators to manage hostel activities effectively.

## Features

### For Students:
- Online room allocation and tracking.
- Submission of requests or complaints.
- View hostel rules, announcements, and notices.
- Fee payment tracking.

### For Administrators:
- Manage student records and hostel rooms.
- Approve or reject requests and complaints.
- Track hostel occupancy and availability.
- Generate reports for hostel management efficiency.

## Technology Stack
- **Frontend:** HTML, CSS, JavaScript, Bootstrap, Jinja Templates  
- **Backend:** Python (Flask)  
- **Database:** SQL (MySQL / SQLite)  
- **Others:** Responsive design for easy access across devices  

## Project Structure
```
Hostel-Management-CEC/
├── app/                # Main Flask application
│   ├── static/         # CSS, JS, images
│   ├── templates/      # HTML/Jinja templates
│   ├── routes.py       # Application routes
│   └── models.py       # Database models
├── requirements.txt    # Python dependencies
├── README.md
└── run.py              # Entry point to run the app
```

## Problem Statement
Manual hostel management in CEC often leads to:
- Difficulty in tracking room allocation.
- Delays in submitting and resolving student complaints.
- Inefficient reporting and occupancy tracking.
  
This system aims to **digitize all hostel operations**, making processes faster, transparent, and error-free.

## Installation and Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/Akshay-S-12/Hostel-Management-CEC.git
   ```
2. Navigate to the project folder:
   ```bash
   cd Hostel-Management-CEC
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the database (MySQL/SQLite) and configure `config.py`.
5. Run the application:
   ```bash
   python run.py
   ```



## Future Enhancements
- Integration of payment gateway for hostel fees.
- Mobile application for easier access.
- Automated notifications and alerts.

## Conclusion
This **Hostel Management System** is specifically tailored for **CEC**, reducing administrative workload and improving student experience. It represents a practical solution  for efficient hostel management.

---


