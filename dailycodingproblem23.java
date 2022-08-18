// You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.
// Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. 
// If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.

import java.util.*;
public class dailycodingproblem23 {

    int x;
    int y;
    int distance;
   
    public dailycodingproblem23(int x, int y, int distance)
    {
        this.x = x;
        this.y = y;
        this.distance = distance;
    }
   
    public boolean isSpaceValid(boolean[][]array, int boardLength, int boardHeight, boolean[][]visited, int x, int y)
    {
        int M = array[0].length;
        int N = array.length;
        if (x >= 0 && y >= 0 && x < M && y < N && visited[x][y] && !array[x][y])
        {
            return true;
        }
        else return false;
    }
   
    public void findShortestPath(boolean[][]array, int startX, int startY, int endX, int endY)
    {
        int M = array[0].length;
        int N = array.length;
        int count = 0;
        boolean[][]visited = new boolean[N][M];
        for (int i = 0; i < M; i++)
        {
            for (int j = 0; j < N; j++)
            {
                visited[i][j] = false;
            }
        }
        Queue<dailycodingproblem23> list = new LinkedList<dailycodingproblem23>();
        dailycodingproblem23 firstSpace = new dailycodingproblem23(startX, startY, 0);
        list.offer(firstSpace);
        visited[startY][startX] = true;
        while (!list.isEmpty())
        {
            dailycodingproblem23 temp = list.poll();
            visited[temp.x][temp.y] = true;
            if (temp.x == endX && temp.y == endY)
            {
                System.out.println(temp.distance);
            }
            if (isSpaceValid(array, M, N, visited, temp.x + 1, temp.y))
            {
                temp.distance++;
                dailycodingproblem23 nextSpace = new dailycodingproblem23(temp.x + 1, temp.y, temp.distance);
                list.offer(nextSpace);
            }
            if (isSpaceValid(array, M, N, visited, temp.x - 1, temp.y))
            {
                temp.distance++;
                dailycodingproblem23 nextSpace = new dailycodingproblem23(temp.x - 1, temp.y, temp.distance);
                list.offer(nextSpace);
            }
            if (isSpaceValid(array, M, N, visited, temp.x, temp.y + 1))
            {
                temp.distance++;
                dailycodingproblem23 nextSpace = new dailycodingproblem23(temp.x, temp.y + 1, temp.distance);
                list.offer(nextSpace);
            }
            if (isSpaceValid(array, M, N, visited, temp.x, temp.y - 1))
            {
                temp.distance++;
                dailycodingproblem23 nextSpace = new dailycodingproblem23(temp.x, temp.y - 1, temp.distance);
                list.offer(nextSpace);
            }
        }
       
    }
}