import file_functins as ff

def summer(numbers):
    total = 0
    for digit in str(numbers):
        total +=int(digit)
    ff.writer('summer.txt',str(total))

summer(999)