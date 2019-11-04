// 5

int shapeArea(int n) {
    int ans = 1;
    for (int i = 1; i < n; i++) {
        ans += 4 * i;
    }
    return ans;
}
