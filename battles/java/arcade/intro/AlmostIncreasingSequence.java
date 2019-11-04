import java.util.*;

public class AlmostIncreasingSequence {
    
    static boolean isInc(List<Integer> seqList) {
        Integer[] sequence;
        sequence = seqList.toArray(new Integer[seqList.size()]);
        int first = sequence[0];
        for (int i = 1; i < sequence.length; i++) {
            if (sequence[i] - first <= 0) {
                return false;
            }
            first = sequence[i];
        }
        return true;
    }

    static boolean almostIncreasingSequence(int[] sequence) {
        List<Integer> newSeq = new ArrayList<>();
        List<Integer> newSeqRight = new ArrayList<>();
        int skip = 0;
        int first = sequence[0];
        
        for (int i = 1; i < sequence.length; i++) {
            // System.out.print(i + " " + first + " ");
            // System.out.println(sequence[i]);
            if (sequence[i] <= first) {
                skip = i-1;
                break;
            }
            first = sequence[i];
        }
        // System.out.println("skip = " + skip);
        for (int i = 0; i < sequence.length; i++) {
            if (i != skip) {
                newSeq.add(sequence[i]);
            }
        }
        for (int i = 0; i < sequence.length; i++) {
            if (i != skip+1 && skip < sequence.length-1) {
                newSeqRight.add(sequence[i]);
            }
        }
        //System.out.println(newSeq);
        //System.out.println(newSeqRight);
        return isInc(newSeq) || isInc(newSeqRight);
    }

    public static void main(String[] args) {
        int[] seq = {1, 3, 2, 3};
        System.out.println(almostIncreasingSequence(seq));
    }
}
