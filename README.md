# TwoGame Website v1.3

a full website that allows users to register and play 2 different games

## Getting Started

These instructions will help you set up and run the project locally for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following software installed:

- Python (3.10.5)
- Node.js (18.18.0)

### Installing

#### Backend (FastAPI)

1. activate the vertual environment or create a new one.
- Windows:
  ```
  venv\Scripts\activate
  ```
- Linux/macOS:
  ```
  source venv/bin/activate
  ```
2. Install the required Python packages.
    ```
    pip install -r requirements.txt
    ```
2. Navigate to the `/fastapi` directory.

5. Start the FastAPI application.
    ```
    uvicorn main:app --reload
    ```

#### Frontend (React)

1. Navigate to the `/reactjs` directory then to '/my-app' 
    ```
    cd /reactjs
    cd my-app
    ```
2. Install the required Node.js packages.
    ```
    npm install
    ```
3. Start the React development server.
    ```
    npm start
    ```

### Usage

Both backend and frontend runs on the localhost, but each on different port.
Backend on port 8000
Frontend on port 3000
and there is a middleware between them to transifer data and integrate the apis with the frontend

You can go directly to 'http://localhost:3000/home' to start navigating through the app 
NOTE: 'http://localhost:3000/' returns nothin for this version. 

## Built With

- [FastAPI](https://fastapi.tiangolo.com/) - The backend framework used
- [React](https://reactjs.org/) - The frontend library used


## updates v1.3

- Created Game2 with corresponding sheet in the database
- edited the frontend to optimize user experience 
- just solved a bug in the login page :))
- made the site direct to the welcome page if not authenticated :))
- edited the logic for game 1, to randomize the equation totally each time