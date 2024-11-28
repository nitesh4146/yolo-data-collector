import os

data_dir = "/Users/nitish/Downloads/Household-small-objects-5.v1i.yolov11/all/"

# List all files in the data directory
files = os.listdir(data_dir)

# Filter out directories
image_files = [f for f in files if os.path.isfile(os.path.join(data_dir, f))]

# from each remove everything after "_jpg"
image_files = [f.split("_jpg")[0] for f in image_files]
print(image_files)