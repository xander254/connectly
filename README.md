
# Connectly - ISP Management System


Connectly is an ISP management system designed to help small ISPs automate billing, manage users, and track internet usage. 
The system integrates with MikroTik routers using Mikrotik apis for network management and supports M-Pesa payments for automated transactions.
### PS: This is an mvp project ost features are not fully completed yet.


## Features

- Automated Billing: Automatically suspends accounts upon expiry and reactivates upon payment.

- User Management: Allows ISPs to add, remove, and update customer details.
- Usage Tracking: Logs user bandwidth consumption and generates reports.
- Admin Dashboard: A simple web-based UI for ISPs to monitor users and payments.

## Architecture

The system consists of the following components:

Backend: Built with Flask (Python). 
SQLAlchemy for database management.
Database: MySQL for structured data storage.
Frontend: A web dashboard for administrators. (v0)
Networking: MikroTik API for real-time user control.
Payment Gateway: M-Pesa/Jenga API for processing transactions. (Not completed)

## Installation
Prerequisites
Python 3.8+
MySQL Server
MikroTik Router
Flask and required dependencies

## Set Up Instructions

Clone the repository:

`git clone https://github.com/your-username/connectly.git`
`cd connectly`
Install dependencies:
`pip install -r requirements.txt`
Configure environment variables:
Create a .env file with the following:

`DATABASE_URL=mysql://user:password@localhost/connectly_db
MIKROTIK_IP=192.168.88.1
MIKROTIK_USERNAME=admin
MIKROTIK_PASSWORD=yourpassword
MPESA_API_KEY=your_mpesa_api_key`

Run database migrations:
`flask db upgrade
Start the application:
flask run`
Access the admin dashboard at `http://localhost:5000`




## Future Improvements

Implement RADIUS authentication for enhanced security and hotspot intergration.
Expand support for additional payment gateways.
Introduce AI-driven bandwidth optimization.
Improve user flows.
## License

This project is licensed under the MIT License.


## Contact
For questions or contributions, reach out via email at alexkinyanjui356@gmail.com or open an issue on GitHub.

Connectly - Empowering Small ISPs Through Automation


