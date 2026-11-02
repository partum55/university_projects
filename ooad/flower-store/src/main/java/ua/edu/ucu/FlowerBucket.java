package ua.edu.ucu;

import java.util.ArrayList;
import java.util.List;

public class FlowerBucket {
    private List<FlowerPack> flowerPacks;

    public FlowerBucket() {
        this.flowerPacks = new ArrayList<>();
    }

    public void add(FlowerPack flowerPack) {
        flowerPacks.add(flowerPack);
    }

    public double getPrice() {
        double total = 0.0;
        for (FlowerPack flowerPack : flowerPacks) {
            total += flowerPack.getPrice();
        }
        return total;
    }
}
