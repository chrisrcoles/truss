# Truss Software Engineering Coding Challenge

# Solution Outline

[Challenge](https://github.com/chrisrcoles/truss/blob/master/docs/challenge.MD)

# Setting up the Application

1. Clone project by running 
- `git clone https://github.com/chrisrcoles/truss.git` 
2. Install and start [Docker](https://docs.docker.com/install/)
3. Build Docker Image 
- `docker build -t truss-app .`
4. Run Python Process in Docker Container
- `docker run -it --rm --name truss-running-app truss-app`


# Running the Project
1. `cat sample | ./main.py > output.csv`
2. `./main.py sample.csv > output.csv`

# Run Tests
1. Run all tests `python -m unittest discover tests`
2. Run a specific test `python -m unittest tests/<test_file.py>`

# Application Architecture

### Tools: Python 3.6, Docker

Directory structure
 - `truss/csvparser` - All code for the CSV Parser, including library and utility helpers
 - `truss/csvparser/lib` - CSV Parser Library Classes and Functions
 - `truss/csvparser/lib/exceptions.py` - Singleton class responsible for managing exceptions 
 - `truss/csvparser/lib/normalizers.py` - Library functions that normalize and transform the data
 - `truss/csvparser/lib/parser.py` - Library functions responsible for reading and writing the stdin/stdout as well as string manipulation. 
 - `truss/csvparser/lib/validators.py` - Library functions responsible for ensuring all data is parseable.  
 - `truss/csvparser/utils` - CSV Parser Utility Functions
 - `truss/csvparser/utils/helpers.py` - Utility functions mainly responsible for dealing with time 
 - `truss/docs` - Documentation
 - `truss/tests` - All tests
 - `truss/main.py` - Main executable script
 - `truss/Dockerfile` - Dockerfile
 
 
 
  
