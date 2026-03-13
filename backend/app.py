from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample exercise data (in a real app, you could pull from an API or database)
exercises = {
    "weight_loss": [
        {"name": "Jumping Jacks", "sets": 3, "reps": 30},
        {"name": "Burpees", "sets": 3, "reps": 20},
        {"name": "Mountain Climbers", "sets": 3, "reps": 30}
    ],
    "muscle_gain": [
        {"name": "Push-Ups", "sets": 4, "reps": 12},
        {"name": "Squats", "sets": 4, "reps": 15},
        {"name": "Dumbbell Rows", "sets": 4, "reps": 12}
    ],
    "endurance": [
        {"name": "Running", "sets": 1, "reps": "20 minutes"},
        {"name": "Cycling", "sets": 1, "reps": "30 minutes"},
        {"name": "Plank", "sets": 3, "reps": 60}
    ]
}

@app.route('/generate-routine', methods=['POST'])
def generate_routine():
    data = request.get_json()
    goal = data.get('goal', '')
    equipment = data.get('equipment', [])
    days_per_week = data.get('days_per_week', 3)

    # Generate workout plan based on the user's goal
    if goal not in exercises:
        return jsonify({"error": "Invalid goal selected"}), 400

    routine = exercises[goal] * (days_per_week // 3)  # Distribute exercises across the week
    
    return jsonify({"workout_routine": routine})

if __name__ == '__main__':
    app.run(debug=True)