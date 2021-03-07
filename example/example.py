import nsipptparser
import json

with open("sneaky.nsippt") as file:
    data = nsipptparser.parse(file)
    # Get the first length measurement of the first View
    length = data["ViewPropertiesSet"]["View Properties"][0]["Actions Set"]["Length"][0]["length value"]
    print("The length is ", length)

    # Get the base64 thumbnail of the first View
    thumbnail = data["ViewPropertiesSet"]["View Properties"][0]["Thumbnail"]
    print("The thumbnail is ", thumbnail)

    # Save to json file
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)
    