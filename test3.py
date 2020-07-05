x = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
chunks, chunk_size = len(x), int(len(x)/2)
a = [ x[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]
print(a)