# --------------
##File path for the file 
file_path
def read_file(path):
    file = open(path,'r')
    sentence=file.readline()
    file.close()
    return sentence
sample_message=read_file(file_path)
print(sample_message)
#Code starts here


# --------------
#Code starts here

#Function to fuse message
def fuse_msg(message_a,message_b):
    
    #Integer division of two numbers
    quot=(int(message_b)//int(message_a))
    
    #Returning the quotient in string format
    return str(quot)

#Calling the function to read file  
message_1=read_file(file_path_1)
print(message_1)
#Calling the function to read file
message_2=read_file(file_path_2)

#Calling the function 'fuse_msg'
secret_msg_1=fuse_msg(message_1,message_2)

#Printing the secret message 
print(secret_msg_1)

#Code ends here


# --------------
#Code starts here
#call function substitute message
def substitute_msg(message_c):
    if message_c == 'Red':
       sub='Army General'
   
    elif message_c =='Green':
         sub='Data Scientist'
      
    elif message_c== 'Blue' :
         sub='Marine Biologist'
#returning substitute of message
    return(sub)  
#call function for read file for message_3
message_3 = read_file(file_path_3)
print(message_3)

#call function substitute_msg()
secret_msg_2=substitute_msg(message_3)



# --------------
# File path for message 4  and message 5
file_path_4
file_path_5

#Code starts here
message_4= read_file(file_path_4)
message_5= read_file(file_path_5)

print(message_4)
print(message_5)

#call for function compare_msg()
def compare_msg(message_d,message_e):
    a_list = message_d.split()
    b_list = message_e.split()
    c_list = [i for i in  a_list if i not in b_list]
    final_msg=" ".join(c_list)
    return final_msg

secret_msg_3 = compare_msg(message_4,message_5)
print(secret_msg_3)





# --------------
#Code starts here
message_6= read_file(file_path_6)
print(message_6)

#define function extract_msg

def extract_msg(message_f):
    a_list=message_f.split()
    even_word = lambda x:(len(x)%2 == 0)
    b_list= list(filter(even_word,a_list))
    final_msg= " ".join(b_list)
    return(final_msg)

#call for function extract_msg
secret_msg_4 =extract_msg(message_6)
print(secret_msg_4)




# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]


final_path= user_data_dir + '/secret_message.txt'

#Code starts here

 #combine the list message parts into single sentence
secret_msg = " ".join(message_parts)

 #define function write file
def write_file(secret_msg,path):
    file= open(path,'a+')
    file.write(secret_msg)
    file.close()

#CALL THE FUNCTION OF WRITE FILE
write_file(secret_msg, final_path)
print(secret_msg)



