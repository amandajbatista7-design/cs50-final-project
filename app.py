# copilot and cs50 duck guidance
from flask import Flask, render_template, request, jsonify, redirect, url_for
import sqlite3

app = Flask(__name__)

def connect_db():
    return sqlite3.connect('shapes.db')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/letters')
def letters():
    return render_template('letters.html')

@app.route('/shapes_colors')
def shapes_colors():
    return render_template('shapes_colors.html')

@app.route('/get_questions')
def get_question():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM questions ORDER BY RANDOM() LIMIT 10')
    questions = cursor.fetchall()
    if not questions:
        return jsonify({'error': 'No questions found'}), 404

    question_data = []
    for question in questions:
        cursor.execute('SELECT * FROM answers WHERE question_id=?', (question[0],))
        answers = cursor.fetchall()
        question_data.append({
            'question': question[1],
            'options': [{'id': answer[0], 'image_path': answer[2]} for answer in answers],
            'correct': next((i for i, ans in enumerate(answers) if ans[3]), None)
    })

    conn.close()
    return jsonify(question_data)

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    data = request.json
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM answers WHERE id=?', (data['answer_id'],))
    answer = cursor.fetchone()
    correct = answer[3]
    conn.close()
    return jsonify({'correct': correct})

@app.route('/end_shapes')
def end_shapes():
    return render_template('end_shapes.html')

@app.route('/end_letters')
def end_letters():
    return render_template('end_letters.html')

if __name__ == '__main__':
    app.run(debug=True)
