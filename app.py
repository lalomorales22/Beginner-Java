from flask import Flask, render_template_string
import os

app = Flask(__name__)

# Simple markdown-like conversion
def convert_to_html(text):
    # Split into lines
    lines = text.split('\n')
    html_lines = []
    in_code_block = False
    
    for line in lines:
        # Code blocks
        if line.startswith('```'):
            if in_code_block:
                html_lines.append('</code></pre>')
                in_code_block = False
            else:
                html_lines.append('<pre><code>')
                in_code_block = True
            continue
            
        # Headers
        if line.startswith('# '):
            html_lines.append(f'<h1>{line[2:]}</h1>')
        elif line.startswith('## '):
            html_lines.append(f'<h2>{line[3:]}</h2>')
        elif line.startswith('### '):
            html_lines.append(f'<h3>{line[4:]}</h3>')
        # Lists
        elif line.startswith('- '):
            html_lines.append(f'<li>{line[2:]}</li>')
        # Code inline
        elif '`' in line and not in_code_block:
            line = line.replace('`', '<code>', 1)
            line = line.replace('`', '</code>', 1)
            html_lines.append(f'<p>{line}</p>')
        # Regular paragraphs
        elif line.strip():
            html_lines.append(f'<p>{line}</p>')
        # Empty lines
        else:
            html_lines.append('<br>')
            
    return '\n'.join(html_lines)

# Read and convert files
def read_file(filename):
    try:
        file_path = os.path.join(os.path.dirname(__file__), filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            return convert_to_html(content)
    except Exception as e:
        return f"<p>Error reading file: {str(e)}</p>"

# Base HTML template with modern styling
BASE_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Java Programming Course</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        /* Modern CSS Reset */
        *, *::before, *::after {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        /* Variables */
        :root {
            --primary-color: #2563eb;
            --secondary-color: #1e40af;
            --background-color: #f8fafc;
            --text-color: #1e293b;
            --code-bg: #282c34;
            --nav-height: 60px;
        }

        /* Base Styles */
        body {
            font-family: system-ui, -apple-system, sans-serif;
            line-height: 1.6;
            color: var(--text-color);
            background: var(--background-color);
            padding-top: var(--nav-height);
        }

        /* Navigation */
        nav {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            height: var(--nav-height);
            background: white;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            display: flex;
            align-items: center;
            padding: 0 2rem;
            z-index: 1000;
            overflow-x: auto;
        }

        nav a {
            color: var(--text-color);
            text-decoration: none;
            padding: 0.5rem 1rem;
            border-radius: 0.375rem;
            transition: background-color 0.3s;
            white-space: nowrap;
        }

        nav a:hover {
            background-color: #f1f5f9;
        }

        nav a.active {
            background-color: #e2e8f0;
        }

        /* Main Content */
        main {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 2rem;
        }

        /* Typography */
        h1 {
            font-size: 2.5rem;
            margin-bottom: 2rem;
            color: var(--primary-color);
        }

        h2 {
            font-size: 1.875rem;
            margin: 2rem 0 1rem;
            color: var(--secondary-color);
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 0.5rem;
        }

        h3 {
            font-size: 1.5rem;
            margin: 1.5rem 0 1rem;
            color: var(--secondary-color);
        }

        p {
            margin-bottom: 1.25rem;
        }

        /* Code Blocks */
        pre {
            background: var(--code-bg);
            color: #abb2bf;
            padding: 1rem;
            border-radius: 0.5rem;
            overflow-x: auto;
            margin: 1.5rem 0;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        code {
            font-family: 'Menlo', 'Monaco', 'Courier New', monospace;
            font-size: 0.9rem;
            background: var(--code-bg);
            color: #abb2bf;
            padding: 0.2rem 0.4rem;
            border-radius: 0.25rem;
        }

        pre code {
            padding: 0;
            background: none;
        }

        /* Lists */
        ul, ol {
            margin: 1rem 0;
            padding-left: 1.5rem;
        }

        li {
            margin-bottom: 0.5rem;
        }

        /* Course Cards */
        .course-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin: 2rem 0;
        }

        .course-card {
            background: white;
            border-radius: 0.5rem;
            padding: 1.5rem;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.3s;
        }

        .course-card:hover {
            transform: translateY(-4px);
        }

        .course-card h3 {
            color: var(--primary-color);
            margin-top: 1rem;
        }

        .course-card p {
            margin: 1rem 0;
            color: #4b5563;
        }

        .btn {
            display: inline-block;
            padding: 0.5rem 1rem;
            background: var(--primary-color);
            color: white;
            text-decoration: none;
            border-radius: 0.375rem;
            transition: background-color 0.3s;
        }

        .btn:hover {
            background: var(--secondary-color);
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            nav {
                padding: 0 1rem;
            }

            main {
                padding: 0 1rem;
            }

            h1 {
                font-size: 2rem;
            }

            h2 {
                font-size: 1.5rem;
            }

            h3 {
                font-size: 1.25rem;
            }

            .course-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <nav>
        <a href="{{ url_for('home') }}" {% if active_page == 'home' %}class="active"{% endif %}>
            <i class="fas fa-home"></i> Home
        </a>
        <a href="{{ url_for('part1') }}" {% if active_page == 'part1' %}class="active"{% endif %}>Part 1: Basics</a>
        <a href="{{ url_for('part2') }}" {% if active_page == 'part2' %}class="active"{% endif %}>Part 2: Strings & Methods</a>
        <a href="{{ url_for('part3') }}" {% if active_page == 'part3' %}class="active"{% endif %}>Part 3: Control Flow</a>
        <a href="{{ url_for('part4') }}" {% if active_page == 'part4' %}class="active"{% endif %}>Part 4: Arrays & Objects</a>
    </nav>
    <main>
        {% if active_page == 'home' %}
            <h1>Welcome to Java Programming</h1>
            <p>Start your journey into programming with our comprehensive Java course. Choose a section below to begin:</p>
            <div class="course-grid">
                <div class="course-card">
                    <i class="fas fa-code fa-2x" style="color: var(--primary-color);"></i>
                    <h3>Part 1: Java Basics</h3>
                    <p>Learn about variables, data types, and basic expressions in Java.</p>
                    <a href="{{ url_for('part1') }}" class="btn">Start Learning</a>
                </div>
                <div class="course-card">
                    <i class="fas fa-font fa-2x" style="color: var(--primary-color);"></i>
                    <h3>Part 2: Strings & Methods</h3>
                    <p>Master string manipulation and method creation in Java.</p>
                    <a href="{{ url_for('part2') }}" class="btn">Start Learning</a>
                </div>
                <div class="course-card">
                    <i class="fas fa-code-branch fa-2x" style="color: var(--primary-color);"></i>
                    <h3>Part 3: Control Flow</h3>
                    <p>Understand decision making and loops in Java programs.</p>
                    <a href="{{ url_for('part3') }}" class="btn">Start Learning</a>
                </div>
                <div class="course-card">
                    <i class="fas fa-cubes fa-2x" style="color: var(--primary-color);"></i>
                    <h3>Part 4: Arrays & Objects</h3>
                    <p>Learn about arrays, objects, and practical programming.</p>
                    <a href="{{ url_for('part4') }}" class="btn">Start Learning</a>
                </div>
            </div>
        {% else %}
            {{ content|safe }}
        {% endif %}
    </main>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(BASE_TEMPLATE, active_page='home', content='')

@app.route('/part1')
def part1():
    content = read_file('java-course-part1.md')
    return render_template_string(BASE_TEMPLATE, active_page='part1', content=content)

@app.route('/part2')
def part2():
    content = read_file('java-course-part2.md')
    return render_template_string(BASE_TEMPLATE, active_page='part2', content=content)

@app.route('/part3')
def part3():
    content = read_file('java-course-part3.md')
    return render_template_string(BASE_TEMPLATE, active_page='part3', content=content)

@app.route('/part4')
def part4():
    content = read_file('java-course-part4.md')
    return render_template_string(BASE_TEMPLATE, active_page='part4', content=content)

if __name__ == '__main__':
    app.run(debug=True)