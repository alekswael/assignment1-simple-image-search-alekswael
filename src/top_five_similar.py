# importing packages
import argparse
import os
import cv2
import pandas as pd
import warnings # For ignoring warnings.
warnings.filterwarnings("ignore") # Ignore warnings.

def input_parse(): # Function to parse command line arguments.
    # initialize the parser
    parser = argparse.ArgumentParser()
    # add arguments
    parser.add_argument("--folder", help="Name of image-containing folder located in the data folder", type=str, default="flowers")
    parser.add_argument("--image", help="Name of the image you want to compare to the rest of the images in the folder", type=str, default="image_0001.jpg")
    # parse the arguments from the command line
    args = parser.parse_args()
    # get the name
    return args


# Define a particular image that you want to work with
def top_five_similar(folder, image): # image_name is a name (string) of an image which is located in the data/flowers folder
    
    path_to_folder = os.path.join(os.getcwd(), "data", folder)
    
    # First I create the empty df that I want to fill
    df = pd.DataFrame(columns = ["Filename", "Distance"])
    
    # I then read in the input/target image
    target_image = cv2.imread(os.path.join(path_to_folder, image))
    
    # I then extract the colour histogram with OpenCV. All colour channels, no mask, full scale, normal range.
    hist_target = cv2.calcHist([target_image], [0,1,2], None, [256,256,256], [0,256, 0,256, 0,256])
    
    # I then normalize then values of the histogram because it makes interpretation of the histogram comparisons easier.
    hist_target = cv2.normalize(hist_target, hist_target, 0, 1.0, cv2.NORM_MINMAX)
    
    # Here I loop over all images in the flowers folder.
    for other_name in os.listdir(path_to_folder):
        
        # I read the image
        other_image = cv2.imread(os.path.join(path_to_folder, other_name))
        
        # I then extract the colour histogram with OpenCV. All colour channels, no mask, full scale, normal range.
        hist_other = cv2.calcHist([other_image], [0,1,2], None, [256,256,256], [0,256, 0,256, 0,256])
        
        # I normalize this histogram as well.
        hist_other = cv2.normalize(hist_other, hist_other, 0, 1.0, cv2.NORM_MINMAX)
        
        # Here is where the comparison happens. I round the distance value to include 2 decimals.
        distance_value = round(cv2.compareHist(hist_target, hist_other, cv2.HISTCMP_CHISQR), 2)
        
        # I then make a new row for the data frame, containing the name of the compared image and the distance value.
        new_row = {"Filename": other_name, "Distance": distance_value}
        
        # If the comparison image is the target image, then I change the other_name variable to "target" so I can easily find it in the dataframe.
        if other_name == image:
            new_row["Filename"] = "target"
        
        # I am now ready to append the completed row to the dataframe.
        # Yeeeees I know frame.append is deprecated, but it's great.
        df = df.append(new_row, ignore_index=True)
    
    # The dataframe now consists of 1360 rows and 3 columns.   
    # I only need the 5 most similar images. These have the lowest distance value.
    # Because the target image is compared with itself (distance_value = 0), I want the df to consist of 6 rows.
    df = df.nsmallest(6, "Distance")
    
    # The df is now complete and I want to save it.
    # I rename the file, adding target_ before the filename, removing .jpg and adding .csv
    my_csv = "target_" + image.replace(".jpg", "") + ".csv"
    df.to_csv(os.path.join(os.getcwd(), "out", my_csv))
    
    # To view quickly I print the df as well.
    print(df)
    
    # And that is the function done!


# Define main function

def main():
    args = input_parse()
    top_five_similar(args.folder, args.image)

if __name__ == "__main__":
    main()