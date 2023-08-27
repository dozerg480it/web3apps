from skimage import io, color, feature

def extract_image_features(image_path):
    try:
        # Load the image
        image = io.imread(image_path)

        # Convert the image to grayscale
        gray_image = color.rgb2gray(image)

        # Calculate the Histogram of Oriented Gradients (HOG) feature
        hog_feature = feature.hog(gray_image, visualize=False)

        print("HOG feature vector:")
        print(hog_feature)

    except Exception as e:
        print(f"An error occurred: {e}")

# Provide the path to the image you want to extract features from
image_path = "picture.jpg"
extract_image_features(image_path)
