# mdb_graphlookup

- I am seeing different results when using $graphLookup aggregation vs. recursive find() queries.

- I tested this with MongoDB 5.0.15, 6.0.11, and 7.0.2 and the results are the same.

# steps to reproduce
- install my database using the following command:
  - `mongoimport -d mdb_test -c graphLookup db`
- install pymongo
  - `pip install pymongo`
- run `python test_graphlookup_vs_recursive_find.py`

There are two chunks of output -- one for recursive find() and one for graphLookup.
The output is row_number parent child

If you look at REQaEjncVH, you will see it is a child of cHAJOAjUij.

In the recursive find method, REQaEjncVH shows up as a child the two times cHAJOAjUij is referenced.

In the graphLookup method, REQaEjncVH shows up as a child only once for cHAJOAjUij. cHAJOAjUij correctly shows up twice.
