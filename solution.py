import hashlib
def welcome_assignment_answers(question):

    #test
    if question == "Are encoding and encryption the same? - Yes/No":
        answer ="No"
    elif question ==  "Is it possible to decrypt a message without a key? - Yes/No":
        answer ="No"
    elif question ==  "Is it possible to decode a message without a key? - Yes/No":
        answer ="Yes"
    elif question ==  "Is a hashed message supposed to be un-hashed? - Yes/No":
        answer ="No"
    elif question ==  "What is the MD5 hashing value to the following message: 'NYU Computer Networking' - Use MD5 hash generator and use the answer in your code":
        s='NYU Computer Networking'
        result = hashlib.md5(s.encode('utf-8'))
        answer=result.hexdigest()
    elif question ==  "Is MD5 a secured hashing algorithm? - Yes/No":
        answer ="No"
    elif question == "What layer from the TCP/IP model the protocol DHCP belongs to? - The answer should be a numeric number":
        answer =5
    elif question ==  "What layer of the TCP/IP model the protocol TCP belongs to? - The answer should be a numeric number":
        answer = 4         
    return (answer)         

if __name__ == "__main__":
    debug_question = "What layer of the TCP/IP model the protocol TCP belongs to? - The answer should be a numeric number"
    print(welcome_assignment_answers(debug_question))

    



 
 
 
 


