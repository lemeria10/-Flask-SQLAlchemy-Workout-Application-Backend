# -Flask-SQLAlchemy-Workout-Application-Backend

🏋️ Workout Tracking API

A RESTful backend API built with Flask, SQLAlchemy, and Marshmallow for tracking workouts and exercises. This system allows personal trainers to create workouts, manage exercises, and associate exercises with workouts including performance data such as sets, reps, and duration.

🚀 Features
Create, view, and delete workouts
Create, view, and delete exercises
Link exercises to workouts with:
Sets
Reps
Duration (seconds)
Many-to-many relationship between workouts and exercises
Data validation using SQLAlchemy and Marshmallow
Cascading deletes for clean database integrity
JSON API responses with nested relationships
🧱 Tech Stack
Python 3.8+
Flask
Flask-SQLAlchemy
Flask-Migrate
Marshmallow
SQLite (default database)
📁 Project Structure
server/
│
├── app.py
├── config.py
├── models.py
├── seed.py
├── requirements.txt
│
├── routes/
│   ├── exercise_routes.py
│   ├── workout_routes.py
│   ├── workout_exercise_routes.py
│
├── schemas/
│   ├── exercise_schema.py
│   ├── workout_schema.py
│   ├── workout_exercise_schema.py
│
├── migrations/
⚙️ Setup Instructions
1. Clone Repository
git clone https://github.com/your-username/workout-api.git
cd workout-api
2. Create Virtual Environment
Using Pipenv:
pipenv install
pipenv shell

OR using venv:

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3. Install Dependencies
pip install -r requirements.txt
4. Set Up Database
export FLASK_APP=app.py
flask db init
flask db migrate -m "initial migration"
flask db upgrade
5. Seed Database (Optional)
python seed.py
6. Run Server
python app.py

Server runs at:

http://127.0.0.1:5000
📌 API Endpoints
🏋️ Workouts
Method	Endpoint	Description
GET	/workouts	Get all workouts
GET	/workouts/<id>	Get single workout (with exercises)
POST	/workouts	Create a workout
DELETE	/workouts/<id>	Delete a workout
💪 Exercises
Method	Endpoint	Description
GET	/exercises	Get all exercises
GET	/exercises/<id>	Get single exercise (with workouts)
POST	/exercises	Create an exercise
DELETE	/exercises/<id>	Delete an exercise
🔗 Workout Exercises (Relationship Table)
Method	Endpoint
POST	/workouts/<workout_id>/exercises/<exercise_id>/workout_exercises
Example Body:
{
  "sets": 4,
  "reps": 12,
  "duration_seconds": null
}
🔄 Relationships
A Workout has many Exercises through WorkoutExercises
An Exercise has many Workouts through WorkoutExercises
WorkoutExercise stores:
sets
reps
duration_seconds
🧠 Validation Rules
Model-Level Validations:
Exercise name must be unique
Workout duration must be greater than 0
WorkoutExercise values must be positive integers
Schema-Level Validations:
Exercise name must be at least 2 characters
Workout duration must be positive
🧪 Example Workflow
Create an Exercise
Create a Workout
Link them using WorkoutExercises endpoint
Fetch Workout → see nested exercises
Fetch Exercise → see related workouts
📦 Example Response (GET /workouts/1)
{
  "id": 1,
  "date": "2026-04-15",
  "duration_minutes": 60,
  "notes": "Leg day",
  "workout_exercises": [
    {
      "sets": 4,
      "reps": 12,
      "exercise": {
        "name": "Squat",
        "category": "Strength",
        "equipment_needed": true
      }
    }
  ]
}
🧑‍💻 Author

Built as a backend summative lab project using Flask.

📌 Notes
Ensure migrations are run before seeding
Do not insert duplicate exercise names (unique constraint)
Use correct endpoint formats for linking exercises to workouts
✅ Status

✔ Fully functional REST API
✔ Relational database design
✔ Validated models and schemas
✔ Production-ready structure
