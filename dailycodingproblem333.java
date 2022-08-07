// At a party, there is a single person who everyone knows, but who does not know anyone in return (the "celebrity"). To help figure out who this is, you have access to an O(1) method called knows(a, b), which returns True if person a knows person b, else False.

// Given a list of N people and the above operation, find a way to identify the celebrity in O(N) time.
//The list of attendees is represented by a 2d matrix here, where 0 represents not knowing another attendee and 1 represents knowing them.
import java.util.Stack;

public class dailycodingproblem333 {
    
    static int m[][] = {{0, 1, 0}, {0, 0, 0}, {1, 1, 0}};

    static boolean knows(int a, int b) {

        boolean result = false;
        if (m[a][b] == 1) {
            result = true;
        }
        return result;
    }

    //Here is the logic. A stack of all attendees is created and 2 attendees are examined. For someone to be the potential celebrity, they must not know another person. 
    //Comparisons are made and if someone is a potential celebrity, they are added to the back of the stack and then compared to a different attendee when they come up again.
    //I think this is O(n) not O(n log n)
    static int getCelebrity(int n) {

        Stack<Integer> possibleCelebrities = new Stack<>();
        for (int i = 0; i < n; i++) {
            possibleCelebrities.push(i);
        }
        while (possibleCelebrities.size() > 1)
        {
            int person1 = possibleCelebrities.pop();
            int person2 = possibleCelebrities.pop();
            if (knows(person1, person2) == true) {
                possibleCelebrities.push(person2);
            }
            else {
                possibleCelebrities.push(person1);
            }
        }
        return possibleCelebrities.pop();
    }


}
