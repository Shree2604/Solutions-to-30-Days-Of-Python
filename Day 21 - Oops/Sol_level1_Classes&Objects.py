# Level 1
# Python has the module called statistics and we can use this module to do all the statistical calculations.
# However, to learn how to make a function and reuse it, let's try to develop a program that calculates the measure of central tendency of a sample
# (mean, median, mode) and measure of variability (range, variance, standard deviation).
# In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample.
# You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class.
# Check the output below.
# ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]


import statistics

class Statistics:
    def __init__(self, data):
        self.data = data

    def count(self):
        return len(self.data)

    def sum(self):
        return sum(self.data)

    def min(self):
        return min(self.data)

    def max(self):
        return max(self.data)

    def range(self):
        return max(self.data) - min(self.data)

    def mean(self):
        return statistics.mean(self.data)

    def median(self):
        return statistics.median(self.data)

    def mode(self):
        return statistics.multimode(self.data)

    def std(self):
        return statistics.stdev(self.data)

    def var(self):
        return statistics.variance(self.data)

    @staticmethod
    def _counts(data):
        counts = {}
        for value in data:
            if value not in counts:
                counts[value] = 0
            counts[value] += 1
        return sorted(counts.items())

    def freq_dist(self):
        return Statistics._counts(self.data)

    def describe(self):
        description = f"Count: {self.count()}\n"
        description += f"Sum: {self.sum()}\n"
        description += f"Min: {self.min()}\n"
        description += f"Max: {self.max()}\n"
        description += f"Range: {self.range()}\n"
        description += f"Mean: {self.mean()}\n"
        description += f"Median: {self.median()}\n"
        description += f"Mode: {self.mode()}\n"
        description += f"Standard Deviation: {self.std()}\n"
        description += f"Variance: {self.var()}\n"
        description += f"Frequency Distribution: {self.freq_dist()}"
        return description


ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

data = Statistics(ages)

# Output for Level 1
print('Count:', data.count()) #25
print('Sum:', data.sum()) #744
print('Min:', data.min()) #24
print('Max:', data.max()) #38
print('Range:', data.range()) #14
print('Mean:', data.mean()) #29.76
print('Median:', data.median()) #29
print('Mode:', data.mode()) #[26]
print('Standard Deviation:', data.std()) #4.2747319604079665
print('Variance:', data.var()) #18.273333333333333
print('Frequency Distribution:', data.freq_dist())
#[(24,2),(25,1),(26,5),(27,4),(29,1),(31,2),(32,3),(33,2),(34,<EUGPSCoordinates>2),(37,<EUGPSCoordinates>2),(38,<EUGPSCoordinates>1)]
