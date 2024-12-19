# **Django Account Management System**

*Django Account Management System* is a Django-based web application for managing accounts, transferring funds, and importing account data from CSV files. The system allows easy creation and management of accounts, handles fund transfers with validation, and ensures transaction integrity with atomic operations.

## **Features**
- **Account Management**:
  - Create, update, and list accounts with opening balances.
  - Maintain account details including name and balance.
- **Fund Transfers**:
  - Transfer funds between accounts with validation for sufficient funds.
  - Use atomic transactions to ensure that both debit and credit operations are successful or rolled back in case of failure.
- **CSV Import**:
  - Import accounts and balances from CSV files, enabling batch creation of accounts.
- **Error Handling**:
  - Display user-friendly error messages for issues like insufficient funds or invalid input.
- **Pagination**:
  - The application includes a pagination function to manage large datasets, making it easy to view accounts in manageable chunks.

## **Technologies Used**
- **Backend**: Django, Python
- **Frontend**: HTML, CSS
- **Database**: SQLite 
