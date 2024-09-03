# FastAPI-Practice
<h2>FastAPI Student Management API</h2>
This project is a simple API built using FastAPI that allows you to manage student records. It demonstrates basic CRUD (Create, Read, Update, Delete) operations with students' data using FastAPI’s powerful and modern features.

<h3>Features</h3>

<b>Welcome Endpoint:</b> Greets users with a simple message.

<b>Retrieve Student Info:</b> Get student details by their ID or name.

<b>Create Student:</b> Add a new student to the database.

<b>Update Student:</b> Update existing student information.

<b>Delete Student:</b> Remove a student record from the database.

<h3>Project Structure</h3>
index: A simple endpoint that welcomes users.
/student-info/{student_id}: Retrieve student details by ID.
/student-info-by-name: Retrieve student details by name or ID.
/create-student/{student_id}: Add a new student.
/update-student/{student_id}: Update student information.
/delete-student/{student_id}: Delete a student record.

<h3>How to Run the Project</h3>

<b>Clone the repository:</b>
git clone https://github.com/yourusername/your-repository.git

<b>Navigate to the project directory:</b>
cd your-repository

<b>Create and activate a virtual environment:</b>

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

<b>Install dependencies:</b>

pip install fastapi uvicorn pydantic

<b>Run the application:</b>

uvicorn main:app --reload

<b>Access the API:</b>

Go to http://127.0.0.1:8000 to see the welcome message.
Explore interactive API docs at http://127.0.0.1:8000/docs.

<h3>Technologies Used</h3>
<b>FastAPI:</b> Modern, fast web framework for building APIs.

<b>Pydantic:</b> Data validation and settings management using Python type annotations.

<h3>Contributing</h3>
Feel free to submit issues or pull requests if you have ideas to improve the project.

<h3>License</h3>
This project is open-source and available under the MIT License.
