// You have access to ranked lists of songs for various users. Each song is represented as an integer, and more preferred songs appear earlier in each list. 
//For example, the list [4, 1, 7] indicates that a user likes song 4 the best, followed by songs 1 and 7.

// Given a set of these ranked lists, interleave them to create a playlist that satisfies everyone's priorities.
//This problem would have been far simpler in Python but I haven't used java for a while so I did it here. Time is O(n), with n as the total number of elements in the input arrays

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.LinkedList;
import java.util.Collections;

public class dailycodingproblem360 {

    public static HashMap<Integer, Integer> createPlaylist(int[][] input) {
        HashMap<Integer, Integer> songList= new HashMap<Integer, Integer>();
        HashSet<Integer> allSongs = new HashSet<Integer>();

        //This gets the set of all songs - we need the total number of songs for the scoring system.
        for (int[] arr: input) {
            for (int song: arr) {
                Integer temp = Integer.valueOf(song);
                allSongs.add(temp);
            }
        }

        //This iterates through all the input arrays and finds the score of each song, placing it in a Hashmap
        //We are weighting the scores of any songs that appear more than once when we add them back into the array
        int numberOfSongs = allSongs.size();

        //2 is chose arbitrarily
        int weightingBonus = 2;
        for (int[] arr: input) {
            for (int i = 0; i < arr.length; i ++) {
                Integer tempI = Integer.valueOf(i);
                if(songList.containsKey(i)) {
                    int score = songList.get(i).intValue();
                    score = score + (numberOfSongs - i) + weightingBonus;
                    Integer tempScore = Integer.valueOf(score);
                    songList.put(tempI, tempScore);
                }
                else {
                    Integer tempScore = Integer.valueOf(numberOfSongs - i);
                    songList.put(tempI, tempScore);
                }
            }
        }

        //Creates a linked list of all the songs, then sorts the list based on compared values (scores)
        //Creates a linkedHashMap based off of that result, this hashmap is then returned with an order of highest to lowest scored songs
        List<Map.Entry<Integer, Integer> > list = new LinkedList<Map.Entry<Integer, Integer> >(songList.entrySet());
        Collections.sort(list, (i1, i2) -> i2.getValue().compareTo(i1.getValue()));
        HashMap<Integer, Integer> result = new LinkedHashMap<Integer, Integer>();
        for (Map.Entry<Integer, Integer> i: list) {
            result.put(i.getKey(), i.getValue());
        }
        return result;


    }
}

