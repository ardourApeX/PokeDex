import os
import shutil

def create_folders(folders = ['Aerodactyl', 'Bulbasaur', 'Charmander', 'Dratini', 'Fearow', 'Meowth', 'Pikachu', 'Psyduck', 'Spearow', 'Squirtle'], parent_dir = "./dataset/"):
     
    # If the separation already exists
    if os.path.isdir(parent_dir + "/validation"):
        print("Separation has been done already! ")
        return
    
    # If not create a validation folder
    else:
        os.mkdir(parent_dir + "/validation")

	    # Now create a seperate folder for each label
	    for label in folders:
	        os.mkdir(parent_dir + "/validation/" + label)

	    SPLIT = 0.9 # spliting data into 90:10 
	        
	        # Load all images from training data and make a split
	    for image_folder in folders:
	        
	        Path = parent_dir + "/train/" + image_folder # Inside each training class folder
	        images = os.listdir(Path)# List all the images
	        split_size =  int(SPLIT * len(images))

	        images_to_move = images[split_size :] # Train-Test split
	        #print(len(images_to_move))
	        for validation_image in images_to_move:
	            src = os.path.join(Path, validation_image) 
	            dest = os.path.join(parent_dir + "/validation/" + image_folder, validation_image)
	            shutil.move(src, dest) # Moving selected images
	    print("Separation done successfully!")
	    return

create_folders()