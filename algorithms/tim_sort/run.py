class Run:
    def __init__(self, start_index = None, size = None):
        self.start_index = start_index
        self.size = size

    def __str__(self):
        return f"start_index={self.start_index} size={self.size}"

    def get_start_index(self):
        return self.start_index

    def get_size(self):
        return self.size