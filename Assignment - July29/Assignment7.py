def find_extensions(filenames):
    extensions = []

    files = filenames.split(",")

    for file in files:
        file = file.strip()

        if "." in file:
            extension = file.split(".")[-1].upper()

            if extension not in extensions:
                extensions.append(extension)

    return extensions


filenames = "report.pdf, image.JPG, data.csv, notes.txt, photo.jpg"

print(find_extensions(filenames))