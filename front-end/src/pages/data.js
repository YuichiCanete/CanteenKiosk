import {ref} from 'vue'

class StartData {
    constructor() {
        this.myUrl = ''
        this.orderNum = 0;
        this.payType = 'cash'
        this.foodList = [];
        this.orderList = [];
        this.userList = [];
        this.currentUser = {}

        // <th>ID</th>
        // <th>Order</th>
        // <th>Payment Type</th>
        // <th>Total</th>
        // <th>Date</th>
        // <th>Actions</th>
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

        let userOrder = {
            orderNum: this.orderNum,
            foodList: this.foodList,
            payType: this.payType,
            date: '0000-00-00'
        };

        this.orderList.push(userOrder);
        // this.resetOrder()
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

    getTotal(fl){
        let total = 0
        fl.forEach(function(food){
            total += food.quantity * food.price
        })
        return total
    }
}

// Example usage:
const data = ref(new StartData())
export { data };
