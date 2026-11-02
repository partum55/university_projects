"""
File worker
"""


class File:
    """Represents a basic file with a name, size, and path."""

    def __init__(self, name: str, size: float):
        self.name = name
        self.size = size
        self.path = ""

    @classmethod
    def create(cls, name: str, size: str):
        """
        Creates a file from string size.

        :param name: Name of the file
        :param size: Size of the file as a string
        :return: Instance of File
        """
        return cls(name, float(size))

    def __str__(self):
        return f"File: {self.path}/{self.name} ({self.size:.2f} MB)"


class TextFile:
    """Represents a text file with content and supports compression."""

    def __init__(self, name: str, content: str):
        self.file = File(name, len(content) * 2 / 1000000)
        self.content = content

    def compress(self):
        """
        Compresses the text file, reducing its size by 50%.
        """
        self.file.size *= 0.5

    def __str__(self):
        return f"TextFile: {self.file.path}/{self.file.name} ({self.file.size:.2f} MB)"

    def __eq__(self, other):
        """
        Compares two TextFile objects.

        :param other: Another TextFile object
        :return: True if the files have the same name and content, False otherwise
        """
        return (
                isinstance(other, TextFile) and
                self.file.name == other.file.name and
                self.content == other.content
        )


class VideoFile:
    """Represents a video file with different quality levels and durations."""

    QUALITY_SIZES = {"480p": 25, "720p": 50, "1080p": 100}

    def __init__(self, name: str, duration: int, quality: str):
        self.file = File(name, duration * self.QUALITY_SIZES[quality])
        self.duration = duration
        self.quality = quality

    def __str__(self):
        return f"VideoFile: {self.file.path}/{self.file.name} ({self.file.size:.2f} MB)"


class Disk:
    """Represents a disk with storage capacity and file management functionality."""
    capacity = 1

    def __init__(self, name: str):
        self.name = name
        self.files = {}
        self.used_space = 0

    @property
    def free_space(self):
        """
        Returns the remaining free space on the disk in GB.

        :return: Free space in GB
        """
        return self.capacity - self.used_space

    def add_file(self, file, path: str):
        """
        Adds a file to the disk at the specified path.

        :param file: File object to be added
        :param path: Directory path where the file should be stored
        :return: String message about the operation success or failure
        """
        file_path = f"{path}/{file.file.name}"
        if file.file.size / 1024 > self.free_space:
            return f"Not enough space on {self.name} for {file.file.name}"
        if file_path in self.files:
            if self.files[file_path] == file:
                return f"File {file.file.name} already exists on {self.name}"
            else:
                self.used_space -= self.files[file_path].file.size / 1024
                self.files[file_path] = file
                self.used_space += file.file.size / 1024
                return str(self)
        file.file.path = path
        self.files[file_path] = file
        self.used_space += file.file.size / 1024
        return str(self)

    def __str__(self):
        return f"Disk: {self.name} ({self.used_space:.2f}/{self.capacity} GB used)"
