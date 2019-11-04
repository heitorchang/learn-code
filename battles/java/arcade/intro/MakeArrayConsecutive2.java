// 6

// https://stackoverflow.com/questions/1484347/finding-the-max-min-value-in-an-array-of-primitives-using-java

import java.util.Set;
import java.util.List;
import java.util.stream.Collectors;
import java.util.HashSet;
import java.util.Arrays;
import java.util.IntSummaryStatistics;

public class MakeArrayConsecutive2 {
    public static int makeArrayConsecutive2(int[] statues) {
        IntSummaryStatistics stat = Arrays.stream(statues).summaryStatistics();
        int left = stat.getMin();
        int right = stat.getMax();

        int answer = 0;
        List<Integer> statuesList = Arrays.stream(statues).boxed().collect(Collectors.toList());
        Set<Integer> statuesSet = new HashSet<Integer>(statuesList);
        
        for (int i = left; i <= right; i++) {
            if (!statuesSet.contains(i)) {
                answer += 1;
            }
        }
        return answer;
    }
    
    public static void main(String[] args) {
        int[] myStatues = {6,2,3,8};
        System.out.println(makeArrayConsecutive2(myStatues));
    }
}
