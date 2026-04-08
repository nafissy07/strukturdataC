class CircularQueue:
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.front = -1
        self.rear = -1

    def enqueue(self, value):
        if (self.rear + 1) % self.k == self.front:
            return False  # Antrean penuh

        elif self.front == -1:  # Kondisi antrean kosong
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = value
        else:
            # Geser rear dengan modulo dan masukkan nilai
            self.rear = (self.rear + 1) % self.k
            self.queue[self.rear] = value
        return True

    def dequeue(self):
        if self.front == -1:  # Kondisi antrean kosong
            return "Queue is Empty"

        data = self.queue[self.front]

        if self.front == self.rear:
            # Ini adalah elemen terakhir, jadi kita reset
            self.front = -1
            self.rear = -1
        else:
            # Geser front maju satu langkah dengan modulo
            self.front = (self.front + 1) % self.k

        return data
