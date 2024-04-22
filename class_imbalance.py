import os
import glob
import cv2
import random
import numpy as np

# Parameters 

dry_run = False # If true, will print output directory.

input_path = '/Users/ayush/Documents/Github/lego_id_training_data/data/'
#output_path = '/Users/ayush/Documents/Github/lego_id_training_data/output_grayscale/'
show_image = False

train_test_split = 0.3
shuffle_split = False

part_numbers = [
                  '2456',
                  '3001',
                  '3002',
                  '3003',
                  '3004',
                  '3010',
                  '3039',
                  '3660',
                  '3701',
                  '32064'
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
    
    count = 0
    while index < 800:
         index += 1
         count += 1
         # Create part path.
         file_index = random.sample(range(1, num_files), num_files- 1)
         original_image_path = f'{input_path}{part_number}/{part_number}_{file_index}.jpg'
         img = cv2.imread(input_file_path)
         part_image_path = f'{input_path}{part_number}/{part_number}_{index}.jpg'
         cv2.imwrite(part_image_path, img)

         if(count >= num_files):
             count = 0