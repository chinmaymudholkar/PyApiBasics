# PyApiBasics

## About
This Python-based test automation project aims to provide the user with the boilerplate code for a test harness and a few sample test cases for REST APIs.  The harness utilizes the powerful yet easy-to-use and versatile test framework - PyTest.

The tests perform actions on https://reqres.in - a great free API testing website.

## Installation
Installation is easy and just requires Python 3.10 (or newer) to be installed on the host computer.  To set the project up on your computer:
1. Clone the repo to any directory using ```git clone https://github.com/chinmay62/PyApiBasics.git ```
1. Open the repo folder in any IDE (Visual Studio Code recommended)
1. Create a virtual environment by running the following command in the terminal ```python -m venv .venv```
1. Activate the new environment by running ```.venv\Scripts\Activate.ps1``` (on Windows) or ```source .venv\bin\activate``` (on Linux or Mac)
1. Install all required dependencies by running ```pip install -r requirements.txt```
1. Once the project is set up, verify the execution by running ```pytest -m setup```.  This will run the tests within the project that will verify the project is setup correctly.  If all tests pass, it means that the project is set up correctly.

## Test Execution
Once the setup tests pass, the API tests can be run using the following commands:

|Command|Narration|
|-------|---------|
|```pytest```|Runs all tests|
|```pytest -m get```|Run all tests for the GET method (retrieve record)|
|```pytest -m post```|Run all tests for the POST method (create record)|
|```pytest -m delete```|Run all tests for the DELETE method (delete record)|
|```pytest -m put```|Run all tests for the PUT method (update record)|
|```pytest -m patch```|Run all tests for the PATCH method (update record)|