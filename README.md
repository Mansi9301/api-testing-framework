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