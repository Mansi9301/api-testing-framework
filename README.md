## About This Project

This framework simulates the kind of API validation performed in network 
management systems — validating endpoint reliability, data schema integrity, 
HTTP method coverage, and performance SLA thresholds. It is designed to 
reflect real-world telecom QA workflows where API consistency and response 
time are critical requirements.

Built entirely in Python using Pytest and the Requests library, the 
framework tests a RESTful API across 36 automated test cases and generates 
HTML reports for test result visibility.

# API Testing Framework

Production-grade REST API test framework built with Python and Pytest,
simulating network management system validation for telecom environments.

## Tech Stack
- Python 3.11
- Pytest
- Requests
- JSON Schema Validation
- Pytest-HTML Reports
- Concurrent Testing

## Test Coverage

### User Endpoint Tests (10)
- Status code validation
- JSON schema validation
- Data integrity checks
- Query parameter filtering
- Response time SLA validation
- Error handling for missing resources

### Posts Endpoint Tests (13)
- GET, POST, PUT, DELETE operations
- Schema validation
- Data creation and update integrity
- Response time validation
- Error handling

### Network Performance Tests (13)
- SLA threshold validation (1s, 2s, 3s)
- 10 concurrent request handling
- Cross-endpoint data integrity
- Sequential request consistency
- Content-Type header validation
- 5G network node simulation

## Total: 36 tests | All Passing | ~2 seconds

## How to Run

### 1. Clone the repo
git clone https://github.com/Mansi9301/api-testing-framework.git
cd api-testing-framework

### 2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Run all tests
pytest -v

### 5. Run with HTML report
mkdir reports
pytest -v --html=reports/report.html --self-contained-html


<img width="1440" height="900" alt="Screenshot 2026-03-20 at 7 26 55 PM" src="https://github.com/user-attachments/assets/f53ae2a7-8e63-4009-9a3a-b1f9ffc47044" />



https://github.com/user-attachments/assets/ee9a42a0-95d4-4b37-a3c4-e5568ec4796b


