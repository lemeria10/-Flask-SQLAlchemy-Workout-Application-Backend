from flask import Flask
from flask_migrate import Migrate
from models import db
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)

    # Import models (IMPORTANT for migrations)
    from models import Exercise, Workout, WorkoutExercise

    # Register blueprints
    from routes.exercise_routes import exercise_bp
    from routes.workout_routes import workout_bp
    from routes.workout_exercise_routes import we_bp

    app.register_blueprint(exercise_bp)
    app.register_blueprint(workout_bp)
    app.register_blueprint(we_bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)