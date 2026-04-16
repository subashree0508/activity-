class MedianFinder:
    def __init__(self):
        self.data = []
    def addNum(self, num):
        self.data.append(num)
        self.data.sort()
    def findMedian(self):
        n = len(self.data)
        mid = n // 2
        if n % 2 == 0:
            return (self.data[mid - 1] + self.data[mid]) / 2
        else:
            return self.data[mid]
mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
print(mf.findMedian())
mf.addNum(3)
print(mf.findMedian())
