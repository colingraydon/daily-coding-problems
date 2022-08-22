// You are given a huge list of airline ticket prices between different cities around the world on a given day. 
// These are all direct flights. Each element in the list has the format (source_city, destination, price).
// Consider a user who is willing to take up to k connections from their origin city A to their destination B. 
// Find the cheapest fare possible for this journey and print the itinerary for that journey.

// I implemented a breadth first search here. Perhaps some pathfinding algo like Djikstra might be more efficient
import java.util.PriorityQueue;
import java.util.ArrayList;

public class Flight {

    public String start;
    public String end;
    public int cost;

    public Flight(String start, String end, int cost) {
        this.start = start;
        this.end = end;
        this.cost = cost;

    }

    public static void findFlight(Flight[] arr, String startPoint, String endPoint, int maxConnectionsAllowed) {
        boolean foundATrip = false;
        FlightList bestTrip = new FlightList();

        PriorityQueue<FlightList> q = new PriorityQueue<FlightList>();
        for (Flight f : arr) {
            if (f.start.equals(startPoint)) {
                ArrayList<Flight> tempList = new ArrayList<Flight>();
                tempList.add(f);
                FlightList temp = new FlightList(f, tempList, f.end, f.cost);
                q.add(temp);
            }
        }

        if (q.isEmpty()) {
            System.out.println("There are no flights possible");
        }

        // Here we perform a breadth first search and add update the min cost for the
        // trip. elements will be removed from the queue when they either reach the
        // destination or exceed the current best cost. elements are added to the queue
        // when there is a flight that
        // leaves their current city and arrives at another city.
        while (!q.isEmpty()) {
            FlightList temp = q.poll();
            String currentDestination = temp.end;
            for (Flight f : arr) {
                if (f.end.equals(endPoint) && f.start.equals(currentDestination)) {
                    if (foundATrip == false || ((temp.totalCost + f.cost) < bestTrip.totalCost)) {
                        bestTrip.setFlight(f);
                        bestTrip.setList(f);
                        bestTrip.setEnd(f.end);
                        bestTrip.setTotalCost(f.cost);

                    }
                }

                // only add it to queue if it beats the best cost or a trip has not been yet
                // found, and if it is within the allowed number of connections
                else if (f.start.equals(currentDestination)) {
                    if ((temp.list.size() < maxConnectionsAllowed)
                            && (((temp.totalCost + f.cost) < bestTrip.totalCost) || foundATrip == false)) {
                        temp.setList(f);
                        FlightList tempFlightList = new FlightList(f, temp.list, f.end, f.cost + temp.totalCost);
                        q.add(tempFlightList);
                    }
                }
            }
        }

        if (!foundATrip) {
            System.out.println("There is no available flight pattern given this number of connections");
        } else {
            System.out.println("Total cost is" + bestTrip.totalCost);
            System.out.println("Flight list is as follows");
            for (Flight f : bestTrip.list) {
                System.out.println("Flight beginning " + f.start + "Flight ending" + f.end);
            }
        }

    }
}