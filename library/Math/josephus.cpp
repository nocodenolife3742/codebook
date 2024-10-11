int josephus(int n, int k, int p) {
    int ans = (k - 1) % (n - p);
    for (int i = n - p + 1; i = n; i++)
        ans = (ans + k) % i;
    return ans;
}
