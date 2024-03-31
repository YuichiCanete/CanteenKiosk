
import {ref} from 'vue'

class StartData {
    constructor() {
        this.orderNum = 0;
        this.foodList = [];
        this.orderList = [];
        this.userList = [];
        this.currentUser = {}
        this.userOrder = {
            number: 0
        };
    }

    loginUser(user){
        this.currentUser = user;
        console.log("Welcome: "+user.userID)
    }

    addUser(userID,password,userType){
        this.userList.push({
            userID:userID,
            password:password,
            userType:userType
        })
    }

    incrementOrder() {
        this.orderNum += 1;
    }

    addFood(name, inventory, price) {
        this.foodList.push({
            name: name,
            inventory: inventory,
            price: price,
            quantity: 0
        });
    }

    addOrder() {
        this.orderNum += 1
        this.orderList.push(this.userOrder);
        this.resetOrder()
    }

    resetOrder(){
        this.foodList.forEach(function(food){
            food.quantity = 0
        })
    }

    addFoodToOrder(name){
        this.foodList.forEach(function(food){
            if (food.name === name){
                food.quantity += 1
                console.log(food)
            }
        })
    }

    incrementFood(name){
        this.foodList.forEach(function(food){
            if (food.name === name & food.quantity < food.inventory){
                food.quantity += 1
            }
        })
    }

    decrementFood(name){
        this.foodList.forEach(function(food){
            if (food.name === name & food.quantity > 0){
                food.quantity -= 1
                console.log(food)
            }
        })
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
const data = ref(new StartData())
export { data };
