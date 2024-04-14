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
        this.orderNum += 1;
        const newFoodList = [...this.foodList];
        const newPayType = this.payType;
        const userOrder = {
            orderNum: this.orderNum,
            foodList: newFoodList,
            payType: newPayType,
            date: '0000-00-00'
        };
        this.orderList.push({...userOrder}); 
        console.log(userOrder)
        this.resetOrder();
        console.log(userOrder)
    }
    
    
    resetOrder() {
        const newFoodList = this.foodList.map(food => ({ ...food }));
        newFoodList.forEach(function (food) {
            food.quantity = 0;
        });
        this.foodList = newFoodList;
    }
    

    addFoodToOrder(name){
        this.foodList.forEach(function(food){
            if (food.name === name){
                food.quantity += 1
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
