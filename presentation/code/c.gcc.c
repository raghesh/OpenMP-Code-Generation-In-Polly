float A[1024];

int main()
{
  int i, j;
  #pragma omp parallel for \
  schedule(runtime) private(j)
  for (i = 0; i < 1024; i++)
    for (j = 0; j < 5000000; j++)
      A[i] += j;
}
