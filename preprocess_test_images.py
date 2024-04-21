import os
import glob
import cv2
import random
import numpy as np

# Parameters 

dry_run = False # If true, will print output directory.

input_path = '/Users/ayush/Documents/Github/lego_id_training_data/data/'
output_path = '/Users/ayush/Documents/Github/lego_id_training_data/output_grayscale/'
show_image = False

train_test_split = 0.3
shuffle_split = False

part_numbers = [
                  '2456',
                  #'3001',
                  #'3002',
                  #'3003',
                  #'3004',
                  #'3010',
                  #'3039',
                  #'3660',
                  #'3701',
                  #'32064'
               ]

for part_number in part_numbers:

    part_input_path  = f'{input_path}{part_number}/'
    
    # Get input file paths.
    image_files = glob.glob(f'{part_input_path}*.jpg')
    num_files = len(image_files)

    # Image index.
    index = 0

    # If true, the images will be loaded and then split at random.
    if shuffle_split:
        file_index = random.sample(range(1, num_files), num_files- 1)
    else:
        file_index = range(1, num_files)


    for file_num in file_index:
         
         # Increment the file index.
         index += 1
         print(file_num)
         # Load the image
         input_file_path = f'{input_path}{part_number}/{part_number}_{str(file_num)}.jpg'
         print(f'LOADED: {input_file_path}')
         
         # Resize image
         #If enlarging image, use interpolation = cv2.INTER_LINEAR or INTER_CUBIC
         #If shrinking image, use interpolation = cv2.INTER_AREA
         img = cv2.imread(input_file_path)

         #Gray scale image
         img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
         #print(np.shape(img))
         #print(img)

         # Show to user.
         if show_image:
               cv2.imshow('image', img)
               cv2.waitKey(0)
               cv2.destroyAllWindows() 

         # Determine if it should be output to train or test.
         test_or_train = 'train'        
         if index < int(num_files * 0.1): 
               test_or_train = 'test'
         elif index < int(num_files * 0.4): 
               test_or_train = 'val'
         
         # Prepare the output folder.
         part_output_folder = f'{output_path}{test_or_train}/{part_number}/'
               
         # Make the output directory, if it doesn't exist.
         if not os.path.exists(part_output_folder):
               os.makedirs(part_output_folder)

         # Create part path.
         part_image_path = f'{part_output_folder}{part_number}_{index}.jpg'
         
         # Output
         if dry_run:
               print(f'Would have saved to: {part_image_path}')
         else:
               print(f'SAVED: {part_image_path}')
               cv2.imwrite(part_image_path, img)