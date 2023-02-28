#Author: Aiden Sanghyeop Hyun
#260974945
 
def invert(num):
    
    
    ''' (str)->str
takes an image string as an input and invert 1s to 0s and 0s to 1s.
and return
 
>>> invert('1000100100')
'0111011011'
 
>>> invert('11110')
'00001'
 
>>> invert('020010')
'101101'
 
'''
    result = ''
    
    # image string goes through this for loop and makes
    
    # a new string that is inverted
    
    for i in num:
        
        if i == '0':
            result +='1'
        
        else:
            result +='0'
     
    
    return(result)
 
def total_pixel(height,width):
    '''(int,int) -> int
get the total number of pixel
 
>>> total_pixel(31,12)
372
 
>>>  total_pixel(1,12)
12
 
>>>  total_pixel(31,1)
31
'''
    return height*width  
 
    
def flip_horizontal(num, height, width):
    ''' (str, int, int)-> (str)
horizontally flips the image string and return
 
>>> flip_horizontal('111000111000',4,3)
'111000111000'
 
>>> flip_horizontal('123456789',3,3)
'321654987'
 
>>> flip_horizontal('185930375109',4,3)
'581039573901'
 
'''
    count = 0
    result =''
    pixel_num = int(total_pixel(height, width))
    
    #for loop limited to the number of heights
    
    #goes through each row and flips horizontally
    
    for i in range(height):
        
        row= num[count:count+width]
        
        count += width
        
        #flips the str
        
        result += row[::-1]
            
            
    return result     
    
    
    
def flip_vertical(num, height, width):
     '''(str, int, int)-> (str)
horizontally flips the image string and return
 
 
>>>flip_vertical('123456789',3,3)
'789456123'
 
>>> flip_vertical('011100',2,3)
'100011'
 
>>> flip_vertical('123456',2,3)
'456123'
 
'''
     pixel_num = int(total_pixel(height, width))
     
     count = 0
     
     result =''
     
     flipped=''
     
     
     for i in range(height):
         
         #slice the image string by the number of rows
         
         row = num[count:count+width]                      
         
         count += width
         
         #adds strings at the back that were in front before                                                                      
         
         flipped = row+flipped                                    
         
     return flipped
    
 
    
def crop(num, image_height,image_width, top_left_x, top_left_y, crop_height, crop_width):
    '''(str, int, int, int, int, int, int) -> str
 
cut out the image string of given infomation from the original image string
 
>>> crop('123456789',3,3,0,2,1,1)
'7'
 
>>> crop('123456789101',3,4,0,0,1,3)
'123'
 
>>> crop('123456789',3,3,0,0,1,1)
'1'
 
'''
    #identify the index where crop starts
    
    top_left_index = (image_width*top_left_y) + top_left_x     #counting from zero
    
    cropped = ''
    
    count = 0
    
    for i in range(int(crop_height)):
        
        #takes the cropped str and adds to object 'cropped'
        
        cropped += num[count+top_left_index:top_left_index+count+crop_width]
        
        # adds width value to the object so that the next row can be cropped with
        # top_left_index just by adding
        
        count += image_width
        
    return cropped
 
def find_end_of_repeated_substring(s,i,c):
    ''' (str, int, str) -> int
count the number of repeated letters and return the index
 
 
>>> find_end_of_repeated_substring('11111000000111111',6,'0')
10
 
>>> find_end_of_repeated_substring('Aiden Sanghyeop Hyun',0,'A')
0
 
>>> find_end_of_repeated_substring('aaaaaaabbbbbbbcccccccccccccc',15,'c')
27
 
'''
    
    count = 0
    
    current_letter = c
    
    #set to exit the while loop as soon as 'c' is a different letter
    
    while c == current_letter:
        
        current_letter = s[1+i+count:i+count+2]
        
        # if it is still the same letter adds 1 to 'count'
        
        if current_letter == c:
            
            count  +=  1
        
        #as soon as current letter becomes something else, it breaks the loop
            
        else:
            break
    
    
    return count+i
 
def compress(num):
    
    '''(str) ->str
takes an image string as an input and return the compressed image string.
 
>>> compress('111111000000001111111100000000')
'1 6 8 8 8'
 
>>> compress('10000100001011000010000101')
'1 1 4 1 4 1 1 2 4 1 4 1 1 1'
 
>>> compress('1')
'1 1'
 
'''
    count1 =0
    
    for i in num:
        
        # if the image string contains something other than 0 and 1
        #return an empty string
        
        if int(i) !=0 and int(i) !=1:
            return ''
    
    initial_num = num[0]
    
    empty_str = ' '
    
    result = num[0] + ' '
    
    #checks whether the number is same as the number before
    
    for i in num:
        
        #i is the current num
        
        #when it is the same number: add one to count1
        if i == initial_num:
            
            count1 += 1
         
         #when it is a different number: add the count to the object result
        
        else:
            result += (str(count1) + empty_str)
            
            initial_num = i
            
            #reset count1 to one
            
            count1 = 1
    
    #for the very last characters
    #add the string outside of the loop
    #without the empty string
            
    result += (str(count1))
    
    return result
            
 
    
<strong id=line-269 class="highlight-1063876">def decompress(compressed_num):
    ''' (str)-> str
 
takes a compressed image string and returns
the decompressed image string.
 
>>> decompress('1 3 5 3 1')
'111000001110'
 
>>> decompress('0 31 5 3 1')
'0000000000000000000000000000000111110001'
 
>>> decompress('1 3 5 3aads 1')
' '
'''
    empty_str = ' '
    
    result = ''
    
    initial_num = compressed_num[0]
    
    # string without the first number info with an additional
    #empty string at the end
    
    compressed_num = compressed_num[2:] +' '
    
    num_list = ['0','1','2','3','4','5','6','7','8','9',' ']
    
    answer= ''
    
    previous_a = 'a'
    
    #checks if there is a character that is not a number
    # or double spaced
    #return an empty string if that is the case
    
    for a in compressed_num:
        
        if a not in num_list:
            
            return empty_str
        
        if a == empty_str and previous_a == empty_str:
            
            return empty_str
        
        previous_a = a
    
    
    #decompressing part
        
    for a in compressed_num:
        
        #save the a value in an object
        if a != ' ':
            result += a
        
        #when there is an empty space
        #use the saved value 'a'
        #to decompress
        
        if a == ' ':
            #print(result)
            answer += (initial_num)*(int(result))
        
            #flip over binary number
            if initial_num == '0':
                initial_num = '1'
            
            elif initial_num == '1':
                initial_num = '0'
            
            #reset the object before next iteration
            result = ''
        
    
    return answer
 
 
            
    
 
<strong id=line-351 class="highlight-1063878">def process_command(command, image_str, height, width): 
        
    '''(str,str,int,int) -> str
 
returns the final image string after performing commands
 
>>> process_command('INV', '101001', 3, 2)
 
'010110'
 
>>> process_command('INV CR0,0,1,2', '010100010110', 3, 4)
 
'10'
 
>>> process_command('INV CR0,0,2,2 FH', '101001101101', 3, 4)
 
'0110'
 
'''
    
    num_list = ['0','1','2','3','4','5','6','7','8','9']
    
    result = ''
    
    image = image_str
    
    len_command = len(command)
    
    command_2 = command +' '
    
    cr_int = ''
    
    count = 0
    
    cr_command_count =0
    
    input_cr = ''
    
    #interpret commands
    
    for a in command_2:
        
        #save the string until it becomes a command
        
        if a != ' ':
            result += a
        
        #perform the command when there is a space
        #in the string
            
        if a == ' ':
        
            if result == 'INV':
                
                image = invert(image)
 
            if result =='FH':
                
                image =  flip_horizontal(image, height, width)
            
            if result =='FV':
                
                image = flip_vertical(image,height, width)
                            
            if result =='DC':
                
                image = decompress(image)
            
            if result =='CP':
                
                image = compress(image)
            
            #CR can only be more than len 6 with an empty string at the end
                
            elif len(result) >6:
                
                #add a comma at the end
                #so that the last int can safely assigned 
                result = result + ','
                
                for x in result:
                    
                    if x == 'C' or x == 'R':
                        
                        continue
                    
                    if x in num_list:
                        
                        input_cr += x
                    
                    #when there is a comma, assign the number
                        
                    elif x == ',':
                        
                        count += 1
                        
                        if count == 1:
                            
                            top_left_x = int(input_cr)
                            input_cr = ''
                        
                        if count ==2:
                            
                            top_left_y = int(input_cr)
                            input_cr = ''
                        
                        if count ==3:
                            
                            crop_height =int(input_cr)
                            input_cr = ''
                            
                        if count ==4:
                            crop_width = int(input_cr)
                            
                            #perfom crop function right away
                            
                            image = crop(image, height,width, top_left_x, top_left_y, crop_height, crop_width)
            
            #clear out the current command
                            
            result = ''
            
    return image
    
        
    
    
        
    
    
    
        
        
        
        
        
    
    
    
 
 
 
 
   
    
    
    
    
        
    
    
    
    
    
    
    
    
    
        
        
        
         
         
    
        
        
            
    
    
    
    
    
    
    
