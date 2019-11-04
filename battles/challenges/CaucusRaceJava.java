// java semi brute force solution, python times out

// https://sites.google.com/site/indy256/algo/sparse_table_rmq

public int[] logTable(int n) {
    int[] logTable = new int[n + 1];
    for (int i = 2; i <= n; i++)
        logTable[i] = logTable[i >> 1] + 1;
    return logTable;
}

public int[][] RmqSparseTable(int[] a) {
    int n = a.length;

    int[] logTable = logTable(n);
    
    int[][] rmq = new int[logTable[n] + 1][n];

    for (int i = 0; i < n; ++i)
        rmq[0][i] = i;

    for (int k = 1; (1 << k) < n; ++k) {
        for (int i = 0; i + (1 << k) <= n; i++) {
            int x = rmq[k - 1][i];
            int y = rmq[k - 1][i + (1 << k - 1)];
            rmq[k][i] = a[x] <= a[y] ? x : y;
        }
    }
    return rmq;
}

public int minPos(int[] logTable, int[][] rmq, int[] a, int i, int j) {
    int k = logTable[j - i];
    int x = rmq[k][i];
    int y = rmq[k][j - (1 << k) + 1];
    return a[x] <= a[y] ? x : y;
}

int[] computeCycle(int[] values) {
    int valuesLen = values.length;
    int cycleLen = valuesLen * 2;
    int[] cycle = new int[cycleLen];
    int runningSum = 0;
    for (int i = 0; i < cycleLen; i++) {
        runningSum += values[i % valuesLen];
        cycle[i] = runningSum;
    }
    return cycle;
}

int[] toIntArray(List<Integer> list)  {
    int[] ret = new int[list.size()];
    int i = 0;
    for (Integer e : list)  
        ret[i++] = e.intValue();
    return ret;
}

int[] caucusRace(int[] values) {
    int valuesLen = values.length;
  
    // int[] answer = new int[values.length];
    List<Integer> winners = new ArrayList<Integer>();
    int[] cycle = computeCycle(values);
  
    int cycleLen = cycle.length;
  
    int[] logTable = logTable(cycleLen);
    int[][] rmq = RmqSparseTable(cycle);
  
    int offset = 0;
    int L = 0;
    int R = 0;
    int minPos = 0;
    int curMin = 0;
  
    int k = 0;
    int x = 0;
    int y = 0;
    for (int i = 0; i < valuesLen; i++) {
        L = i;
        R = i + valuesLen - 1;
    
        k = logTable[R - L];
        x = rmq[k][L];
        y = rmq[k][R - (1 << k) + 1];
    
        if (cycle[x] <= cycle[y]) {
            minPos = x;
        } else {
            minPos = y;
        }
    
        curMin = cycle[minPos];
        if (curMin + offset > 0) {
            winners.add(i);
        }
        offset = -cycle[i];
    }
    int[] answer = toIntArray(winners);

    return answer;
}
