## Python CHMOD Simplifier

### This script converts symbolic representation of CHMOD permissions to it's numerical equivalent, and the Numerical representation of CHMOD permissions to its Symbolic equivalent as well.
Example (numerical to symbolic representation):
input: 777
output: rwxrwxrwx

![Symbolic Representation](./SymbolicNotation.PNG)
[Symbolic Representation](./SymbolicNotation.PNG)

Example (symbolic to numerical representation):
input: rwxrwxrwx
output: 777

![Numerical Representation](./NumericalNotation.PNG)
[Numerical Representation](./NumericalNotation.PNG)

### How to use this script?

1. Make sure all the requirements for the script are present in your system by running:

    pip install -r requirements.txt
    
2. The script has 2 options:
- Symbolic to Numerical (N)
- Numerical to Symbolic (S)

Pass the desired mode of conversion while executing the script

3. Run the following command:
    python chmod_simplifier.py <representation> <mode>
    
    Replace: 
        - <representation> with 777 or rwxrwxrwx based on your preferred mode of conversion
        - <mode> with either 'S' or 'N' as per the desired mode

3. View output on console

### Author

[Schezeen Fazulbhoy](https://github.com/schezfaz)