from flask import Flask, request, render_template_string
import csv
from pathlib import Path

app = Flask(__name__)


FILE = Path(__file__).with_name("students.txt")


FORM = """
<h2>Student Details</h2>

<form action="/save" method="post">
    Name: <input name="name" required><br><br>
    Branch: <input name="branch" required><br><br>
    Email: <input type="email" name="email" required><br><br>
    Mobile: <input name="mobile" required><br><br>
    Division: <input name="division" required><br><br>

    <button type="submit">Submit</button>
</form>

<br>
<a href="/read">Read Saved Details</a>
"""

TABLE = """
<h2>Saved Student Details</h2>

<table border="1" cellpadding="10">
    <tr>
        <th>Name</th>
        <th>Branch</th>
        <th>Email</th>
        <th>Mobile</th>
        <th>Division</th>
    </tr>

    {% for student in students %}
    <tr>
        {% for value in student %}
        <td>{{ value }}</td>
        {% endfor %}
    </tr>
    {% endfor %}
</table>

<br>
<a href="/">Back to Form</a>
"""


@app.route("/")
def home():
    return FORM


@app.route("/save", methods=["POST"])
def save():
    student = [
        request.form["name"],
        request.form["branch"],
        request.form["email"],
        request.form["mobile"],
        request.form["division"]
    ]

    with FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(student)

    return """
    <h3>Details saved successfully!</h3>
    <a href="/">Add Another Student</a><br><br>
    <a href="/read">Read Saved Details</a>
    """


@app.route("/read")
def read():
    students = []

    if FILE.exists():
        with FILE.open("r", newline="", encoding="utf-8") as file:
            students = list(csv.reader(file))

    return render_template_string(TABLE, students=students)


if __name__ == "__main__":
    app.run()