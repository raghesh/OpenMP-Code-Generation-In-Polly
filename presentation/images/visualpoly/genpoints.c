int main()
{
	for (int i = -10; i < 10; i++)
		for (int j = -10; j <= 10; j++)
			for (int k = -10; k < 10; k++)
				if ((k <= 1) && (k >= 0) && (i <= j) && (i + j) >= k && (i + 4*k) <= 4*j)
					printf("%d %d %d\n", i, j, k);

	return 0;
}
