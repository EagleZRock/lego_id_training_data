import os
import glob
import cv2
import random

# Parameters 

dry_run                 = False # If true, will print output directory.

root_path               = '/Users/ayush/Documents/GitHub/LEGO-Sorter/data/'
input_path              = f'{root_path}raw/'
output_path             = f'{root_path}processed/'

show_image              = False

output_img_size         = (300, 300)
grab_area               = 500
train_test_split        = 0.3
shuffle_split           = True

part_numbers            = [
                           '3001',
                           '3003',
                           '3004',
                           '3005',
                           '3010',
                           '3020',
                           '3021',
                           '3022',
                           '3039',
                           '3040',
                           '3710',
                           '6091',
                           '44728',
                           '60470',
                           '85984'
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
        file_index = random.sample(range(1, num_files), num_files - 1)
    else:
        file_index = range(1, num_files)

for file_num in file_index:
        
        # Increment the file index.
        index += 1
        
        # Load the image
        input_file_path = f'{input_path}{part_number}/{str(file_num).zfill(4)}.jpg'
        print(f'LOADED: {input_file_path}')
        
        # Crop raw image from center.
        img = cv2.imread(input_file_path)

        # Get the center of the image.
        c_x, c_y = int(img.shape[0] / 2), int(img.shape[1] / 2)
        img = img[c_y - grab_area: c_y + grab_area, c_x - grab_area: c_x + grab_area]
         
        # Resize image
        img = cv2.resize(img, output_img_size, interpolation = cv2.INTER_AREA)
        
        # Should we convert it to grayscale?
        if gray_scale:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Show to user.
        if show_image:
            cv2.imshow('image', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows() 

        # Determine if it should be output to train or test.
        test_or_train = 'train'        
        if index < int(num_files * train_test_split): 
            test_or_train = 'test'
        
        # Prepare the output folder.
        color = ''
        if gray_scale:
            part_output_folder = f'{output_path}gray_scale/{test_or_train}/{part_number}/'
        else:
            part_output_folder = f'{output_path}color/{test_or_train}/{part_number}/'
            
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