from flask import Flask, render_template_string

app = Flask(__name__)


html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Portfolio</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            background-color: black;
            color: #00ff00; /* green */
            font-family: Arial, Helvetica, sans-serif;
        }
        .container {
            max-width: 900px;
            margin: auto;
            padding: 40px;
        }
        h1, h2 {
            color: red;
        }
        p {
            line-height: 1.6;
        }
        .skills span {
            display: inline-block;
            margin: 5px;
            padding: 8px 12px;
            border: 1px solid red;
            color: #00ff00;
        }
        footer {
            margin-top: 40px;
            border-top: 1px solid red;
            padding-top: 20px;
            text-align: center;
            color: red;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Hi, I'm Your Name</h1>
        <p>Python Developer | Web Developer | Learner</p>

        <h2>About Me</h2>
        <p>
            Main ek passionate Python developer hoon jo web applications aur automation par kaam karta hai.
        </p>

        <h2>Skills</h2>
        <div class="skills">
            <span>Python</span>
            <span>Flask</span>
            <span>HTML</span>
            <span>CSS</span>
            <span>Git</span>
        </div>

        <h2>Projects</h2>
        <p>
            • Portfolio Website<br>
            • Python Automation Scripts<br>
            • Flask Web Apps
        </p>

        <h2>Contact</h2>
        <p>Email: your@email.com</p>

        <footer>
            © 2026 Your Name | Made with Python
        </footer>
    </div>
</body>
</html>
"""

@app.route("/")
def portfolio():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
