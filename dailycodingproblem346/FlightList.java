import java.util.ArrayList;

public class FlightList {

    public ArrayList<Flight> list;
    public String end;
    public int totalCost;
    public Flight flight;

    public FlightList() {

    }

    public FlightList(Flight flight, ArrayList<Flight> list, String end, int totalCost) {
        this.flight = flight;
        this.list = list;
        this.end = end;
        this.totalCost = totalCost;
    }

    public void setFlight(Flight f) {
        this.flight = f;
    }

    public void setList(Flight f) {
        ArrayList<Flight> tempList = this.list;
        tempList.add(f);
        this.list = tempList;
    }

    public void setEnd(String s) {
        this.end = s;
    }

    public void setTotalCost(int c) {
        int temp = this.totalCost;
        temp += c;
        this.totalCost = temp;
    }
}