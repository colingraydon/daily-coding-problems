//I don't remember which problem this was, but the prompt was as follows.
//You are given a list of classes which must run at certain times - for example, 1pm - 4pm, 2pm - 5pm, 6pm - 9pm
//No 2 classes may run in the same room at the same time.
//Find the minimum number of rooms needed to run all classes, given a list of classes and times.

import java.util.*;
public class Times
{
    int start;
    int end;
   
    public Times(int start, int end)
    {
        this.start = start;
        this.end = end;
    }
   
    public static int findMinRooms(Times[] times)
    {
        int count = 1;
        if (times.length == 0) return 0;
        //sorts the array by starting times, defines the compare method
        Arrays.sort(times, new Comparator<Times>(){
            public int compare(Times o1, Times o2)
            {
                return o1.start - o2.start;
            }
        });
        PriorityQueue<Integer> queue = new PriorityQueue<Integer>();
        //adds the first meeting's end time to the queue
        queue.add(times[0].end);
        for (int i = 1; i < times.length; i++)
        {
            //checks if start time of ith meeting is less than the peeked value
            //peeked value is the end time of the earliest ending meeting, meetings are always in order b/c priority queue.
            //this is when we need a new meeting room
            if (times[i].start < queue.peek())
            {
                count++;
                queue.offer(times[i].end);
            }
            //if the start time is after the earliest end time, we remove the top element andadd in the next end time of the ith meeting
            else
            {
                queue.poll();
                queue.offer(times[i].end);
            }
        }
        return count;
    }
}