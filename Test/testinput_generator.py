output_str = ""
comma = " ,"
Isfirstline = True
Isfirstchar  = True
readlines = ""

with open("raw_input.py", "rt") as readptr:

    readlines = readptr.read().splitlines()

    output_str = "[\n"
    for line in readlines:
        if Isfirstline:
            output_str += "["
            Isfirstline = False
        else:
            output_str += ",\n["
        Isfirstchar = True
        for char in line:
            if Isfirstchar:
                Isfirstchar = False
            else:
                output_str += comma
            if char == ".":
                 char = 0
            output_str += str(char)
        else:
            output_str += "]"

    else:
         output_str += "\n]"

    #print(output_str)

    with open("testinput.py", "w") as input_ptr:
        driver_str =\
        "board = " + output_str

        input_ptr.write(driver_str)







