import os

# Define the content of each file
html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LOUIS SOLOM YOU HAVE BEEN HACKED</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>LOUIS SOLOM YOU HAVE BEEN HACKED</h1>
    </header>
    <main>
        <section id="message">
            <p>
                print('Hello, World!')<br>
                for i in range(10):<br>
                &nbsp;&nbsp;&nbsp;&nbsp;print(i)<br>
                if (x > 0) {<br>
                &nbsp;&nbsp;&nbsp;&nbsp;console.log('Positive');<br>
                } else {<br>
                &nbsp;&nbsp;&nbsp;&nbsp;console.log('Non-positive');<br>
                }<br>
                SELECT * FROM users;<br>
                def my_function():<br>
                &nbsp;&nbsp;&nbsp;&nbsp;pass<br>
                #include &lt;iostream&gt;<br>
                int main() {<br>
                &nbsp;&nbsp;&nbsp;&nbsp;return 0;<br>
                }<br>
                while (true) {<br>
                &nbsp;&nbsp;&nbsp;&nbsp;break;<br>
                }<br>
                let x = Math.random();<br>
                x = x * 100;<br>
                if (x > 50) {<br>
                &nbsp;&nbsp;&nbsp;&nbsp;console.log('Greater than 50');<br>
                } else {<br>
                &nbsp;&nbsp;&nbsp;&nbsp;console.log('Less than or equal to 50');<br>
                }<br>
                function exampleFunc() {<br>
                &nbsp;&nbsp;&nbsp;&nbsp;return 'example';<br>
                }<br>
                console.log(exampleFunc());<br>
                import random<br>
                for _ in range(5):<br>
                &nbsp;&nbsp;&nbsp;&nbsp;print(random.randint(1, 100))<br>
                // JavaScript comment<br>
                <!-- HTML comment --><br>
            </p>
        </section>
        <section id="image">
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Anonymous.svg/1200px-Anonymous.svg.png" alt="Anonymous Image">
        </section>
    </main>
    <footer>
        <p>&copy; 2024 Hacked by LOUIS SOLOM</p>
    </footer>
    <script src="script.js"></script>
</body>
</html>
'''

css_content = '''body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    background-color: #000000;
    color: #00ff00;
}

header {
    background-color: #333333;
    color: #00ff00;
    padding: 15px 0;
    text-align: center;
}

main {
    padding: 20px;
}

section {
    margin-bottom: 20px;
}

footer {
    background-color: #333333;
    color: #00ff00;
    text-align: center;
    padding: 10px 0;
    position: fixed;
    width: 100%;
    bottom: 0;
}

img {
    display: block;
    margin-left: auto;
    margin-right: auto;
}
'''

js_content = '''document.addEventListener('DOMContentLoaded', function() {
    console.log('LOUIS SOLOM YOU HAVE BEEN HACKED');
});
'''

# Create the project directory and navigate into it
os.makedirs('my-hacked-website', exist_ok=True)
os.chdir('my-hacked-website')

# Create and write to index.html
with open('index.html', 'w') as file:
    file.write(html_content)

# Create and write to styles.css
with open('styles.css', 'w') as file:
    file.write(css_content)

# Create and write to script.js
with open('script.js', 'w') as file:
    file.write(js_content)

print("Website files have been created successfully.")


