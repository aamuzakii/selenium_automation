>>> from itertools import islice
>>> data = ws.values
>>> cols = next(data)[1:]
>>> data = list(data)
>>> idx = [r[0] for r in data]
>>> data = (islice(r, 1, None) for r in data)
>>> df = pd.DataFrame(data, index=idx, columns=cols)
