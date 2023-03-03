# import required module
import os
# assign directory
path_of_the_directory = '/home/ec2-user/environment' #file or folder path

 
# iterate over files in
# that directory
for filename in os.listdir(path_of_the_directory):
    file = os.path.join(path_of_the_directory,filename)
    if os.path.isfile(file):
        with open(file) as f:
            lines = f.readlines()
            data = ''.join(lines)
            print('')
            print('File Name =',f.name)
            print('lines =',len(lines))
            print('Words = ',len(data.split()))
            data = ''.join(data.split())
            print('characters = ',len(data))
            print('')
                #read the content of file
        #data = f.read()

        #get the length of the data
        #number_of_characters = len(data)

        #print('Number of characters in text file :', number_of_characters)
        #print(f)
