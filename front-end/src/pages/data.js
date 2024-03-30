
import {ref} from 'vue'

class StartData {
    constructor() {
        this.orderNum = 0;
        this.foodList = [];
        this.orderList = [];
        this.userOrder = {
            number: 0
        };
    }

    incrementOrder() {
        this.orderNum += 1;
    }

    addFood(name, inventory, price) {
        this.foodList.push({
            name: name,
            inventory: inventory,
            price: price,
            quantity: 1
        });
    }

    addOrder() {
        this.orderList.push(this.userOrder);
    }

    addFoodToOrder(name){
        this.foodList.forEach(function(food){
            if (food.name === name){
                food.quantity += 1
                console.log(food)
            }
        })
        console.log('Added')
    }

    getTotal(){
        let total = 0
        this.foodList.forEach(function(food){
            total += food.quantity * food.price
        })
        return total
    }
}

// Example usage:
const data = new StartData()

export { data };
