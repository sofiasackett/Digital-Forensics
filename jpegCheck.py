# Sofia Sackett
# CFRS 510
# 18 April 2020

def main():
    import os
    import binascii
    import time

    ''' Get user input for directory of interest. '''
    try:
        user_input = input("Enter the complete path to the directory you want investigated: ")
        assert os.path.exists(user_input)
    except:
        print("The directory you are looking for cannot be found at that location.")

    ''' Define JPEG using magic numbers and create output text file. '''
    jpeg_header = binascii.unhexlify(b'FFD8')
    jpeg_footer = binascii.unhexlify(b'FFD9')
    output = open("Sackettoutput.txt", "w+")

    ''' Traverse directory and open each file. '''
    for root, dirs, files in os.walk(user_input):
        for name in files:
            with open(os.path.join(root, name), 'rb') as f:
                
                # Save the first and last two bytes of each file
                header_contents = f.read(2)
                footer_contents = f.read()[-2]
                
                # Analyze each file and look only at files with JPEG headers
                if header_contents in jpeg_header:

                    ''' Begin by looking only at files without appended data. '''
                    if footer_contents not in jpeg_footer:
                        appended = True
                        with open (os.path.join(root, name), 'rb') as f:
                            file = str(os.path.join(root, name))
                            whole_file = f.read()

                            # Find the location of the JPEG footer
                            footer_bytes = whole_file.find(jpeg_footer)

                            # Add 2 bytes to exclude footer from appended data
                            appended_start = int(footer_bytes) + 2

                            # Separate the original file from the appended data
                            appended_data = whole_file[appended_start:]
                            original_file = whole_file[:appended_start]

                            md5_hash = md5HashFunc(appended, original_file)
                            
                            m_time = os.path.getmtime(file) 
                            a_time = os.path.getatime(file)
                            c_time = os.path.getctime(file)

                            decoded_message = b64decode(appended_data)

                            ''' Save all collected data to a dictionary and write it to Sackettoutput.txt. '''
                            appended_dict = {
                                'Filename': file,
                                'Last content modification time': m_time,
                                'Last accessed time': a_time,
                                'Inode modified time': c_time,
                                'MD5 Hash': md5_hash,
                                'Decoded message': decoded_message
                                }
                            
                            output.write(str(appended_dict))
                            output.write("\n")

                    #Now look at files that do not have any appended data.
                    elif footer_contents in jpeg_footer:
                        appended = False
                        file = str(os.path.join(root, name))
                        md5_hash = md5HashFunc(appended, file)

                        m_time = os.path.getmtime(file) 
                        a_time = os.path.getatime(file)
                        c_time = os.path.getctime(file)

                        ''' Save all collected data to a dictionary and write it to Sackettoutput.txt. '''
                        unappended_dict = {
                            'Filename': file,
                            'Last content modification time': m_time,
                            'Last accessed time': a_time,
                            'Inode modified time': c_time,
                            'MD5 Hash': md5_hash,
                            'Decoded message': 'N/A'
                            }

                        output.write(str(unappended_dict))
                        output.write("\n")

    ''' Print path to output text file and the time the script finishes executing. '''
    print("Sackettoutput.txt can be found at " + os.path.abspath("Sackettoutput.txt"))
    current_time = time.strftime("%H:%M:%S %p on %m-%d-%Y", time.localtime())
    print("Script completed: " + current_time)


''' b64decode  ecodes the appended data assuming base64 encoding. '''
def b64decode(data):
    import base64
    decoded_message = base64.b64decode(data)
    return decoded_message


''' md5HashFunc hashes the original file minus any appended data.
The function takes in appended (a Boolean value where True means that there is appended data)
and file, which represents the content to be hashed.'''
def md5HashFunc(appended, file):
    import hashlib
    if appended == False:
        # Read only 65K bytes at a time as a block
        block = 65000 
        file_hash = hashlib.md5()

        # Open the file and read block by block 
        with open(file, 'rb') as md5_f: 
            file_block = md5_f.read(block)

            # Update hash block by block as long as there are bytes left to read
            while len(file_block) > 0:    
                
                file_hash.update(file_block) 
                file_block = md5_f.read(block) 

        md5_hash = file_hash.hexdigest()
        return md5_hash
       
    elif appended == True:
        md5_hash = (hashlib.md5(file)).hexdigest()
        return md5_hash


if __name__ == '__main__':
    main()














