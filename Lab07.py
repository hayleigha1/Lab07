def get_mpg ():

    while True:
        try:

            min_mpg = int(input("Enter the minimum mpg ==> "))

            if (min_mpg <= 0):

                print("Fuel economy given must be greater than 0")


            elif (min_mpg >= 100):

                print("Fuel economy must be less than 100")

            else:
                return True

        except ValueError:

            print("You must enter a number for the fuel economy")

def get_inputfile():

    while True:

        try:

            user_inputfile = input("Enter the name of the input vehicle file ==> ")
            fileinput = open(user_inputfile)
            break

        except FileNotFoundError:
            
            print("Could not open file ",user_inputfile)

            
def get_outputfile(mpg, file):

    while True:

        try:

            user_outputfile = input("Enter the name of the file to output to ==> ")
            with open(user_outputfile, 'w') as write_file:
                for data in file:
                    try:
                        if mpg >= float(data[7])
                        write_file.write('
        
        except (IOError, OSError):
            
            print("There is an IO Error ",fileoutput)

def 

'''main'''
mpg = get_mpg()   
file = get_inputfile()
final = get_outputfile(mpg, file)





            
        
        
    

        

            

        

        

        
        

        
        


    

        
        
        
    
