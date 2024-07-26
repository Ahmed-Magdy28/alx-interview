<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Pascal's Triangle Generator</h1>

<h2>Overview</h2>
<p>
    This repository contains a Python function that generates Pascal's Triangle up to a specified number of rows. 
    Pascal's Triangle is a triangular array of binomial coefficients, which has many applications in mathematics 
    and computer science, including combinatorics, probability, and algebra.
</p>

<h2>Features</h2>
<ul>
    <li>Generates Pascal's Triangle up to any specified number of rows.</li>
    <li>Handles edge cases such as non-positive integers.</li>
    <li>Efficiently constructs the triangle using an iterative method.</li>
    <li>Easy to understand and well-documented code.</li>
</ul>

<h2>Usage</h2>
<p>
    To use the Pascal's Triangle generator, you need Python 3 installed on your system. 
    You can include the function in your Python scripts or run it as a standalone script.
</p>

<h3>Example Usage</h3>
<p>To generate Pascal's Triangle with 5 rows:</p>
<pre>
<code>
if __name__ == "__main__":
    print(pascal_triangle(5))
</code>
</pre>
<p>This will output:</p>
<pre>
<code>
[
 [1],
 [1, 1],
 [1, 2, 1],
 [1, 3, 3, 1],
 [1, 4, 6, 4, 1]
]
</code>
</pre>

<h2>Installation</h2>
<ol>
    <li>Clone the repository:
        <pre><code>git clone https://github.com/yourusername/pascal-triangle-generator.git</code></pre>
    </li>
    <li>Navigate to the project directory:
        <pre><code>cd pascal-triangle-generator</code></pre>
    </li>
</ol>

<h2>Running the Script</h2>
<p>You can run the script directly from the command line:</p>
<pre><code>python3 pascal_triangle.py</code></pre>

<h2>License</h2>
<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

<h2>Contributions</h2>
<p>
    Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss any changes.
</p>

<h2>Acknowledgements</h2>
<p>
    Thanks to everyone who has contributed to this project. Special thanks to the Python community for their 
    continuous support and resources.
</p>

</body>
</html>
