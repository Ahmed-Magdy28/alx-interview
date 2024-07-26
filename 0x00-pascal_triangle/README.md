Pascal's Triangle Generator
Overview
This repository contains a Python function that generates Pascal's Triangle up to a specified number of rows. Pascal's Triangle is a triangular array of binomial coefficients, which has many applications in mathematics and computer science, including combinatorics, probability, and algebra.

Features
Generates Pascal's Triangle up to any specified number of rows.
Handles edge cases such as non-positive integers.
Efficiently constructs the triangle using an iterative method.
Easy to understand and well-documented code.
Usage
To use the Pascal's Triangle generator, you need Python 3 installed on your system. You can include the function in your Python scripts or run it as a standalone script.

Example Usage
To generate Pascal's Triangle with 5 rows:

python
Copy code
if __name__ == "__main__":
    print(pascal_triangle(5))
This will output:

csharp
Copy code
[
 [1],
 [1, 1],
 [1, 2, 1],
 [1, 3, 3, 1],
 [1, 4, 6, 4, 1]
]
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/pascal-triangle-generator.git
Navigate to the project directory:
bash
Copy code
cd pascal-triangle-generator
Running the Script
You can run the script directly from the command line:

bash
Copy code
python3 pascal_triangle.py
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributions
Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss any changes.

Acknowledgements
Thanks to everyone who has contributed to this project. Special thanks to the Python community for their continuous support and resources.