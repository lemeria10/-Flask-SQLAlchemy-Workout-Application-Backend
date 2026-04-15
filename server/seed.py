from app import app
from models import db, Exercise, Workout, WorkoutExercise
from datetime import date

with app.app_context():

    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()

    squat = Exercise(name="Squat", category="Strength", equipment_needed=True)
    run = Exercise(name="Running", category="Cardio", equipment_needed=False)

    workout = Workout(date=date.today(), duration_minutes=45, notes="Leg day")

    db.session.add_all([squat, run, workout])
    db.session.commit()

    we = WorkoutExercise(workout_id=workout.id, exercise_id=squat.id, sets=4, reps=10)

    db.session.add(we)
    db.session.commit()

    print("Seeded!")