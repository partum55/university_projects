package ua.edu.ucu;

import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

@Getter
@Setter
@ToString
public class Flower {
    private double sepalLength;
    private FlowerColor color;
    private double price;
    private FlowerType flowerType;

    public Flower(double sepalLength, FlowerColor color, double price, FlowerType flowerType) {
        this.sepalLength = sepalLength;
        this.color = color;
        this.price = price;
        this.flowerType = flowerType;
    }

    public Flower(Flower flower) {
        this.sepalLength = flower.getSepalLength();
        this.color = FlowerColor.valueOf(flower.getColor());
        this.price = flower.getPrice();
        this.flowerType = flower.getFlowerType();
    }

    public String getColor() {
        return color.toString();
    }
}
