from google.cloud import vision
import io

def detect_objects(image_path):
    # Instantiate a client
    client = vision.ImageAnnotatorClient()

    # Open the image file
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    # Prepare the image for Vision API
    image = vision.Image(content=content)

    # Perform object localization (detection) on the image
    response = client.object_localization(image=image)

    # Check if the response is successful
    if response.error.message:
        raise Exception(f'Error: {response.error.message}')
    
    # Print out the detected objects and their bounding boxes
    print("Objects detected in the image:")
    for obj in response.localized_object_annotations:
        print(f"Object: {obj.name}")
        print(f"Confidence: {obj.score:.2f}")
        print(f"Bounding box: {obj.bounding_poly}")
        print('-' * 50)

if __name__ == "__main__":
    # Path to your image file
    image_path = "foodimage.jpg"
    
    # Detect objects in the image
    detect_objects(image_path)
