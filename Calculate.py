import sqlite3
import math

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
adj_close = []
volume = []
def media (l):
    return sum(l)/len(l)

def median(l):
    sortedList = sorted(l)
    indexMedian = (len(l)-1)//2

    if (len(l) % 2):
        return sortedList[indexMedian]
    else:
        return (sortedList[indexMedian] + sortedList[indexMedian + 1])/2.0
    
def standardDeviation(l):
    mediaNumber = media(l)
    squares = []
    for n in l:
        squares.append((n - mediaNumber)**2)
    return math.sqrt((1/(len(l) - 1))*sum(squares))

for row in cursor.execute("SELECT adj_close, volume FROM actions"):
    adj_close.append(row[0])
    volume.append(row[1])

media_adj_close = media(adj_close)
media_volume = media(volume)

print("Media of ajust close %.2f " % media_adj_close)
print("Media of volume %.2f " % media_volume)

median_adj_close = median(adj_close)
median_volume = median(volume)

print("Median of ajust close %.2f " % median_adj_close)
print("Media of volume %.2f " % median_volume)

sd_adj_close = standardDeviation(adj_close)
print("Standard Deviation of ajust close %.2f " % sd_adj_close)
sd_volume = standardDeviation(volume)
print("Standard Deviation of volume %.2f " % sd_volume)

print("Range of ajust close is [%.2f, %.2f]" % (min(adj_close), max(adj_close)))
print("Range of volume [%.2f, %.2f]" % (min(volume), max(volume)))