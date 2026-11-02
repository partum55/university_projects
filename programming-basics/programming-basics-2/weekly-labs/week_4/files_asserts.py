from files import File, TextFile, VideoFile, Disk

def test_files():
    # Creating a file and checking attributes
    file = File.create("file.abc", "2.0")
    assert file.name == "file.abc"
    assert file.path == ""
    # File size in megabytes
    assert file.size == 2.0
    assert str(file) == f"File: {file.path}/{file.name} ({file.size:.2f} MB)"

    # Creating a text file and checking attributes
    text_file = TextFile("notes.txt", "This is a test text.")
    assert text_file.file.name == "notes.txt"
    assert text_file.file.path == ""
    assert text_file.content == "This is a test text."
    # File size in megabytes assuming 1 character is 2 bytes
    assert text_file.file.size == len("This is a test text.") * 2 / 1000000
    assert text_file.file.size > 0
    assert str(text_file) == (
        f"TextFile: {text_file.file.path}/{text_file.file.name} "
        f"({text_file.file.size:.2f} MB)")

    # Compressing the text file and checking attributes
    text_file.compress()
    assert text_file.file.size < len("This is a test text.") * 2 / 1000000

    # Creating a video file and checking attributes
    video_file = VideoFile("movie.mp4", 12, "720p")
    assert VideoFile.QUALITY_SIZES == {"480p": 25, "720p": 50, "1080p": 100}
    assert video_file.file.name == "movie.mp4"
    assert video_file.file.path == ""
    assert video_file.duration == 12
    assert video_file.quality == "720p"
    assert video_file.file.size == 12 * 50  # 720p = 50MB per minute
    assert str(video_file) == (
        f"VideoFile: {video_file.file.path}/{video_file.file.name} "
        f"({video_file.file.size:.2f} MB)")

    # Creating a disk
    # Disk is empty
    disk = Disk("SSD")
    assert Disk.capacity == 1
    assert disk.free_space == 1
    assert disk.used_space == 0
    assert len(disk.files) == 0
    assert disk.name == "SSD"
    assert str(disk) == "Disk: SSD (0.00/1 GB used)"

    # Adding a text file to the disk and checking attributes
    assert disk.add_file(text_file, "/Documents") == str(disk)
    assert text_file.file.path == "/Documents"
    assert disk.used_space > 0
    assert disk.free_space < 1
    assert len(disk.files) == 1
    assert text_file.file.name in disk.files["/Documents/notes.txt"].file.name

    # Adding a video file to the disk and checking attributes
    assert disk.add_file(video_file, "/Videos") == str(disk)
    assert video_file.file.path == "/Videos"
    assert disk.used_space > video_file.file.size / 1024
    assert disk.free_space < 1
    assert len(disk.files) == 2
    assert video_file.file.name in disk.files["/Videos/movie.mp4"].file.name

    # Adding a large file and checking constraints
    large_text_file = TextFile("large_notes.txt", "Text" * 107374183)
    assert large_text_file.file.name == "large_notes.txt"
    # File size is larger than available space on the disk
    assert large_text_file.file.size > disk.free_space * 1024  
    assert disk.add_file(large_text_file, "/Documents") == (
        f"Not enough space on {disk.name} for {large_text_file.file.name}")

    # Ensuring there is still space on the disk and compressing the file
    assert disk.used_space <= 1
    large_text_file.compress()

    # Retrying to add the compressed file
    if disk.free_space >= large_text_file.file.size / 1024:
        assert disk.add_file(large_text_file, "/Documents") == str(disk)
        assert large_text_file.file.path == "/Documents"

    # Ensuring there is still space on the disk
    assert disk.used_space <= 1

    # Adding an identical text file and checking for duplication
    text_file = TextFile("notes.txt", "This is a test text.")
    identical_text_file = TextFile("notes.txt", "This is a test text.")

    # Files are compared by name, size, and content
    assert identical_text_file == text_file  
    not_identical_text_file = TextFile("notes.txt", "This is a cute text.")
    assert not_identical_text_file != text_file
    assert disk.add_file(text_file, "/Notes") == str(disk)
    # Message that the file already exists
    assert disk.add_file(identical_text_file, "/Notes") == (
        f"File {identical_text_file.file.name} already exists on {disk.name}")  
    assert len(disk.files) == 3  # Number of files has not changed
    assert disk.add_file(not_identical_text_file, "/Documents") == str(disk)
    # Number of files has not changed because the file was overwritten by another file
    assert len(disk.files) == 3  

    print("All tests passed.")

if __name__ == "__main__":
    test_files()