# Enterprise API - Lakasir
Lakasir client api allows you to integration with your products.

## Example
```python
# create object
lakasir = LakasirClient(
    base_url='BASE_URL',
    email='EMAIL',
    password='PASSWORD',
)

# showing user information
lakasir.me()

# showing transaction of sells
lakasir.transaction_sells()
```

## Installation
To install the package (dev), run the following command:
```bash
git clone https://github.com/DeeloaSociety/enterprise_api
cd enterprise_api/lakasirclient
pip install .
```

## List API
#### Transactions
- [X] /transaction/selling (List of transactions related to sales)
- [X] /transaction/dashboard (Overview of total sales, total gross profit, and total revenue)
#### Auth, Profile, and About
- [X] /auth/login (Process for users to authentication)
- [X] /auth/me (User profile information)
- [X] /about (Information of merchant/store such as name, location, etc.)