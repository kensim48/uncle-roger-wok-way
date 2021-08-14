# uncle-roger-wok-way

## Prequisites
### For main application
1. [Docker](https://docs.docker.com/get-docker/)
2. [Docker Compose](https://docs.docker.com/compose/)
3. Ports 8000 and 8080 to be free

### For loading mock items
1. [Python](https://docs.python.org/)
2. [Python venv](https://docs.python.org/3/library/venv.html)
## Instructions to run
### Main app
1. `docker-compose build`
2. `docker-compose up`

### Loading mock items
1. `cd backend_populate`
2. `pip install -r requirements.txt`
3. `python main.py`
#### If you prefer venv
2. `python -m venv venv`
3. `venv\Scripts\activate`(win) or `source venv\bin\activate`(OSX or Linux)
4. `pip install -r requirements.txt`
5. `python main.py`

## Objectives
### Main Objectives
#### Frontend Webpage
- [x] A page to list all the items in the store
- [x] A form to add / update item in the store
- [x] Demonstrate calling API to perform CRUD
#### Backend Webpage
- [x] CREATE an item in the store
- [x] READ list of all items in the store
- [x] UPDATE an item in the store
- [x] DELETE an item in the store
- [x] JSON response
- [x] Item attributes:
    - ID (changed to serial_id, as id is pk used by Django)
    - Name
    - Price
### Optional Objectives
- [ ] (?:)) Extra points for good frontend design (frontend)
- [x] Extra points for usage of database wrapper – ORM (backend)
- [x] Usage of container technologies such as Dockers or Kubernetes
- [ ] Deployment of security controls such as IDS, IPS, Firewall, etc.
- [ ] Strong authentication with 2FA.   
- [ ] Usage of cloud technologies such as AWS, GCP or Azure
    - For AWS deployment, could be as follows:
        - frontend on S3
        - backend on ECS
        - database on PostgreSQL RDS
        - authentication via Cognito
        - CI/CD via CodePipeline

## Information
### Links
Frontend: http://localhost:8080/

Backend: http://localhost:8000/admin
### Backend Documentation
API documentation is provided in this [Postman Documentation](https://documenter.getpostman.com/view/9432978/Tzz7Pxk9)
### Accounts
#### Default Account
Username: admin

Password: password

#### Account types
There are two types of accounts, staff and non-staff.
A staff account has some additional privileges over a non-staff account.
1. Access backend admin page
2. Access certain additional endpoints (shown in Postman Document)
3. Make other users staff through admin page

Any user registered via the frontend, or registration endpoint is automatically a non-staff

#### Things to note
1. Some design decisions were made to assist with easy setup of MVP, i.e. database is in docker container and will be destroyed, sensitive info can be moved to environment variables for future use
2. OAuth2 flow is not properly setup, and only uses Access Token for verification
3. Made orders are only readable by staff and only through API query or admin portal
