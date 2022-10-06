// You are given an unsorted list of 999,000 unique integers, each from 1 and 1,000,000. Find the missing 1000 numbers. What is the computational and space complexity of your solution?

import java.util.PriorityQueue;
import java.util.ArrayList;

public class dailycodingproblem390 {

    static ArrayList<Integer> myMethod(int[] data) {

        boolean first = false; 
        PriorityQueue<Integer> q = new PriorityQueue<Integer>();
        ArrayList<Integer> ans = new ArrayList<Integer>();
        int n = data.length;
        for (int i = 0; i < n; i++) {
            Integer temp = Integer.valueOf(data[i]);
            q.add(temp);
        }

        while(q.peek() != null) {
            Integer tempVal = q.poll();
            if (!first) {
                if (tempVal > 1) {
                    for (int i = 1; i < tempVal; i++) {
                        ans.add(i);
                    }
                }
                Integer prev = tempVal;
                first = true;
            }
            else {
                if (tempVal - prev > 1) {
                    for (int i = prev + 1; i < tempVal; i++) {
                        ans.add(i)
                    }
                }
                prev = tempVal;
            }
        }

        return ans;
    }
    
}
