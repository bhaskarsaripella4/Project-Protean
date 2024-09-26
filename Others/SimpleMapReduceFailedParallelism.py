
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor as Executor
# https://freecontent.manning.com/implementing-a-mapreduce-framework-using-python-threads/

emitter = lambda word: (word,1)
# counter = lambda (word,emissions): (work, sum(emissions))

def counter(shuffledDict):
    # return [(count[0],sum(count[1])) for count in shuffledDict.items()] #using list comprehension
    return (shuffledDict[0],sum(shuffledDict[1]))



def map_reduce_ultra_naive(my_input, mapper):
    map_results = map(mapper,my_input)

    shuffler = defaultdict(list)
    for key, value in map_results:
        shuffler[key].append(value)
    return map(counter, shuffler.items())
    # return counter(shuffler) #to use list comprehension


def counter_distributed(shuffledDict):
       return (shuffledDict[0],sum(shuffledDict[1]))

# a concurrent implementation of the above map_reduce using multithreading
def map_reduce_still_naive(my_input, mapper):
    with Executor() as executor:
        map_results = executor.map(mapper, my_input)

        distributor = defaultdict(list)
        for key,value in map_results:
            distributor[key].append(value)

        results = executor.map(counter_distributed,distributor.items())
    return results

words = "Python is great Python rocks".split()
print(list(map_reduce_ultra_naive(words,emitter)))
print(list(map_reduce_still_naive(words,emitter)))

