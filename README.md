# parmult-bench
A naive parallelization benchmark

## Usage
Simply type
```
./parmult-bench NWORKERS_MAX MATRIX_ORDER
```
where `NWORKERS_MAX` is the maximal numbers of workers (processes) to be tested,
and `MATRIX_ORDER` is the order of the square matrices to be multiplied.

## Example
For instance, on my (not very recent) two-core laptop I get
```
$ ./parmult-bench 4 2e3
NWORKERS_MAX:     4
MATRIX_ORDER:     2e3
OMP_NUM_THREADS:  1
OUTPUT:           EliteBookZZ-4-2e3-20200217-10h35.data

nworkers=1  (NWORKERS_MAX=4)
Starting job 1/1
 => RUNTIME=0.89

nworkers=2  (NWORKERS_MAX=4)
Starting job 1/2
Starting job 2/2
 => RUNTIME=0.95

nworkers=3  (NWORKERS_MAX=4)
Starting job 1/3
Starting job 2/3
Starting job 3/3
 => RUNTIME=1.56

nworkers=4  (NWORKERS_MAX=4)
Starting job 1/4
Starting job 2/4
Starting job 3/4
Starting job 4/4
 => RUNTIME=1.69
```

The output data is available is a CSV file for further processing:
```
$ cat EliteBookZZ-4-2e3-20200217-10h35.data 
nworkers, runtime
1, 0.89
2, 0.95
3, 1.56
4, 1.69
```

